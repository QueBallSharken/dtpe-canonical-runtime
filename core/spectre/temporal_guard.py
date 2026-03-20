from __future__ import annotations

from typing import Any, Dict


def evaluate_temporal_invariant(
    canonical_transition: Dict[str, Any],
    execution_time: str,
) -> Dict[str, Any]:
    """
    Phase-6 deterministic temporal admissibility evaluation.

    Rules locked by repo docs:
    - execution_time is a required canonical input
    - expires_at must come from canonical_transition
    - no runtime clock
    - no hidden temporal state
    - enumerated reasons only
    """

    expires_at = canonical_transition.get("expires_at") if isinstance(canonical_transition, dict) else None

    if not isinstance(execution_time, str) or not execution_time.strip():
        return {
            "ok": False,
            "reason": "MISSING_EXECUTION_TIME",
            "execution_time": execution_time,
            "expires_at": expires_at,
        }

    if not isinstance(expires_at, str) or not expires_at.strip():
        return {
            "ok": False,
            "reason": "MISSING_EXPIRES_AT",
            "execution_time": execution_time,
            "expires_at": expires_at,
        }

    ok = execution_time <= expires_at

    return {
        "ok": ok,
        "reason": "VALID" if ok else "EXPIRED",
        "execution_time": execution_time,
        "expires_at": expires_at,
    }
