from __future__ import annotations

from typing import Any, Dict, List

from .evaluator import evaluate_first_target
from .scenarios import (
    get_all_supported_stress_categories,
    get_first_target_scenario_ids,
    get_first_target_stress_category,
    get_second_category_scenario_ids,
    get_second_category_stress_category,
    get_third_category_scenario_ids,
    get_third_category_stress_category,
    get_fourth_category_scenario_ids,
    get_fourth_category_stress_category,
    get_fifth_category_scenario_ids,
    get_fifth_category_stress_category,
    get_sixth_category_scenario_ids,
    get_sixth_category_stress_category,
)


def _run_suite_for_category(
    rule_profile_id: str,
    stress_category: str,
    scenario_ids: List[str],
    suite_id: str,
) -> Dict[str, Any]:
    receipts: List[Dict[str, Any]] = []
    results_by_scenario_id: Dict[str, str] = {}

    for scenario_id in scenario_ids:
        receipt = evaluate_first_target(
            scenario_id=scenario_id,
            stress_category=stress_category,
            rule_profile_id=rule_profile_id,
        )
        receipts.append(receipt)
        results_by_scenario_id[scenario_id] = receipt["fst_result"]

    return {
        "fst_suite_id": suite_id,
        "fst_suite_version": "1.0",
        "fst_rule_profile_id": rule_profile_id,
        "stress_category": stress_category,
        "scenario_ids": scenario_ids,
        "receipts": receipts,
        "results_by_scenario_id": results_by_scenario_id,
    }


def run_first_target_suite(
    rule_profile_id: str,
) -> Dict[str, Any]:
    return _run_suite_for_category(
        rule_profile_id=rule_profile_id,
        stress_category=get_first_target_stress_category(),
        scenario_ids=get_first_target_scenario_ids(),
        suite_id="spectre_fst_first_target_suite_v1",
    )


def run_second_category_suite(
    rule_profile_id: str,
) -> Dict[str, Any]:
    return _run_suite_for_category(
        rule_profile_id=rule_profile_id,
        stress_category=get_second_category_stress_category(),
        scenario_ids=get_second_category_scenario_ids(),
        suite_id="spectre_fst_second_category_suite_v1",
    )


def run_third_category_suite(
    rule_profile_id: str,
) -> Dict[str, Any]:
    return _run_suite_for_category(
        rule_profile_id=rule_profile_id,
        stress_category=get_third_category_stress_category(),
        scenario_ids=get_third_category_scenario_ids(),
        suite_id="spectre_fst_third_category_suite_v1",
    )


def run_fourth_category_suite(
    rule_profile_id: str,
) -> Dict[str, Any]:
    return _run_suite_for_category(
        rule_profile_id=rule_profile_id,
        stress_category=get_fourth_category_stress_category(),
        scenario_ids=get_fourth_category_scenario_ids(),
        suite_id="spectre_fst_fourth_category_suite_v1",
    )


def run_fifth_category_suite(
    rule_profile_id: str,
) -> Dict[str, Any]:
    return _run_suite_for_category(
        rule_profile_id=rule_profile_id,
        stress_category=get_fifth_category_stress_category(),
        scenario_ids=get_fifth_category_scenario_ids(),
        suite_id="spectre_fst_fifth_category_suite_v1",
    )


def run_sixth_category_suite(
    rule_profile_id: str,
) -> Dict[str, Any]:
    return _run_suite_for_category(
        rule_profile_id=rule_profile_id,
        stress_category=get_sixth_category_stress_category(),
        scenario_ids=get_sixth_category_scenario_ids(),
        suite_id="spectre_fst_sixth_category_suite_v1",
    )


def run_all_known_suites(
    rule_profile_id: str,
) -> Dict[str, Any]:
    first_suite = run_first_target_suite(rule_profile_id=rule_profile_id)
    second_suite = run_second_category_suite(rule_profile_id=rule_profile_id)
    third_suite = run_third_category_suite(rule_profile_id=rule_profile_id)
    fourth_suite = run_fourth_category_suite(rule_profile_id=rule_profile_id)
    fifth_suite = run_fifth_category_suite(rule_profile_id=rule_profile_id)
    sixth_suite = run_sixth_category_suite(rule_profile_id=rule_profile_id)

    suites_by_category = {
        first_suite["stress_category"]: first_suite,
        second_suite["stress_category"]: second_suite,
        third_suite["stress_category"]: third_suite,
        fourth_suite["stress_category"]: fourth_suite,
        fifth_suite["stress_category"]: fifth_suite,
        sixth_suite["stress_category"]: sixth_suite,
    }

    return {
        "fst_aggregate_id": "spectre_fst_multi_category_suite_v1",
        "fst_aggregate_version": "1.0",
        "fst_rule_profile_id": rule_profile_id,
        "stress_categories": get_all_supported_stress_categories(),
        "suites_by_category": suites_by_category,
    }