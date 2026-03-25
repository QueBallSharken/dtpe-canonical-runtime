from __future__ import annotations

from typing import Any, Dict, List

from core.spectre.frame_continuity import evaluate_frame_continuity
from core.spectre.state_guard import evaluate_state_admissibility
from core.spectre.stability_guard import evaluate_system_stability
from core.spectre.temporal_guard import evaluate_temporal_invariant


def evaluate_execution_boundary(
    authority_result: Dict[str, Any],
    canonical_current_state: Dict[str, Any],
    system_state: Dict[str, Any],
    canonical_transition: Dict[str, Any],
    canonical_policy_state_hash: str,
    execution_intent: str,
    authority_hash: str,
    crypto_profile: str,
    execution_time: str,
    constraint_profile: str,
    temporal_rule_profile: str,
    prior_invariant_frame_hash: str | None,
    prior_execution_time: str | None,
    continuity_required: bool,
    transition_mode: str = "DISABLED",
    allowed_frame_transitions: List[Dict[str, str]] | None = None,
) -> Dict[str, Any]:
    """
    Phase-7 deterministic boundary control.

    ALLOW only if:
    - authority is valid
    - state is admissible
    - system remains stable
    - temporal invariant holds
    - frame continuity holds
    - temporal continuity across linked decisions holds
    """

    authority_ok = bool(authority_result.get("ok", False))

    state_result = evaluate_state_admissibility(
        canonical_current_state=canonical_current_state,
        canonical_transition=canonical_transition,
        canonical_policy_state_hash=canonical_policy_state_hash,
        execution_intent=execution_intent,
        authority_hash=authority_hash,
        crypto_profile=crypto_profile,
    )

    stability_result = evaluate_system_stability(
        system_state=system_state,
        proposed_transition=canonical_transition,
    )

    temporal_result = evaluate_temporal_invariant(
        canonical_transition=canonical_transition,
        execution_time=execution_time,
    )

    frame_continuity_result = evaluate_frame_continuity(
        policy_hash=canonical_policy_state_hash,
        authority_hash=authority_hash,
        execution_intent=execution_intent,
        constraint_profile=constraint_profile,
        temporal_rule_profile=temporal_rule_profile,
        current_execution_time=execution_time,
        prior_invariant_frame_hash=prior_invariant_frame_hash,
        prior_execution_time=prior_execution_time,
        continuity_required=continuity_required,
        transition_mode=transition_mode,
        allowed_frame_transitions=allowed_frame_transitions,
    )

    state_ok = bool(state_result.get("ok", False))
    stability_ok = bool(stability_result.get("ok", False))
    temporal_ok = bool(temporal_result.get("ok", False))
    frame_continuity_ok = frame_continuity_result.get("continuity_mode") in {
        "INITIAL",
        "EXACT",
        "AUTHORIZED_TRANSITION",
    }
    temporal_continuity_ok = bool(frame_continuity_result.get("temporal_continuity_ok", False))

    allowed = (
        authority_ok
        and state_ok
        and stability_ok
        and temporal_ok
        and frame_continuity_ok
        and temporal_continuity_ok
    )

    return {
        "ok": allowed,
        "execution_state": "ALLOW" if allowed else "REFUSED_NON_BINDING",
        "authority_result": authority_result,
        "state_admissibility_result": state_result,
        "stability_result": stability_result,
        "temporal_invariant_result": temporal_result,
        "frame_continuity_result": frame_continuity_result,
        "invariant_frame_hash": frame_continuity_result.get("current_invariant_frame_hash"),
        "prior_invariant_frame_hash": prior_invariant_frame_hash,
        "sequence_id": frame_continuity_result.get("sequence_id"),
        "continuity_required": continuity_required,
        "signal_profile": {
            "state_admissibility": {
                "ok": bool(state_result.get("ok", False)),
                "reason": state_result.get("reason"),
            },
            "system_stability": {
                "ok": bool(stability_result.get("ok", False)),
                "reason": stability_result.get("reason"),
            },
            "temporal_invariant": {
                "ok": bool(temporal_result.get("ok", False)),
                "reason": temporal_result.get("reason"),
            },
            "frame_continuity": {
                "ok": bool(frame_continuity_result.get("ok", False)),
                "reason": frame_continuity_result.get("reason"),
                "continuity_mode": frame_continuity_result.get("continuity_mode"),
                "temporal_continuity_ok": bool(frame_continuity_result.get("temporal_continuity_ok", False)),
            },
            "signal_profile_version": "v1",
        },
        "decision_space": {
            "policy_hash": canonical_policy_state_hash,
            "authority_hash": authority_hash,
            "execution_intent": execution_intent,
            "constraint_profile": constraint_profile,
            "signal_profile": {
                "state_admissibility": {
                    "ok": bool(state_result.get("ok", False)),
                    "reason": state_result.get("reason"),
                },
                "system_stability": {
                    "ok": bool(stability_result.get("ok", False)),
                    "reason": stability_result.get("reason"),
                },
                "temporal_invariant": {
                    "ok": bool(temporal_result.get("ok", False)),
                    "reason": temporal_result.get("reason"),
                },
                "frame_continuity": {
                    "ok": bool(frame_continuity_result.get("ok", False)),
                    "reason": frame_continuity_result.get("reason"),
                    "continuity_mode": frame_continuity_result.get("continuity_mode"),
                    "temporal_continuity_ok": bool(frame_continuity_result.get("temporal_continuity_ok", False)),
                },
                "signal_profile_version": "v1",
            },
            "decision_space_version": "v1",
        },
        "reason": "BOUNDARY_ALLOW" if allowed else "BOUNDARY_REFUSED_NON_BINDING",
    }




