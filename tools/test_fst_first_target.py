from core.canonical import canonical_json
from core.hashing import sha256_hex_str
from core.spectre.fst.evaluator import evaluate_first_target
from core.spectre.fst.receipt_schema import (
    get_minimal_receipt_canonical,
    get_minimal_receipt_hash,
)
from core.spectre.fst.rule_profiles import (
    get_first_target_rule_profile,
    get_first_target_rule_profile_hash,
)
from core.spectre.fst.runner import (
    run_all_known_suites,
    run_first_target_suite,
    run_second_category_suite,
    run_third_category_suite,
    run_fourth_category_suite,
)
from core.spectre.fst.scenarios import (
    get_all_supported_stress_categories,
    get_first_target_scenario_ids,
    get_second_category_scenario_ids,
    get_third_category_scenario_ids,
    get_fourth_category_scenario_ids,
)


def _assert_minimal_receipt_shape(receipt):
    expected_fields = {
        "fst_profile_id",
        "fst_profile_version",
        "fst_rule_profile_id",
        "stress_scenario_id",
        "stress_category",
        "fst_result",
        "fst_findings",
        "fst_gaps",
        "fst_contradictions",
    }

    assert set(receipt.keys()) == expected_fields
    assert isinstance(receipt["fst_findings"], list)
    assert isinstance(receipt["fst_gaps"], list)
    assert isinstance(receipt["fst_contradictions"], list)


def _assert_raises_value_error(fn, expected_message_fragment: str) -> None:
    try:
        fn()
    except ValueError as exc:
        if expected_message_fragment not in str(exc):
            raise AssertionError(
                f"expected ValueError containing {expected_message_fragment!r}, got {str(exc)!r}"
            ) from exc
        return

    raise AssertionError("expected ValueError but no exception was raised")


