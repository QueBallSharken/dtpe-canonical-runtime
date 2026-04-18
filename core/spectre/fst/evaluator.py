from __future__ import annotations

from typing import Any, Dict

from .receipt_schema import validate_minimal_receipt
from .result_vocabulary import is_valid_primary_result
from .rule_profiles import get_first_target_rule_profile
from .scenarios import (
    get_first_target_scenario_id,
    get_first_target_stress_category,
    get_second_target_scenario_id,
    resolve_scenario,
)


_FST_PROFILE_ID = "spectre_fst_minimal_v1"
_FST_PROFILE_VERSION = "1.0"


def evaluate_first_target(
    scenario_id: str,
    stress_category: str,
    rule_profile_id: str,
) -> Dict[str, Any]:
    rule_profile = get_first_target_rule_profile()

    if rule_profile_id != rule_profile["fst_rule_profile_id"]:
        raise ValueError(f"unsupported rule_profile_id: {rule_profile_id}")

    allowed_stress_categories = rule_profile["allowed_stress_categories"]
    if stress_category not in allowed_stress_categories:
        raise ValueError(f"stress_category not allowed by rule profile: {stress_category}")

    allowed_scenario_ids = {
        get_first_target_scenario_id(),
        get_second_target_scenario_id(),
    }
    if scenario_id not in allowed_scenario_ids:
        raise ValueError(f"unsupported scenario_id: {scenario_id}")

    expected_stress_category = get_first_target_stress_category()
    if stress_category != expected_stress_category:
        raise ValueError(f"unsupported stress_category: {stress_category}")

    scenario = resolve_scenario(
        scenario_id=scenario_id,
        stress_category=stress_category,
    )

    local_refusal_boundary_live = bool(scenario["local_refusal_boundary_live"])
    system_wide_refusal_continuity_proven = bool(
        scenario["system_wide_refusal_continuity_proven"]
    )
    stronger_continuity_claim_asserted = bool(
        scenario["stronger_continuity_claim_asserted"]
    )

    findings = []
    gaps = []
    contradictions = []

    if local_refusal_boundary_live:
        findings.append("local refusal boundary remained live")

    if not system_wide_refusal_continuity_proven:
        gaps.append("system-wide refusal continuity not proven under in-flight authority change")

    if stronger_continuity_claim_asserted and not system_wide_refusal_continuity_proven:
        contradictions.append("stronger continuity claim exceeded what the evidenced path supports")
        fst_result = "CONTRADICTION_EXPOSED"
    elif local_refusal_boundary_live and not system_wide_refusal_continuity_proven:
        fst_result = "PARTIAL"
    else:
        fst_result = "UNVERIFIABLE"

    if not is_valid_primary_result(fst_result):
        raise ValueError(f"invalid fst_result: {fst_result}")

    allowed_primary_results = rule_profile["allowed_primary_results"]
    if fst_result not in allowed_primary_results:
        raise ValueError(f"fst_result not allowed by rule profile: {fst_result}")

    receipt = {
        "fst_profile_id": _FST_PROFILE_ID,
        "fst_profile_version": _FST_PROFILE_VERSION,
        "fst_rule_profile_id": rule_profile["fst_rule_profile_id"],
        "stress_scenario_id": scenario["stress_scenario_id"],
        "stress_category": scenario["stress_category"],
        "fst_result": fst_result,
        "fst_findings": findings,
        "fst_gaps": gaps,
        "fst_contradictions": contradictions,
    }

    validate_minimal_receipt(receipt)
    return receipt