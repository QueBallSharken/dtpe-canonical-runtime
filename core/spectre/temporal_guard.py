from __future__ import annotations

from typing import Any, Dict


def evaluate_temporal_invariants(
    canonical_transition: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Phase-6 deterministic temporal invariant validation.
    """

    if canonical_transition is None:
        return {"ok": False, "reason": "MISSING_CANONICAL_TRANSITION"}

    if not isinstance(canonical_transition, dict):
        return {"ok": False, "reason": "INVALID_CANONICAL_TRANSITION"}

    if not canonical_transition:
        return {"ok": False, "reason": "EMPTY_CANONICAL_TRANSITION"}

    expires_at = canonical_transition.get("expires_at")
    if not isinstance(expires_at, str):
        return {"ok": False, "reason": "MISSING_TRANSITION_EXPIRY"}

    if not expires_at.strip():
        return {"ok": False, "reason": "MISSING_TRANSITION_EXPIRY"}

    return {
        "ok": True,
        "reason": "TEMPORAL_INVARIANTS_SATISFIED",
        "canonical_transition": canonical_transition,
    }
