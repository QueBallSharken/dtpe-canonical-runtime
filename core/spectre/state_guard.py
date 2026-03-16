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

    if not isinstance(canonical_current_state, dict):
        return {"ok": False, "reason": "INVALID_CANONICAL_CURRENT_STATE"}

    if not canonical_current_state:
        return {"ok": False, "reason": "EMPTY_CANONICAL_CURRENT_STATE"}

    if canonical_transition is None:
        return {"ok": False, "reason": "MISSING_CANONICAL_TRANSITION"}

    if not isinstance(canonical_transition, dict):
        return {"ok": False, "reason": "INVALID_CANONICAL_TRANSITION"}

    if not canonical_transition:
        return {"ok": False, "reason": "EMPTY_CANONICAL_TRANSITION"}

    if not isinstance(canonical_policy_state_hash, str) or not canonical_policy_state_hash.strip():
        return {"ok": False, "reason": "MISSING_POLICY_STATE_HASH"}

    if not isinstance(execution_intent, str) or not execution_intent.strip():
        return {"ok": False, "reason": "MISSING_EXECUTION_INTENT"}

    if not isinstance(authority_hash, str) or not authority_hash.strip():
        return {"ok": False, "reason": "MISSING_AUTHORITY_HASH"}

    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
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