def main() -> int:
    receipt_one = evaluate_first_target(
        scenario_id="fst_first_target_scenario_001",
        stress_category="boundary_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_two = evaluate_first_target(
        scenario_id="fst_first_target_scenario_002",
        stress_category="boundary_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_three = evaluate_first_target(
        scenario_id="fst_first_target_scenario_003",
        stress_category="boundary_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_four = evaluate_first_target(
        scenario_id="fst_first_target_scenario_004",
        stress_category="boundary_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_five = evaluate_first_target(
        scenario_id="fst_second_category_scenario_001",
        stress_category="authority_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_six = evaluate_first_target(
        scenario_id="fst_third_category_scenario_001",
        stress_category="temporal_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_seven = evaluate_first_target(
        scenario_id="fst_fourth_category_scenario_001",
        stress_category="state_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    _assert_minimal_receipt_shape(receipt_one)
    _assert_minimal_receipt_shape(receipt_two)
    _assert_minimal_receipt_shape(receipt_three)
    _assert_minimal_receipt_shape(receipt_four)
    _assert_minimal_receipt_shape(receipt_five)
    _assert_minimal_receipt_shape(receipt_six)
    _assert_minimal_receipt_shape(receipt_seven)

    assert receipt_one["stress_scenario_id"] == "fst_first_target_scenario_001"
    assert receipt_one["fst_result"] == "PARTIAL"
    assert receipt_one["fst_findings"] == [
        "local refusal boundary remained live"
    ]
    assert receipt_one["fst_gaps"] == [
        "system-wide refusal continuity not proven under in-flight authority change"
    ]
    assert receipt_one["fst_contradictions"] == []

    assert receipt_two["stress_scenario_id"] == "fst_first_target_scenario_002"
    assert receipt_two["fst_result"] == "CONTRADICTION_EXPOSED"
    assert receipt_two["fst_findings"] == [
        "local refusal boundary remained live"
    ]
    assert receipt_two["fst_gaps"] == [
        "system-wide refusal continuity not proven under in-flight authority change"
    ]
    assert receipt_two["fst_contradictions"] == [
        "stronger continuity claim exceeded what the evidenced path supports"
    ]

    assert receipt_three["stress_scenario_id"] == "fst_first_target_scenario_003"
    assert receipt_three["fst_result"] == "UNVERIFIABLE"
    assert receipt_three["fst_findings"] == []
    assert receipt_three["fst_gaps"] == [
        "system-wide refusal continuity not proven under in-flight authority change"
    ]
    assert receipt_three["fst_contradictions"] == []

    assert receipt_four["stress_scenario_id"] == "fst_first_target_scenario_004"
    assert receipt_four["fst_result"] == "UNVERIFIABLE"
    assert receipt_four["fst_findings"] == [
        "local refusal boundary remained live"
    ]
    assert receipt_four["fst_gaps"] == []
    assert receipt_four["fst_contradictions"] == []

    assert receipt_five["stress_scenario_id"] == "fst_second_category_scenario_001"
    assert receipt_five["stress_category"] == "authority_continuity_stress"
    assert receipt_five["fst_result"] == "CONTRADICTION_EXPOSED"
    assert receipt_five["fst_findings"] == [
        "local authority binding remained live"
    ]
    assert receipt_five["fst_gaps"] == [
        "end-to-end authority continuity not proven across delegated mutation path"
    ]
    assert receipt_five["fst_contradictions"] == [
        "stronger authority continuity claim exceeded what the evidenced path supports"
    ]

    assert receipt_six["stress_scenario_id"] == "fst_third_category_scenario_001"
    assert receipt_six["stress_category"] == "temporal_continuity_stress"
    assert receipt_six["fst_result"] == "CONTRADICTION_EXPOSED"
    assert receipt_six["fst_findings"] == [
        "local temporal binding remained live"
    ]
    assert receipt_six["fst_gaps"] == [
        "end-to-end temporal continuity not proven across delayed execution path"
    ]
    assert receipt_six["fst_contradictions"] == [
        "stronger temporal continuity claim exceeded what the evidenced path supports"
    ]

    assert receipt_seven["stress_scenario_id"] == "fst_fourth_category_scenario_001"
    assert receipt_seven["stress_category"] == "state_continuity_stress"
    assert receipt_seven["fst_result"] == "CONTRADICTION_EXPOSED"
    assert receipt_seven["fst_findings"] == [
        "local state binding remained live"
    ]
    assert receipt_seven["fst_gaps"] == [
        "end-to-end state continuity not proven across persisted mutation path"
    ]
    assert receipt_seven["fst_contradictions"] == [
        "stronger state continuity claim exceeded what the evidenced path supports"
    ]

    first_category_scenario_ids = get_first_target_scenario_ids()
    assert first_category_scenario_ids == [
        "fst_first_target_scenario_001",
        "fst_first_target_scenario_002",
        "fst_first_target_scenario_003",
        "fst_first_target_scenario_004",
    ]

    second_category_scenario_ids = get_second_category_scenario_ids()
    assert second_category_scenario_ids == [
        "fst_second_category_scenario_001",
    ]

    third_category_scenario_ids = get_third_category_scenario_ids()
    assert third_category_scenario_ids == [
        "fst_third_category_scenario_001",
    ]

    fourth_category_scenario_ids = get_fourth_category_scenario_ids()
    assert fourth_category_scenario_ids == [
        "fst_fourth_category_scenario_001",
    ]

    assert get_all_supported_stress_categories() == [
        "boundary_continuity_stress",
        "authority_continuity_stress",
        "temporal_continuity_stress",
        "state_continuity_stress",
    ]

    rule_profile = get_first_target_rule_profile()
    expected_rule_profile_hash = sha256_hex_str(canonical_json(rule_profile))
    assert get_first_target_rule_profile_hash() == expected_rule_profile_hash

    assert get_minimal_receipt_canonical(receipt_one) == canonical_json(receipt_one)
    assert get_minimal_receipt_hash(receipt_one) == sha256_hex_str(canonical_json(receipt_one))

    first_suite = run_first_target_suite(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )
    assert first_suite["fst_suite_id"] == "spectre_fst_first_target_suite_v1"
    assert first_suite["stress_category"] == "boundary_continuity_stress"
    assert first_suite["scenario_ids"] == first_category_scenario_ids
    assert len(first_suite["receipts"]) == 4
    assert first_suite["results_by_scenario_id"] == {
        "fst_first_target_scenario_001": "PARTIAL",
        "fst_first_target_scenario_002": "CONTRADICTION_EXPOSED",
        "fst_first_target_scenario_003": "UNVERIFIABLE",
        "fst_first_target_scenario_004": "UNVERIFIABLE",
    }

    second_suite = run_second_category_suite(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )
    assert second_suite["fst_suite_id"] == "spectre_fst_second_category_suite_v1"
    assert second_suite["stress_category"] == "authority_continuity_stress"
    assert second_suite["scenario_ids"] == second_category_scenario_ids
    assert len(second_suite["receipts"]) == 1
    assert second_suite["results_by_scenario_id"] == {
        "fst_second_category_scenario_001": "CONTRADICTION_EXPOSED",
    }

    third_suite = run_third_category_suite(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )
    assert third_suite["fst_suite_id"] == "spectre_fst_third_category_suite_v1"
    assert third_suite["stress_category"] == "temporal_continuity_stress"
    assert third_suite["scenario_ids"] == third_category_scenario_ids
    assert len(third_suite["receipts"]) == 1
    assert third_suite["results_by_scenario_id"] == {
        "fst_third_category_scenario_001": "CONTRADICTION_EXPOSED",
    }

    fourth_suite = run_fourth_category_suite(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )
    assert fourth_suite["fst_suite_id"] == "spectre_fst_fourth_category_suite_v1"
    assert fourth_suite["stress_category"] == "state_continuity_stress"
    assert fourth_suite["scenario_ids"] == fourth_category_scenario_ids
    assert len(fourth_suite["receipts"]) == 1
    assert fourth_suite["results_by_scenario_id"] == {
        "fst_fourth_category_scenario_001": "CONTRADICTION_EXPOSED",
    }

    aggregate = run_all_known_suites(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )
    assert aggregate["fst_aggregate_id"] == "spectre_fst_multi_category_suite_v1"
    assert aggregate["fst_aggregate_version"] == "1.0"
    assert aggregate["fst_rule_profile_id"] == "spectre_fst_first_target_rules_v1"
    assert aggregate["stress_categories"] == [
        "boundary_continuity_stress",
        "authority_continuity_stress",
        "temporal_continuity_stress",
        "state_continuity_stress",
    ]
    assert set(aggregate["suites_by_category"].keys()) == {
        "boundary_continuity_stress",
        "authority_continuity_stress",
        "temporal_continuity_stress",
        "state_continuity_stress",
    }

    _assert_raises_value_error(
        lambda: evaluate_first_target(
            scenario_id="fst_first_target_scenario_001",
            stress_category="boundary_continuity_stress",
            rule_profile_id="wrong_rule_profile",
        ),
        "unsupported rule_profile_id",
    )

    _assert_raises_value_error(
        lambda: evaluate_first_target(
            scenario_id="wrong_scenario",
            stress_category="boundary_continuity_stress",
            rule_profile_id="spectre_fst_first_target_rules_v1",
        ),
        "unsupported scenario_id",
    )

    _assert_raises_value_error(
        lambda: evaluate_first_target(
            scenario_id="fst_first_target_scenario_001",
            stress_category="wrong_stress_category",
            rule_profile_id="spectre_fst_first_target_rules_v1",
        ),
        "stress_category not allowed by rule profile",
    )

    print("PASS: fst four-category aggregate suite verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())