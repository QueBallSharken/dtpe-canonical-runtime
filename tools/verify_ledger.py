import base64
import json
from pathlib import Path
from typing import Any, Dict, List

from core.canonical import canonical_json
from core.crypto.registry import get_crypto_verifier, initialize_builtin_registry
from core.hashing import sha256_hex_str
from core.identity.identity_registry import load_identity, resolve_identity_key_record
from core.paths import DATA_DIR
from core.spectre.boundary import evaluate_execution_boundary
from core.spectre.evaluator_rules import (
    get_boundary_evaluator_rule_hash,
    get_boundary_evaluator_rule_profile,
    resolve_evaluator_rule_profile,
)


LEDGER_PATH = DATA_DIR / "ledger.log"


def _load_lines(path: Path) -> List[str]:
    if not path.exists():
        raise RuntimeError(f"Ledger file missing: {path}")

    return [line for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def _verify_receipt_payload(payload: Dict[str, Any], index: int) -> None:
    required_fields = [
        "execution_state",
        "reason",
        "authority_hash",
        "policy_state_hash",
        "crypto_profile",
        "receipt_canonical",
        "receipt_hash",
    ]

    for field in required_fields:
        if field not in payload:
            raise RuntimeError(f"Ledger record {index}: payload missing {field}")

    receipt_material = {
        "execution_state": payload.get("execution_state"),
        "reason": payload.get("reason"),
        "authority_hash": payload.get("authority_hash"),
        "policy_state_hash": payload.get("policy_state_hash"),
        "crypto_profile": payload.get("crypto_profile"),
    }

    evaluator_trace = payload.get("evaluator_trace")
    if evaluator_trace is None:
        raise RuntimeError(f"Ledger record {index}: payload missing evaluator_trace")
    if not isinstance(evaluator_trace, dict):
        raise RuntimeError(f"Ledger record {index}: evaluator_trace must be a JSON object")

    required_evaluator_trace_fields = {
        "evaluator_id": str,
        "evaluator_rule_profile": dict,
        "evaluator_rule_hash": str,
        "decision_space_hash": str,
        "signal_profile_hash": str,
        "policy_hash": str,
        "authority_hash": str,
        "execution_intent": str,
        "constraint_profile": str,
        "temporal_rule_profile": str,
        "evaluator_trace_version": str,
    }

    if set(evaluator_trace.keys()) != set(required_evaluator_trace_fields.keys()):
        raise RuntimeError(f"Ledger record {index}: evaluator_trace fields invalid")

    for field, expected_type in required_evaluator_trace_fields.items():
        if not isinstance(evaluator_trace.get(field), expected_type):
            raise RuntimeError(
                f"Ledger record {index}: evaluator_trace field {field} must be {expected_type.__name__}"
            )

    receipt_material["evaluator_trace"] = evaluator_trace

    state_admissibility_present = "state_admissibility_result" in payload
    stability_present = "stability_result" in payload
    temporal_present = "temporal_invariant_result" in payload
    execution_time_present = "execution_time" in payload

    if state_admissibility_present != stability_present:
        raise RuntimeError(
            f"Ledger record {index}: boundary receipt state/stability fields must appear together"
        )

    if temporal_present != execution_time_present:
        raise RuntimeError(
            f"Ledger record {index}: temporal_invariant_result and execution_time must appear together"
        )

    if state_admissibility_present:
        state_admissibility_result = payload.get("state_admissibility_result")
        stability_result = payload.get("stability_result")

        if not isinstance(state_admissibility_result, dict):
            raise RuntimeError(
                f"Ledger record {index}: state_admissibility_result must be a JSON object"
            )

        if not isinstance(stability_result, dict):
            raise RuntimeError(
                f"Ledger record {index}: stability_result must be a JSON object"
            )

        receipt_material["state_admissibility_result"] = state_admissibility_result
        receipt_material["stability_result"] = stability_result

    if temporal_present:
        temporal_invariant_result = payload.get("temporal_invariant_result")
        execution_time = payload.get("execution_time")

        if not isinstance(temporal_invariant_result, dict):
            raise RuntimeError(
                f"Ledger record {index}: temporal_invariant_result must be a JSON object"
            )

        if not isinstance(execution_time, str):
            raise RuntimeError(
                f"Ledger record {index}: execution_time must be a string"
            )

        receipt_material["temporal_invariant_result"] = temporal_invariant_result
        receipt_material["execution_time"] = execution_time

    authority_result = payload.get("authority_result")
    if authority_result is not None:
        if not isinstance(authority_result, dict):
            raise RuntimeError(f"Ledger record {index}: authority_result must be a JSON object")
        receipt_material["authority_result"] = authority_result

    canonical_current_state = payload.get("canonical_current_state")
    if canonical_current_state is not None:
        if not isinstance(canonical_current_state, dict):
            raise RuntimeError(
                f"Ledger record {index}: canonical_current_state must be a JSON object"
            )
        receipt_material["canonical_current_state"] = canonical_current_state

    system_state = payload.get("system_state")
    if system_state is not None:
        if not isinstance(system_state, dict):
            raise RuntimeError(f"Ledger record {index}: system_state must be a JSON object")
        receipt_material["system_state"] = system_state

    canonical_transition = payload.get("canonical_transition")
    if canonical_transition is not None:
        if not isinstance(canonical_transition, dict):
            raise RuntimeError(
                f"Ledger record {index}: canonical_transition must be a JSON object"
            )
        receipt_material["canonical_transition"] = canonical_transition

    execution_intent = payload.get("execution_intent")
    if execution_intent is not None:
        if not isinstance(execution_intent, str):
            raise RuntimeError(
                f"Ledger record {index}: execution_intent must be a string"
            )
        receipt_material["execution_intent"] = execution_intent

    frame_continuity_present = "frame_continuity_result" in payload

    if frame_continuity_present:
        frame_continuity_result = payload.get("frame_continuity_result")
        invariant_frame_hash = payload.get("invariant_frame_hash")
        sequence_id = payload.get("sequence_id")
        continuity_mode = payload.get("continuity_mode")
        current_execution_time = payload.get("current_execution_time")

        if not isinstance(frame_continuity_result, dict):
            raise RuntimeError(
                f"Ledger record {index}: frame_continuity_result must be a JSON object"
            )

        if not isinstance(invariant_frame_hash, str):
            raise RuntimeError(
                f"Ledger record {index}: invariant_frame_hash must be a string"
            )

        if not isinstance(sequence_id, str):
            raise RuntimeError(
                f"Ledger record {index}: sequence_id must be a string"
            )

        if not isinstance(continuity_mode, str):
            raise RuntimeError(
                f"Ledger record {index}: continuity_mode must be a string"
            )

        if not isinstance(current_execution_time, str):
            raise RuntimeError(
                f"Ledger record {index}: current_execution_time must be a string"
            )

        receipt_material["frame_continuity_result"] = frame_continuity_result
        receipt_material["invariant_frame_hash"] = invariant_frame_hash
        receipt_material["sequence_id"] = sequence_id
        receipt_material["continuity_mode"] = continuity_mode
        receipt_material["current_execution_time"] = current_execution_time

    continuity_required = payload.get("continuity_required")
    if not isinstance(continuity_required, bool):
        raise RuntimeError(f"Ledger record {index}: continuity_required must be a bool")
    receipt_material["continuity_required"] = continuity_required

    signal_profile = payload.get("signal_profile")
    if not isinstance(signal_profile, dict):
        raise RuntimeError(f"Ledger record {index}: signal_profile missing or invalid")
    receipt_material["signal_profile"] = signal_profile

    decision_space = payload.get("decision_space")
    if not isinstance(decision_space, dict):
        raise RuntimeError(f"Ledger record {index}: decision_space missing or invalid")

    required_decision_space_fields = {
        "policy_hash": str,
        "authority_hash": str,
        "execution_intent": str,
        "constraint_profile": str,
        "signal_profile": dict,
        "decision_space_version": str,
    }

    for field, expected_type in required_decision_space_fields.items():
        if field not in decision_space:
            raise RuntimeError(
                f"Ledger record {index}: decision_space missing required field {field}"
            )
        if not isinstance(decision_space[field], expected_type):
            raise RuntimeError(
                f"Ledger record {index}: decision_space field {field} must be {expected_type.__name__}"
            )

    for forbidden_field in [
        "visible_alternatives_profile",
        "risk_frame_profile",
        "sequence_id",
    ]:
        if forbidden_field in decision_space:
            raise RuntimeError(
                f"Ledger record {index}: decision_space contains forbidden field {forbidden_field}"
            )

    decision_space_signal_profile = decision_space["signal_profile"]

    required_signal_profile_fields = {
        "state_admissibility": dict,
        "system_stability": dict,
        "temporal_invariant": dict,
        "frame_continuity": dict,
        "signal_profile_version": str,
    }

    for field, expected_type in required_signal_profile_fields.items():
        if field not in decision_space_signal_profile:
            raise RuntimeError(
                f"Ledger record {index}: decision_space.signal_profile missing required field {field}"
            )
        if not isinstance(decision_space_signal_profile[field], expected_type):
            raise RuntimeError(
                f"Ledger record {index}: decision_space.signal_profile field {field} must be {expected_type.__name__}"
            )

    for field in ["state_admissibility", "system_stability", "temporal_invariant"]:
        nested_obj = decision_space_signal_profile[field]
        if "ok" not in nested_obj or "reason" not in nested_obj:
            raise RuntimeError(
                f"Ledger record {index}: decision_space.signal_profile.{field} missing ok/reason"
            )
        if not isinstance(nested_obj["ok"], bool):
            raise RuntimeError(
                f"Ledger record {index}: decision_space.signal_profile.{field}.ok must be a bool"
            )
        if not isinstance(nested_obj["reason"], str):
            raise RuntimeError(
                f"Ledger record {index}: decision_space.signal_profile.{field}.reason must be a string"
            )

    frame_continuity_signal = decision_space_signal_profile["frame_continuity"]
    required_frame_continuity_fields = {
        "ok": bool,
        "reason": str,
        "continuity_mode": str,
        "temporal_continuity_ok": bool,
    }

    for field, expected_type in required_frame_continuity_fields.items():
        if field not in frame_continuity_signal:
            raise RuntimeError(
                f"Ledger record {index}: decision_space.signal_profile.frame_continuity missing required field {field}"
            )
        if not isinstance(frame_continuity_signal[field], expected_type):
            raise RuntimeError(
                f"Ledger record {index}: decision_space.signal_profile.frame_continuity field {field} must be {expected_type.__name__}"
            )

    receipt_material["decision_space"] = decision_space

    expected_signal_profile_hash = sha256_hex_str(canonical_json(signal_profile))
    if evaluator_trace.get("signal_profile_hash") != expected_signal_profile_hash:
        raise RuntimeError(f"Ledger record {index}: signal_profile_hash mismatch")

    expected_decision_space_hash = sha256_hex_str(canonical_json(decision_space))
    if evaluator_trace.get("decision_space_hash") != expected_decision_space_hash:
        raise RuntimeError(f"Ledger record {index}: decision_space_hash mismatch")

    evaluator_rule_profile = evaluator_trace.get("evaluator_rule_profile")
    if not isinstance(evaluator_rule_profile, dict):
        raise RuntimeError(f"Ledger record {index}: evaluator_rule_profile missing or invalid")

    evaluator_rule_profile_id = evaluator_rule_profile.get("evaluator_rule_profile_id")
    evaluator_rule_version = evaluator_rule_profile.get("evaluator_rule_version")

    if not isinstance(evaluator_rule_profile_id, str):
        raise RuntimeError(f"Ledger record {index}: evaluator_rule_profile_id must be a string")

    if not isinstance(evaluator_rule_version, str):
        raise RuntimeError(f"Ledger record {index}: evaluator_rule_version must be a string")

    try:
        expected_evaluator_rule_profile = resolve_evaluator_rule_profile(
            evaluator_rule_profile_id=evaluator_rule_profile_id,
            evaluator_rule_version=evaluator_rule_version,
        )
    except ValueError as exc:
        raise RuntimeError(f"Ledger record {index}: {exc}") from None

    if evaluator_rule_profile != expected_evaluator_rule_profile:
        raise RuntimeError(f"Ledger record {index}: evaluator_rule_profile mismatch")

    expected_evaluator_rule_hash = sha256_hex_str(canonical_json(expected_evaluator_rule_profile))
    if evaluator_trace.get("evaluator_rule_hash") != expected_evaluator_rule_hash:
        raise RuntimeError(f"Ledger record {index}: evaluator_rule_hash mismatch")

    if evaluator_trace.get("policy_hash") != payload.get("policy_state_hash"):
        raise RuntimeError(f"Ledger record {index}: evaluator_trace policy_hash mismatch")

    if evaluator_trace.get("authority_hash") != payload.get("authority_hash"):
        raise RuntimeError(f"Ledger record {index}: evaluator_trace authority_hash mismatch")

    if evaluator_trace.get("execution_intent") != payload.get("execution_intent"):
        raise RuntimeError(f"Ledger record {index}: evaluator_trace execution_intent mismatch")

    if evaluator_trace.get("constraint_profile") != payload.get("constraint_profile"):
        raise RuntimeError(f"Ledger record {index}: evaluator_trace constraint_profile mismatch")

    if evaluator_trace.get("temporal_rule_profile") != payload.get("temporal_rule_profile"):
        raise RuntimeError(f"Ledger record {index}: evaluator_trace temporal_rule_profile mismatch")

    constraint_profile = payload.get("constraint_profile")
    if constraint_profile is not None:
        if not isinstance(constraint_profile, str):
            raise RuntimeError(
                f"Ledger record {index}: constraint_profile must be a string"
            )
        receipt_material["constraint_profile"] = constraint_profile

    temporal_rule_profile = payload.get("temporal_rule_profile")
    if temporal_rule_profile is not None:
        if not isinstance(temporal_rule_profile, str):
            raise RuntimeError(
                f"Ledger record {index}: temporal_rule_profile must be a string"
            )
        receipt_material["temporal_rule_profile"] = temporal_rule_profile

    authority_signature_b64 = payload.get("authority_signature_b64")
    if authority_signature_b64 is not None:
        receipt_material["authority_signature_b64"] = authority_signature_b64

    authority_canonical = payload.get("authority_canonical")
    if authority_canonical is not None:
        receipt_material["authority_canonical"] = authority_canonical

    expected_receipt_canonical = canonical_json(receipt_material)
    if payload["receipt_canonical"] != expected_receipt_canonical:
        raise RuntimeError(f"Ledger record {index}: receipt_canonical mismatch")

    expected_receipt_hash = sha256_hex_str(expected_receipt_canonical)
    if payload["receipt_hash"] != expected_receipt_hash:
        raise RuntimeError(f"Ledger record {index}: receipt_hash mismatch")


def _verify_boundary_replay(payload: Dict[str, Any], index: int) -> None:
    authority_result = payload.get("authority_result")
    canonical_current_state = payload.get("canonical_current_state")
    system_state = payload.get("system_state")
    canonical_transition = payload.get("canonical_transition")
    execution_intent = payload.get("execution_intent")
    authority_hash = payload.get("authority_hash")
    policy_state_hash = payload.get("policy_state_hash")
    crypto_profile = payload.get("crypto_profile")
    execution_time = payload.get("execution_time")

    replay_inputs_present = all(
        value is not None
        for value in [
            authority_result,
            canonical_current_state,
            system_state,
            canonical_transition,
            execution_intent,
            authority_hash,
            policy_state_hash,
            crypto_profile,
            execution_time,
        ]
    )

    if not replay_inputs_present:
        return

    replay_result = evaluate_execution_boundary(
        authority_result=authority_result,
        canonical_current_state=canonical_current_state,
        system_state=system_state,
        canonical_transition=canonical_transition,
        canonical_policy_state_hash=policy_state_hash,
        execution_intent=execution_intent,
        authority_hash=authority_hash,
        crypto_profile=crypto_profile,
        execution_time=execution_time,
        constraint_profile=payload.get("constraint_profile"),
        temporal_rule_profile=payload.get("temporal_rule_profile"),
        prior_invariant_frame_hash=payload.get("prior_invariant_frame_hash"),
        prior_execution_time=payload.get("prior_execution_time"),
        continuity_required=payload.get("continuity_required"),
    )

    if payload.get("execution_state") != replay_result.get("execution_state"):
        raise RuntimeError(
            f"Ledger record {index}: boundary replay execution_state mismatch"
        )

    if payload.get("reason") != replay_result.get("reason"):
        raise RuntimeError(
            f"Ledger record {index}: boundary replay reason mismatch"
        )

    recorded_state_result = payload.get("state_admissibility_result")
    recorded_stability_result = payload.get("stability_result")
    recorded_temporal_result = payload.get("temporal_invariant_result")

    if recorded_state_result != replay_result.get("state_admissibility_result"):
        raise RuntimeError(
            f"Ledger record {index}: boundary replay state_admissibility_result mismatch"
        )

    if recorded_stability_result != replay_result.get("stability_result"):
        raise RuntimeError(
            f"Ledger record {index}: boundary replay stability_result mismatch"
        )

    if recorded_temporal_result != replay_result.get("temporal_invariant_result"):
        raise RuntimeError(
            f"Ledger record {index}: boundary replay temporal_invariant_result mismatch"
        )

    if payload.get("evaluator_trace") != replay_result.get("evaluator_trace"):
        raise RuntimeError(
            f"Ledger record {index}: boundary replay evaluator_trace mismatch"
        )


def _verify_authority_signature_if_present(payload: Dict[str, Any], index: int) -> None:
    authority_signature_b64 = payload.get("authority_signature_b64")
    if authority_signature_b64 is None:
        return

    authority_canonical = payload.get("authority_canonical")
    if not isinstance(authority_canonical, str) or not authority_canonical:
        raise RuntimeError(
            f"Ledger record {index}: authority signature present but authority_canonical "
            f"is missing or invalid"
        )

    try:
        authority_obj = json.loads(authority_canonical)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Ledger record {index}: authority_canonical is not valid JSON: {exc}"
        ) from None

    if not isinstance(authority_obj, dict):
        raise RuntimeError(
            f"Ledger record {index}: authority_canonical must decode to a JSON object"
        )

    identity_id = authority_obj.get("identity_id")
    if not isinstance(identity_id, str) or not identity_id.strip():
        raise RuntimeError(
            f"Ledger record {index}: authority_canonical missing non-empty identity_id"
        )

    crypto_profile = payload.get("crypto_profile")
    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        raise RuntimeError(f"Ledger record {index}: crypto_profile missing or invalid")

    identity = load_identity(identity_id)
    key_record = resolve_identity_key_record(identity, crypto_profile)

    public_key_b64 = key_record["public_key_b64"]
    public_key_bytes = base64.b64decode(public_key_b64, validate=True)
    signature_bytes = base64.b64decode(authority_signature_b64, validate=True)
    message_bytes = authority_canonical.encode("utf-8")

    verifier = get_crypto_verifier(crypto_profile)
    verified = verifier(public_key_bytes, message_bytes, signature_bytes)

    if not verified:
        raise RuntimeError(f"Ledger record {index}: authority signature verification failed")


