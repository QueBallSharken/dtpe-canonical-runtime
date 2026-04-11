import json

from core.paths import DATA_DIR
from core.spectre.evaluator_rules import get_boundary_evaluator_rule_profile
from tools.verify_ledger import verify_ledger


LEDGER_PATH = DATA_DIR / "ledger.log"


def main() -> int:
    if not LEDGER_PATH.exists():
        raise RuntimeError("ledger.log missing before replay verifier test")

    verify_ledger(LEDGER_PATH)

    lines = [line for line in LEDGER_PATH.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if len(lines) != 1:
        raise RuntimeError(f"expected 1 ledger line, got {len(lines)}")

    record = json.loads(lines[0])
    payload = record.get("payload")
    if not isinstance(payload, dict):
        raise RuntimeError("payload missing or invalid")

    required_replay_fields = [
        "authority_result",
        "canonical_current_state",
        "system_state",
        "canonical_transition",
        "execution_intent",
        "execution_time",
        "temporal_invariant_result",
        "frame_continuity_result",
        "invariant_frame_hash",
        "sequence_id",
        "continuity_mode",
        "current_execution_time",
    ]
    for field in required_replay_fields:
        if field not in payload:
            raise RuntimeError(f"payload missing replay field: {field}")

    evaluator_trace = payload.get("evaluator_trace")
    if not isinstance(evaluator_trace, dict):
        raise RuntimeError("payload evaluator_trace missing or invalid")

    required_evaluator_trace_string_fields = [
        "evaluator_id",
        "evaluator_rule_hash",
        "decision_space_hash",
        "signal_profile_hash",
        "policy_hash",
        "authority_hash",
        "execution_intent",
        "constraint_profile",
        "temporal_rule_profile",
        "evaluator_trace_version",
    ]
    for field in required_evaluator_trace_string_fields:
        value = evaluator_trace.get(field)
        if not isinstance(value, str):
            raise RuntimeError(f"payload evaluator_trace field missing or invalid: {field}")

    expected_evaluator_rule_profile = get_boundary_evaluator_rule_profile()
    evaluator_rule_profile = evaluator_trace.get("evaluator_rule_profile")
    if evaluator_rule_profile != expected_evaluator_rule_profile:
        raise RuntimeError(f"unexpected evaluator_rule_profile: {evaluator_rule_profile!r}")

    if evaluator_trace.get("policy_hash") != payload.get("policy_state_hash"):
        raise RuntimeError("payload evaluator_trace policy_hash mismatch")

    if evaluator_trace.get("authority_hash") != payload.get("authority_hash"):
        raise RuntimeError("payload evaluator_trace authority_hash mismatch")

    if evaluator_trace.get("execution_intent") != payload.get("execution_intent"):
        raise RuntimeError("payload evaluator_trace execution_intent mismatch")

    if evaluator_trace.get("constraint_profile") != payload.get("constraint_profile"):
        raise RuntimeError("payload evaluator_trace constraint_profile mismatch")

    if evaluator_trace.get("temporal_rule_profile") != payload.get("temporal_rule_profile"):
        raise RuntimeError("payload evaluator_trace temporal_rule_profile mismatch")

    frame_result = payload.get("frame_continuity_result")
    if not isinstance(frame_result, dict):
        raise RuntimeError("payload frame_continuity_result missing or invalid")

    continuation_disposition = frame_result.get("continuation_disposition")
    if not isinstance(continuation_disposition, str) or not continuation_disposition.strip():
        raise RuntimeError("payload continuation_disposition missing or invalid")

    allowed_dispositions = {
        "continue_initial",
        "continue_exact",
        "continue_authorized_transition",
        "refuse_missing_prior_frame_hash",
        "refuse_missing_prior_execution_time",
        "refuse_temporal_order_violation",
        "refuse_frame_mismatch",
    }
    if continuation_disposition not in allowed_dispositions:
        raise RuntimeError(f"unexpected continuation_disposition: {continuation_disposition!r}")

    print("PASS: phase7 boundary replay verifier path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())