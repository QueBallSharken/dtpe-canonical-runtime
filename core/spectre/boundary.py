from __future__ import annotations

from typing import Any, Dict

from core.spectre.state_guard import evaluate_state_admissibility
from core.spectre.stability_guard import evaluate_system_stability


def evaluate_execution_boundary(
    authority_result: Dict[str, Any],
    current_state: Dict[str, Any],
    system_state: Dict[str, Any],
    proposed_transition: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Phase-5 scaffold for deterministic boundary control.

    ALLOW only if:
    - authority is valid
    - state is admissible
    - system remains stable
    """

    authority_ok = bool(authority_result.get("ok", False))

    state_result = evaluate_state_admissibility(
        current_state=current_state,
        proposed_transition=proposed_transition,
    )

    stability_result = evaluate_system_stability(
        system_state=system_state,
        proposed_transition=proposed_transition,
    )

    state_ok = bool(state_result.get("ok", False))
    stability_ok = bool(stability_result.get("ok", False))

    allowed = authority_ok and state_ok and stability_ok

    return {
        "ok": allowed,
        "execution_state": "ALLOW" if allowed else "REFUSED_NON_BINDING",
        "authority_result": authority_result,
        "state_admissibility_result": state_result,
        "stability_result": stability_result,
        "reason": "BOUNDARY_ALLOW" if allowed else "BOUNDARY_REFUSED_NON_BINDING",
    }
