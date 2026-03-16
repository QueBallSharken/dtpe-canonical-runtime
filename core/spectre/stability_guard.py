from __future__ import annotations

from typing import Any, Dict


def evaluate_system_stability(
    system_state: Dict[str, Any],
    proposed_transition: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Phase-5 deterministic stability evaluation.
    """

    if system_state is None:
        return {"ok": False, "reason": "MISSING_SYSTEM_STATE"}

    if not isinstance(system_state, dict):
        return {"ok": False, "reason": "INVALID_SYSTEM_STATE"}

    if not system_state:
        return {"ok": False, "reason": "EMPTY_SYSTEM_STATE"}

    if proposed_transition is None:
        return {"ok": False, "reason": "MISSING_PROPOSED_TRANSITION"}

    if not isinstance(proposed_transition, dict):
        return {"ok": False, "reason": "INVALID_PROPOSED_TRANSITION"}

    if not proposed_transition:
        return {"ok": False, "reason": "EMPTY_PROPOSED_TRANSITION"}

    action = proposed_transition.get("action")
    if not isinstance(action, str) or not action.strip():
        return {"ok": False, "reason": "MISSING_TRANSITION_ACTION"}

    expires_at = proposed_transition.get("expires_at")
    if not isinstance(expires_at, str) or not expires_at.strip():
        return {"ok": False, "reason": "MISSING_TRANSITION_EXPIRY"}

    return {
        "ok": True,
        "reason": "SYSTEM_STABLE",
        "system_state": system_state,
        "proposed_transition": proposed_transition,
    }
