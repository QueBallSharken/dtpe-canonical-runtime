from __future__ import annotations

from typing import Any, Dict, List

from core.canonical import canonical_json
from core.hashing import sha256_hex_str


def build_invariant_frame(
    *,
    policy_hash: str,
    authority_hash: str,
    execution_intent: str,
    constraint_profile: str,
    temporal_rule_profile: str,
) -> Dict[str, str]:
    return {
        "policy_hash": policy_hash,
        "authority_hash": authority_hash,
        "execution_intent": execution_intent,
        "constraint_profile": constraint_profile,
        "temporal_rule_profile": temporal_rule_profile,
    }


def compute_invariant_frame_hash(invariant_frame: Dict[str, str]) -> str:
    return sha256_hex_str(canonical_json(invariant_frame))


def compute_sequence_id(
    *,
    authority_hash: str,
    execution_intent: str,
) -> str:
    sequence_scope = {
        "authority_hash": authority_hash,
        "execution_intent": execution_intent,
    }
    return sha256_hex_str(canonical_json(sequence_scope))


def _frame_result(
    *,
    ok: bool,
    reason: str,
    continuity_mode: str,
    current_invariant_frame_hash: str,
    prior_invariant_frame_hash: str | None,
    transition_authorized: bool,
    sequence_id: str,
    prior_execution_time: str | None,
    current_execution_time: str,
    temporal_continuity_ok: bool,
    continuation_disposition: str,
) -> Dict[str, Any]:
    return {
        "ok": ok,
        "reason": reason,
        "continuity_mode": continuity_mode,
        "current_invariant_frame_hash": current_invariant_frame_hash,
        "prior_invariant_frame_hash": prior_invariant_frame_hash,
        "transition_authorized": transition_authorized,
        "sequence_id": sequence_id,
        "prior_execution_time": prior_execution_time,
        "current_execution_time": current_execution_time,
        "temporal_continuity_ok": temporal_continuity_ok,
        "continuation_disposition": continuation_disposition,
    }


