from __future__ import annotations

from typing import Any, Dict


def evaluate_state_admissibility(
    canonical_current_state: Dict[str, Any],
    canonical_transition: Dict[str, Any],
    canonical_policy_state_hash: str,
    execution_intent: str,
    authority_hash: str,
    crypto_profile: str,
) -> Dict[str, Any]:
    """
    Phase-5 deterministic admissibility validation.
    """

    if canonical_current_state is None:
        return {"ok": False, "reason": "MISSING_CANONICAL_CURRENT_STATE"}

    if canonical_transition is None:
        return {"ok": False, "reason": "MISSING_CANONICAL_TRANSITION"}

    if not canonical_policy_state_hash:
        return {"ok": False, "reason": "MISSING_POLICY_STATE_HASH"}

    if not execution_intent:
        return {"ok": False, "reason": "MISSING_EXECUTION_INTENT"}

    if not authority_hash:
        return {"ok": False, "reason": "MISSING_AUTHORITY_HASH"}

    if not crypto_profile:
        return {"ok": False, "reason": "MISSING_CRYPTO_PROFILE"}

    return {
        "ok": True,
        "reason": "STATE_ADMISSIBLE",
        "canonical_current_state": canonical_current_state,
        "canonical_transition": canonical_transition,
        "canonical_policy_state_hash": canonical_policy_state_hash,
        "execution_intent": execution_intent,
        "authority_hash": authority_hash,
        "crypto_profile": crypto_profile,
    }
