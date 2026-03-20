from __future__ import annotations

from typing import Any, Dict

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
) -> Dict[str, Any]:
    """
    Phase-6 deterministic boundary control.

    ALLOW only if:
    - authority is valid
    - state is admissible
    - system remains stable
    - temporal invariant holds
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

    state_ok = bool(state_result.get("ok", False))
    stability_ok = bool(stability_result.get("ok", False))
    temporal_ok = bool(temporal_result.get("ok", False))

    allowed = authority_ok and state_ok and stability_ok and temporal_ok

    return {
        "ok": allowed,
        "execution_state": "ALLOW" if allowed else "REFUSED_NON_BINDING",
        "authority_result": authority_result,
        "state_admissibility_result": state_result,
        "stability_result": stability_result,
        "temporal_invariant_result": temporal_result,
        "reason": "BOUNDARY_ALLOW" if allowed else "BOUNDARY_REFUSED_NON_BINDING",
    }