def evaluate_frame_continuity(
    *,
    policy_hash: str,
    authority_hash: str,
    execution_intent: str,
    constraint_profile: str,
    temporal_rule_profile: str,
    current_execution_time: str,
    prior_invariant_frame_hash: str | None,
    prior_execution_time: str | None,
    continuity_required: bool,
    transition_mode: str = "DISABLED",
    allowed_frame_transitions: List[Dict[str, str]] | None = None,
) -> Dict[str, Any]:
    invariant_frame = build_invariant_frame(
        policy_hash=policy_hash,
        authority_hash=authority_hash,
        execution_intent=execution_intent,
        constraint_profile=constraint_profile,
        temporal_rule_profile=temporal_rule_profile,
    )
    current_invariant_frame_hash = compute_invariant_frame_hash(invariant_frame)
    sequence_id = compute_sequence_id(
        authority_hash=authority_hash,
        execution_intent=execution_intent,
    )

    if not continuity_required and prior_invariant_frame_hash is None and prior_execution_time is None:
        return _frame_result(
            ok=True,
            reason="initial_frame",
            continuity_mode="INITIAL",
            current_invariant_frame_hash=current_invariant_frame_hash,
            prior_invariant_frame_hash=None,
            transition_authorized=False,
            sequence_id=sequence_id,
            prior_execution_time=None,
            current_execution_time=current_execution_time,
            temporal_continuity_ok=True,
            continuation_disposition="continue_initial",
        )

    if continuity_required and (not isinstance(prior_invariant_frame_hash, str) or not prior_invariant_frame_hash.strip()):
        return _frame_result(
            ok=False,
            reason="missing_prior_frame_hash",
            continuity_mode="VIOLATION",
            current_invariant_frame_hash=current_invariant_frame_hash,
            prior_invariant_frame_hash=prior_invariant_frame_hash,
            transition_authorized=False,
            sequence_id=sequence_id,
            prior_execution_time=prior_execution_time,
            current_execution_time=current_execution_time,
            temporal_continuity_ok=False,
            continuation_disposition="refuse_missing_prior_frame_hash",
        )

    if continuity_required and (not isinstance(prior_execution_time, str) or not prior_execution_time.strip()):
        return _frame_result(
            ok=False,
            reason="missing_prior_execution_time",
            continuity_mode="VIOLATION",
            current_invariant_frame_hash=current_invariant_frame_hash,
            prior_invariant_frame_hash=prior_invariant_frame_hash,
            transition_authorized=False,
            sequence_id=sequence_id,
            prior_execution_time=prior_execution_time,
            current_execution_time=current_execution_time,
            temporal_continuity_ok=False,
            continuation_disposition="refuse_missing_prior_execution_time",
        )

    temporal_continuity_ok = True
    if isinstance(prior_execution_time, str) and prior_execution_time.strip():
        temporal_continuity_ok = current_execution_time >= prior_execution_time

    if not temporal_continuity_ok:
        return _frame_result(
            ok=False,
            reason="temporal_order_violation",
            continuity_mode="VIOLATION",
            current_invariant_frame_hash=current_invariant_frame_hash,
            prior_invariant_frame_hash=prior_invariant_frame_hash,
            transition_authorized=False,
            sequence_id=sequence_id,
            prior_execution_time=prior_execution_time,
            current_execution_time=current_execution_time,
            temporal_continuity_ok=False,
            continuation_disposition="refuse_temporal_order_violation",
        )

    if current_invariant_frame_hash == prior_invariant_frame_hash:
        return _frame_result(
            ok=True,
            reason="frame_continuity_ok",
            continuity_mode="EXACT",
            current_invariant_frame_hash=current_invariant_frame_hash,
            prior_invariant_frame_hash=prior_invariant_frame_hash,
            transition_authorized=False,
            sequence_id=sequence_id,
            prior_execution_time=prior_execution_time,
            current_execution_time=current_execution_time,
            temporal_continuity_ok=True,
            continuation_disposition="continue_exact",
        )

    if transition_mode == "EXPLICIT_MAP":
        allowed_frame_transitions = allowed_frame_transitions or []
        transition_authorized = any(
            transition.get("from") == prior_invariant_frame_hash
            and transition.get("to") == current_invariant_frame_hash
            for transition in allowed_frame_transitions
        )
        if transition_authorized:
            return _frame_result(
                ok=True,
                reason="authorized_frame_transition",
                continuity_mode="AUTHORIZED_TRANSITION",
                current_invariant_frame_hash=current_invariant_frame_hash,
                prior_invariant_frame_hash=prior_invariant_frame_hash,
                transition_authorized=True,
                sequence_id=sequence_id,
                prior_execution_time=prior_execution_time,
                current_execution_time=current_execution_time,
                temporal_continuity_ok=True,
                continuation_disposition="continue_authorized_transition",
            )

        return _frame_result(
            ok=False,
            reason="unauthorized_frame_transition",
            continuity_mode="VIOLATION",
            current_invariant_frame_hash=current_invariant_frame_hash,
            prior_invariant_frame_hash=prior_invariant_frame_hash,
            transition_authorized=False,
            sequence_id=sequence_id,
            prior_execution_time=prior_execution_time,
            current_execution_time=current_execution_time,
            temporal_continuity_ok=True,
            continuation_disposition="refuse_frame_mismatch",
        )

    return _frame_result(
        ok=False,
        reason="frame_mismatch",
        continuity_mode="VIOLATION",
        current_invariant_frame_hash=current_invariant_frame_hash,
        prior_invariant_frame_hash=prior_invariant_frame_hash,
        transition_authorized=False,
        sequence_id=sequence_id,
        prior_execution_time=prior_execution_time,
        current_execution_time=current_execution_time,
        temporal_continuity_ok=True,
        continuation_disposition="refuse_frame_mismatch",
    )