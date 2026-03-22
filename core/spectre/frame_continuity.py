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
        return {
            "ok": True,
            "reason": "initial_frame",
            "continuity_mode": "INITIAL",
            "current_invariant_frame_hash": current_invariant_frame_hash,
            "prior_invariant_frame_hash": None,
            "transition_authorized": False,
            "sequence_id": sequence_id,
            "prior_execution_time": None,
            "current_execution_time": current_execution_time,
            "temporal_continuity_ok": True,
        }

    if continuity_required and (not isinstance(prior_invariant_frame_hash, str) or not prior_invariant_frame_hash.strip()):
        return {
            "ok": False,
            "reason": "missing_prior_frame_hash",
            "continuity_mode": "VIOLATION",
            "current_invariant_frame_hash": current_invariant_frame_hash,
            "prior_invariant_frame_hash": prior_invariant_frame_hash,
            "transition_authorized": False,
            "sequence_id": sequence_id,
            "prior_execution_time": prior_execution_time,
            "current_execution_time": current_execution_time,
            "temporal_continuity_ok": False,
        }

    if continuity_required and (not isinstance(prior_execution_time, str) or not prior_execution_time.strip()):
        return {
            "ok": False,
            "reason": "missing_prior_execution_time",
            "continuity_mode": "VIOLATION",
            "current_invariant_frame_hash": current_invariant_frame_hash,
            "prior_invariant_frame_hash": prior_invariant_frame_hash,
            "transition_authorized": False,
            "sequence_id": sequence_id,
            "prior_execution_time": prior_execution_time,
            "current_execution_time": current_execution_time,
            "temporal_continuity_ok": False,
        }

    temporal_continuity_ok = True
    if isinstance(prior_execution_time, str) and prior_execution_time.strip():
        temporal_continuity_ok = current_execution_time >= prior_execution_time

    if not temporal_continuity_ok:
        return {
            "ok": False,
            "reason": "temporal_order_violation",
            "continuity_mode": "VIOLATION",
            "current_invariant_frame_hash": current_invariant_frame_hash,
            "prior_invariant_frame_hash": prior_invariant_frame_hash,
            "transition_authorized": False,
            "sequence_id": sequence_id,
            "prior_execution_time": prior_execution_time,
            "current_execution_time": current_execution_time,
            "temporal_continuity_ok": False,
        }

    if current_invariant_frame_hash == prior_invariant_frame_hash:
        return {
            "ok": True,
            "reason": "frame_continuity_ok",
            "continuity_mode": "EXACT",
            "current_invariant_frame_hash": current_invariant_frame_hash,
            "prior_invariant_frame_hash": prior_invariant_frame_hash,
            "transition_authorized": False,
            "sequence_id": sequence_id,
            "prior_execution_time": prior_execution_time,
            "current_execution_time": current_execution_time,
            "temporal_continuity_ok": True,
        }

    if transition_mode == "EXPLICIT_MAP":
        allowed_frame_transitions = allowed_frame_transitions or []
        transition_authorized = any(
            item.get("from") == prior_invariant_frame_hash
            and item.get("to") == current_invariant_frame_hash
            for item in allowed_frame_transitions
        )
        if transition_authorized:
            return {
                "ok": True,
                "reason": "authorized_frame_transition",
                "continuity_mode": "AUTHORIZED_TRANSITION",
                "current_invariant_frame_hash": current_invariant_frame_hash,
                "prior_invariant_frame_hash": prior_invariant_frame_hash,
                "transition_authorized": True,
                "sequence_id": sequence_id,
                "prior_execution_time": prior_execution_time,
                "current_execution_time": current_execution_time,
                "temporal_continuity_ok": True,
            }

        return {
            "ok": False,
            "reason": "unauthorized_frame_transition",
            "continuity_mode": "VIOLATION",
            "current_invariant_frame_hash": current_invariant_frame_hash,
            "prior_invariant_frame_hash": prior_invariant_frame_hash,
            "transition_authorized": False,
            "sequence_id": sequence_id,
            "prior_execution_time": prior_execution_time,
            "current_execution_time": current_execution_time,
            "temporal_continuity_ok": True,
        }

    return {
        "ok": False,
        "reason": "frame_mismatch",
        "continuity_mode": "VIOLATION",
        "current_invariant_frame_hash": current_invariant_frame_hash,
        "prior_invariant_frame_hash": prior_invariant_frame_hash,
        "transition_authorized": False,
        "sequence_id": sequence_id,
        "prior_execution_time": prior_execution_time,
        "current_execution_time": current_execution_time,
        "temporal_continuity_ok": True,
    }
