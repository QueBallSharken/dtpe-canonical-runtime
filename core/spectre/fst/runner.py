from __future__ import annotations

from typing import Any, Dict, List

from .evaluator import evaluate_first_target
from .scenarios import (
    get_first_target_scenario_ids,
    get_first_target_stress_category,
)


def run_first_target_suite(
    rule_profile_id: str,
) -> Dict[str, Any]:
    stress_category = get_first_target_stress_category()
    scenario_ids = get_first_target_scenario_ids()

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

    aggregate = {
        "fst_suite_id": "spectre_fst_first_target_suite_v1",
        "fst_suite_version": "1.0",
        "fst_rule_profile_id": rule_profile_id,
        "stress_category": stress_category,
        "scenario_ids": scenario_ids,
        "receipts": receipts,
        "results_by_scenario_id": results_by_scenario_id,
    }

    return aggregate