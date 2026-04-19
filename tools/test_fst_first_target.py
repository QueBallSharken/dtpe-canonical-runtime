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
    run_fifth_category_suite,
    run_sixth_category_suite,
)
from core.spectre.fst.scenarios import (
    get_all_supported_stress_categories,
    get_first_target_scenario_ids,
    get_second_category_scenario_ids,
    get_third_category_scenario_ids,
    get_fourth_category_scenario_ids,
    get_fifth_category_scenario_ids,
    get_sixth_category_scenario_ids,
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
        scenario_id="fst_second_category_scenario_002",
        stress_category="authority_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_seven = evaluate_first_target(
        scenario_id="fst_second_category_scenario_003",
        stress_category="authority_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_eight = evaluate_first_target(
        scenario_id="fst_second_category_scenario_004",
        stress_category="authority_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_nine = evaluate_first_target(
        scenario_id="fst_third_category_scenario_001",
        stress_category="temporal_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_ten = evaluate_first_target(
        scenario_id="fst_third_category_scenario_002",
        stress_category="temporal_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_eleven = evaluate_first_target(
        scenario_id="fst_third_category_scenario_003",
        stress_category="temporal_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_twelve = evaluate_first_target(
        scenario_id="fst_third_category_scenario_004",
        stress_category="temporal_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_thirteen = evaluate_first_target(
        scenario_id="fst_fourth_category_scenario_001",
        stress_category="state_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_fourteen = evaluate_first_target(
        scenario_id="fst_fifth_category_scenario_001",
        stress_category="path_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    receipt_fifteen = evaluate_first_target(
        scenario_id="fst_sixth_category_scenario_001",
        stress_category="transport_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    for receipt in [
        receipt_one,
        receipt_two,
        receipt_three,
        receipt_four,
        receipt_five,
        receipt_six,
        receipt_seven,
        receipt_eight,
        receipt_nine,
        receipt_ten,
        receipt_eleven,
        receipt_twelve,
        receipt_thirteen,
        receipt_fourteen,
        receipt_fifteen,
    ]:
        _assert_minimal_receipt_shape(receipt)

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

    assert receipt_six["stress_scenario_id"] == "fst_second_category_scenario_002"
    assert receipt_six["stress_category"] == "authority_continuity_stress"
    assert receipt_six["fst_result"] == "PARTIAL"
    assert receipt_six["fst_findings"] == [
        "local authority binding remained live"
    ]
    assert receipt_six["fst_gaps"] == [
        "end-to-end authority continuity not proven across delegated mutation path"
    ]
    assert receipt_six["fst_contradictions"] == []

    assert receipt_seven["stress_scenario_id"] == "fst_second_category_scenario_003"
    assert receipt_seven["stress_category"] == "authority_continuity_stress"
    assert receipt_seven["fst_result"] == "UNVERIFIABLE"
    assert receipt_seven["fst_findings"] == []
    assert receipt_seven["fst_gaps"] == [
        "end-to-end authority continuity not proven across delegated mutation path"
    ]
    assert receipt_seven["fst_contradictions"] == []

    assert receipt_eight["stress_scenario_id"] == "fst_second_category_scenario_004"
    assert receipt_eight["stress_category"] == "authority_continuity_stress"
    assert receipt_eight["fst_result"] == "UNVERIFIABLE"
    assert receipt_eight["fst_findings"] == [
        "local authority binding remained live"
    ]
    assert receipt_eight["fst_gaps"] == []
    assert receipt_eight["fst_contradictions"] == []

    assert receipt_nine["stress_scenario_id"] == "fst_third_category_scenario_001"
    assert receipt_nine["stress_category"] == "temporal_continuity_stress"
    assert receipt_nine["fst_result"] == "CONTRADICTION_EXPOSED"
    assert receipt_nine["fst_findings"] == [
        "local temporal binding remained live"
    ]
    assert receipt_nine["fst_gaps"] == [
        "end-to-end temporal continuity not proven across delayed execution path"
    ]
    assert receipt_nine["fst_contradictions"] == [
        "stronger temporal continuity claim exceeded what the evidenced path supports"
    ]

    assert receipt_ten["stress_scenario_id"] == "fst_third_category_scenario_002"
    assert receipt_ten["stress_category"] == "temporal_continuity_stress"
    assert receipt_ten["fst_result"] == "PARTIAL"
    assert receipt_ten["fst_findings"] == [
        "local temporal binding remained live"
    ]
    assert receipt_ten["fst_gaps"] == [
        "end-to-end temporal continuity not proven across delayed execution path"
    ]
    assert receipt_ten["fst_contradictions"] == []

    assert receipt_eleven["stress_scenario_id"] == "fst_third_category_scenario_003"
    assert receipt_eleven["stress_category"] == "temporal_continuity_stress"
    assert receipt_eleven["fst_result"] == "UNVERIFIABLE"
    assert receipt_eleven["fst_findings"] == []
    assert receipt_eleven["fst_gaps"] == [
        "end-to-end temporal continuity not proven across delayed execution path"
    ]
    assert receipt_eleven["fst_contradictions"] == []

    assert receipt_twelve["stress_scenario_id"] == "fst_third_category_scenario_004"
    assert receipt_twelve["stress_category"] == "temporal_continuity_stress"
    assert receipt_twelve["fst_result"] == "UNVERIFIABLE"
    assert receipt_twelve["fst_findings"] == [
        "local temporal binding remained live"
    ]
    assert receipt_twelve["fst_gaps"] == []
    assert receipt_twelve["fst_contradictions"] == []

    assert receipt_thirteen["stress_scenario_id"] == "fst_fourth_category_scenario_001"
    assert receipt_thirteen["stress_category"] == "state_continuity_stress"
    assert receipt_thirteen["fst_result"] == "CONTRADICTION_EXPOSED"
    assert receipt_thirteen["fst_findings"] == [
        "local state binding remained live"
    ]
    assert receipt_thirteen["fst_gaps"] == [
        "end-to-end state continuity not proven across persisted mutation path"
    ]
    assert receipt_thirteen["fst_contradictions"] == [
        "stronger state continuity claim exceeded what the evidenced path supports"
    ]

    assert receipt_fourteen["stress_scenario_id"] == "fst_fifth_category_scenario_001"
    assert receipt_fourteen["stress_category"] == "path_continuity_stress"
    assert receipt_fourteen["fst_result"] == "CONTRADICTION_EXPOSED"
    assert receipt_fourteen["fst_findings"] == [
        "local path binding remained live"
    ]
    assert receipt_fourteen["fst_gaps"] == [
        "end-to-end path continuity not proven across translated execution route"
    ]
    assert receipt_fourteen["fst_contradictions"] == [
        "stronger path continuity claim exceeded what the evidenced path supports"
    ]

    assert receipt_fifteen["stress_scenario_id"] == "fst_sixth_category_scenario_001"
    assert receipt_fifteen["stress_category"] == "transport_continuity_stress"
    assert receipt_fifteen["fst_result"] == "CONTRADICTION_EXPOSED"
    assert receipt_fifteen["fst_findings"] == [
        "local transport binding remained live"
    ]
    assert receipt_fifteen["fst_gaps"] == [
        "end-to-end transport continuity not proven across delivery channel"
    ]
    assert receipt_fifteen["fst_contradictions"] == [
        "stronger transport continuity claim exceeded what the evidenced path supports"
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
        "fst_second_category_scenario_002",
        "fst_second_category_scenario_003",
        "fst_second_category_scenario_004",
    ]

    third_category_scenario_ids = get_third_category_scenario_ids()
    assert third_category_scenario_ids == [
        "fst_third_category_scenario_001",
        "fst_third_category_scenario_002",
        "fst_third_category_scenario_003",
        "fst_third_category_scenario_004",
    ]

    fourth_category_scenario_ids = get_fourth_category_scenario_ids()
    assert fourth_category_scenario_ids == [
        "fst_fourth_category_scenario_001",
    ]

    fifth_category_scenario_ids = get_fifth_category_scenario_ids()
    assert fifth_category_scenario_ids == [
        "fst_fifth_category_scenario_001",
    ]

    sixth_category_scenario_ids = get_sixth_category_scenario_ids()
    assert sixth_category_scenario_ids == [
        "fst_sixth_category_scenario_001",
    ]

    assert get_all_supported_stress_categories() == [
        "boundary_continuity_stress",
        "authority_continuity_stress",
        "temporal_continuity_stress",
        "state_continuity_stress",
        "path_continuity_stress",
        "transport_continuity_stress",
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
    assert len(second_suite["receipts"]) == 4
    assert second_suite["results_by_scenario_id"] == {
        "fst_second_category_scenario_001": "CONTRADICTION_EXPOSED",
        "fst_second_category_scenario_002": "PARTIAL",
        "fst_second_category_scenario_003": "UNVERIFIABLE",
        "fst_second_category_scenario_004": "UNVERIFIABLE",
    }

    third_suite = run_third_category_suite(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )
    assert third_suite["fst_suite_id"] == "spectre_fst_third_category_suite_v1"
    assert third_suite["stress_category"] == "temporal_continuity_stress"
    assert third_suite["scenario_ids"] == third_category_scenario_ids
    assert len(third_suite["receipts"]) == 4
    assert third_suite["results_by_scenario_id"] == {
        "fst_third_category_scenario_001": "CONTRADICTION_EXPOSED",
        "fst_third_category_scenario_002": "PARTIAL",
        "fst_third_category_scenario_003": "UNVERIFIABLE",
        "fst_third_category_scenario_004": "UNVERIFIABLE",
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

    fifth_suite = run_fifth_category_suite(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )
    assert fifth_suite["fst_suite_id"] == "spectre_fst_fifth_category_suite_v1"
    assert fifth_suite["stress_category"] == "path_continuity_stress"
    assert fifth_suite["scenario_ids"] == fifth_category_scenario_ids
    assert len(fifth_suite["receipts"]) == 1
    assert fifth_suite["results_by_scenario_id"] == {
        "fst_fifth_category_scenario_001": "CONTRADICTION_EXPOSED",
    }

    sixth_suite = run_sixth_category_suite(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )
    assert sixth_suite["fst_suite_id"] == "spectre_fst_sixth_category_suite_v1"
    assert sixth_suite["stress_category"] == "transport_continuity_stress"
    assert sixth_suite["scenario_ids"] == sixth_category_scenario_ids
    assert len(sixth_suite["receipts"]) == 1
    assert sixth_suite["results_by_scenario_id"] == {
        "fst_sixth_category_scenario_001": "CONTRADICTION_EXPOSED",
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
        "path_continuity_stress",
        "transport_continuity_stress",
    ]
    assert set(aggregate["suites_by_category"].keys()) == {
        "boundary_continuity_stress",
        "authority_continuity_stress",
        "temporal_continuity_stress",
        "state_continuity_stress",
        "path_continuity_stress",
        "transport_continuity_stress",
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
            stress_category="temporal_continuity_stress",
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

    print("PASS: fst temporal category expanded to four scenarios")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())