def verify_ledger(path: Path) -> int:
    initialize_builtin_registry()

    lines = _load_lines(path)

    expected_previous_hash = "GENESIS"

    for index, line in enumerate(lines, start=1):
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Ledger record {index}: invalid JSON: {exc}") from None

        if not isinstance(obj, dict):
            raise RuntimeError(f"Ledger record {index}: record must be a JSON object")

        previous_hash = obj.get("previous_hash")
        payload = obj.get("payload")
        record_canonical = obj.get("record_canonical")
        record_hash = obj.get("record_hash")

        if previous_hash != expected_previous_hash:
            raise RuntimeError(
                f"Ledger record {index}: previous_hash mismatch: expected "
                f"{expected_previous_hash!r}, got {previous_hash!r}"
            )

        if not isinstance(payload, dict):
            raise RuntimeError(f"Ledger record {index}: payload missing or invalid")

        if not isinstance(record_canonical, str) or not record_canonical:
            raise RuntimeError(f"Ledger record {index}: record_canonical missing or invalid")

        if not isinstance(record_hash, str) or not record_hash:
            raise RuntimeError(f"Ledger record {index}: record_hash missing or invalid")

        expected_record_material = {
            "previous_hash": previous_hash,
            "payload": payload,
        }
        expected_record_canonical = canonical_json(expected_record_material)

        if record_canonical != expected_record_canonical:
            raise RuntimeError(f"Ledger record {index}: record_canonical mismatch")

        expected_record_hash = sha256_hex_str(expected_record_canonical)
        if record_hash != expected_record_hash:
            raise RuntimeError(f"Ledger record {index}: record_hash mismatch")

        _verify_receipt_payload(payload, index)
        _verify_boundary_replay(payload, index)
        _verify_authority_signature_if_present(payload, index)

        expected_previous_hash = record_hash

    print(f"PASS: verified {len(lines)} ledger record(s)")
    return 0


def main() -> int:
    return verify_ledger(LEDGER_PATH)


if __name__ == "__main__":
    raise SystemExit(main())