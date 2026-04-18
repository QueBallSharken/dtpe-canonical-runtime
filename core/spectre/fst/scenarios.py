from __future__ import annotations

from typing import Any, Dict, Tuple


_FIRST_TARGET_SCENARIO_ID = "fst_first_target_scenario_001"
_SECOND_TARGET_SCENARIO_ID = "fst_first_target_scenario_002"
_FIRST_TARGET_STRESS_CATEGORY = "boundary_continuity_stress"

_FIRST_TARGET_SCENARIO: Dict[str, Any] = {
    "stress_scenario_id": _FIRST_TARGET_SCENARIO_ID,
    "scenario_name": "Boundary continuity claim with incomplete system-wide refusal continuity evidence",
    "stress_category": _FIRST_TARGET_STRESS_CATEGORY,
    "local_refusal_boundary_live": True,
    "system_wide_refusal_continuity_proven": False,
    "stronger_continuity_claim_asserted": False,
}

_SECOND_TARGET_SCENARIO: Dict[str, Any] = {
    "stress_scenario_id": _SECOND_TARGET_SCENARIO_ID,
    "scenario_name": "Boundary continuity claim with materially conflicting stronger continuity assertion",
    "stress_category": _FIRST_TARGET_STRESS_CATEGORY,
    "local_refusal_boundary_live": True,
    "system_wide_refusal_continuity_proven": False,
    "stronger_continuity_claim_asserted": True,
}

_SCENARIO_REGISTRY: Dict[Tuple[str, str], Dict[str, Any]] = {
    (_FIRST_TARGET_SCENARIO_ID, _FIRST_TARGET_STRESS_CATEGORY): _FIRST_TARGET_SCENARIO,
    (_SECOND_TARGET_SCENARIO_ID, _FIRST_TARGET_STRESS_CATEGORY): _SECOND_TARGET_SCENARIO,
}


def resolve_scenario(
    scenario_id: str,
    stress_category: str,
) -> Dict[str, Any]:
    key = (scenario_id, stress_category)
    if key not in _SCENARIO_REGISTRY:
        raise ValueError(f"unknown scenario/category pair: {scenario_id} / {stress_category}")
    return dict(_SCENARIO_REGISTRY[key])


def get_first_target_scenario_id() -> str:
    return _FIRST_TARGET_SCENARIO_ID


def get_second_target_scenario_id() -> str:
    return _SECOND_TARGET_SCENARIO_ID


def get_first_target_stress_category() -> str:
    return _FIRST_TARGET_STRESS_CATEGORY