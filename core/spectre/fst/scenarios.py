from __future__ import annotations

from typing import Any, Dict, List, Tuple


_FIRST_TARGET_SCENARIO_ID = "fst_first_target_scenario_001"
_SECOND_TARGET_SCENARIO_ID = "fst_first_target_scenario_002"
_THIRD_TARGET_SCENARIO_ID = "fst_first_target_scenario_003"
_FOURTH_TARGET_SCENARIO_ID = "fst_first_target_scenario_004"
_FIRST_TARGET_STRESS_CATEGORY = "boundary_continuity_stress"

_SECOND_CATEGORY_SCENARIO_ID = "fst_second_category_scenario_001"
_SECOND_CATEGORY_STRESS_CATEGORY = "authority_continuity_stress"

_THIRD_CATEGORY_SCENARIO_ID = "fst_third_category_scenario_001"
_THIRD_CATEGORY_STRESS_CATEGORY = "temporal_continuity_stress"

_FOURTH_CATEGORY_SCENARIO_ID = "fst_fourth_category_scenario_001"
_FOURTH_CATEGORY_STRESS_CATEGORY = "state_continuity_stress"

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

_THIRD_TARGET_SCENARIO: Dict[str, Any] = {
    "stress_scenario_id": _THIRD_TARGET_SCENARIO_ID,
    "scenario_name": "Boundary continuity claim without live local refusal boundary and without sufficient stronger-claim contradiction evidence",
    "stress_category": _FIRST_TARGET_STRESS_CATEGORY,
    "local_refusal_boundary_live": False,
    "system_wide_refusal_continuity_proven": False,
    "stronger_continuity_claim_asserted": False,
}

_FOURTH_TARGET_SCENARIO: Dict[str, Any] = {
    "stress_scenario_id": _FOURTH_TARGET_SCENARIO_ID,
    "scenario_name": "Boundary continuity claim with system-wide refusal continuity already proven",
    "stress_category": _FIRST_TARGET_STRESS_CATEGORY,
    "local_refusal_boundary_live": True,
    "system_wide_refusal_continuity_proven": True,
    "stronger_continuity_claim_asserted": False,
}

_SECOND_CATEGORY_SCENARIO: Dict[str, Any] = {
    "stress_scenario_id": _SECOND_CATEGORY_SCENARIO_ID,
    "scenario_name": "Authority continuity claim with conflicting stronger end-to-end authority assertion",
    "stress_category": _SECOND_CATEGORY_STRESS_CATEGORY,
    "local_authority_binding_live": True,
    "end_to_end_authority_continuity_proven": False,
    "stronger_authority_claim_asserted": True,
}

_THIRD_CATEGORY_SCENARIO: Dict[str, Any] = {
    "stress_scenario_id": _THIRD_CATEGORY_SCENARIO_ID,
    "scenario_name": "Temporal continuity claim with conflicting stronger timing/finality assertion",
    "stress_category": _THIRD_CATEGORY_STRESS_CATEGORY,
    "local_time_window_binding_live": True,
    "end_to_end_temporal_continuity_proven": False,
    "stronger_temporal_claim_asserted": True,
}

_FOURTH_CATEGORY_SCENARIO: Dict[str, Any] = {
    "stress_scenario_id": _FOURTH_CATEGORY_SCENARIO_ID,
    "scenario_name": "State continuity claim with conflicting stronger persistent-state assertion",
    "stress_category": _FOURTH_CATEGORY_STRESS_CATEGORY,
    "local_state_binding_live": True,
    "end_to_end_state_continuity_proven": False,
    "stronger_state_claim_asserted": True,
}

_SCENARIO_REGISTRY: Dict[Tuple[str, str], Dict[str, Any]] = {
    (_FIRST_TARGET_SCENARIO_ID, _FIRST_TARGET_STRESS_CATEGORY): _FIRST_TARGET_SCENARIO,
    (_SECOND_TARGET_SCENARIO_ID, _FIRST_TARGET_STRESS_CATEGORY): _SECOND_TARGET_SCENARIO,
    (_THIRD_TARGET_SCENARIO_ID, _FIRST_TARGET_STRESS_CATEGORY): _THIRD_TARGET_SCENARIO,
    (_FOURTH_TARGET_SCENARIO_ID, _FIRST_TARGET_STRESS_CATEGORY): _FOURTH_TARGET_SCENARIO,
    (_SECOND_CATEGORY_SCENARIO_ID, _SECOND_CATEGORY_STRESS_CATEGORY): _SECOND_CATEGORY_SCENARIO,
    (_THIRD_CATEGORY_SCENARIO_ID, _THIRD_CATEGORY_STRESS_CATEGORY): _THIRD_CATEGORY_SCENARIO,
    (_FOURTH_CATEGORY_SCENARIO_ID, _FOURTH_CATEGORY_STRESS_CATEGORY): _FOURTH_CATEGORY_SCENARIO,
}

_FIRST_TARGET_SCENARIO_IDS = [
    _FIRST_TARGET_SCENARIO_ID,
    _SECOND_TARGET_SCENARIO_ID,
    _THIRD_TARGET_SCENARIO_ID,
    _FOURTH_TARGET_SCENARIO_ID,
]

_SECOND_CATEGORY_SCENARIO_IDS = [
    _SECOND_CATEGORY_SCENARIO_ID,
]

_THIRD_CATEGORY_SCENARIO_IDS = [
    _THIRD_CATEGORY_SCENARIO_ID,
]

_FOURTH_CATEGORY_SCENARIO_IDS = [
    _FOURTH_CATEGORY_SCENARIO_ID,
]

_ALL_SUPPORTED_STRESS_CATEGORIES = [
    _FIRST_TARGET_STRESS_CATEGORY,
    _SECOND_CATEGORY_STRESS_CATEGORY,
    _THIRD_CATEGORY_STRESS_CATEGORY,
    _FOURTH_CATEGORY_STRESS_CATEGORY,
]


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


def get_third_target_scenario_id() -> str:
    return _THIRD_TARGET_SCENARIO_ID


def get_fourth_target_scenario_id() -> str:
    return _FOURTH_TARGET_SCENARIO_ID


def get_first_target_stress_category() -> str:
    return _FIRST_TARGET_STRESS_CATEGORY


def get_first_target_scenario_ids() -> List[str]:
    return list(_FIRST_TARGET_SCENARIO_IDS)


def get_second_category_stress_category() -> str:
    return _SECOND_CATEGORY_STRESS_CATEGORY


def get_second_category_scenario_id() -> str:
    return _SECOND_CATEGORY_SCENARIO_ID


def get_second_category_scenario_ids() -> List[str]:
    return list(_SECOND_CATEGORY_SCENARIO_IDS)


def get_third_category_stress_category() -> str:
    return _THIRD_CATEGORY_STRESS_CATEGORY


def get_third_category_scenario_id() -> str:
    return _THIRD_CATEGORY_SCENARIO_ID


def get_third_category_scenario_ids() -> List[str]:
    return list(_THIRD_CATEGORY_SCENARIO_IDS)


def get_fourth_category_stress_category() -> str:
    return _FOURTH_CATEGORY_STRESS_CATEGORY


def get_fourth_category_scenario_id() -> str:
    return _FOURTH_CATEGORY_SCENARIO_ID


def get_fourth_category_scenario_ids() -> List[str]:
    return list(_FOURTH_CATEGORY_SCENARIO_IDS)


def get_all_supported_stress_categories() -> List[str]:
    return list(_ALL_SUPPORTED_STRESS_CATEGORIES)