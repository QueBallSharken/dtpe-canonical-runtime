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
from core.spectre.fst.runner import run_first_target_suite
from core.spectre.fst.scenarios import get_first_target_scenario_ids


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

    _assert_minimal_receipt_shape(receipt_one)
    _assert_minimal_receipt_shape(receipt_two)
    _assert_minimal_receipt_shape(receipt_three)
    _assert_minimal_receipt_shape(receipt_four)

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

    scenario_ids = get_first_target_scenario_ids()
    assert scenario_ids == [
        "fst_first_target_scenario_001",
        "fst_first_target_scenario_002",
        "fst_first_target_scenario_003",
        "fst_first_target_scenario_004",
    ]

    rule_profile = get_first_target_rule_profile()
    expected_rule_profile_hash = sha256_hex_str(canonical_json(rule_profile))
    assert get_first_target_rule_profile_hash() == expected_rule_profile_hash

    assert get_minimal_receipt_canonical(receipt_one) == canonical_json(receipt_one)
    assert get_minimal_receipt_hash(receipt_one) == sha256_hex_str(canonical_json(receipt_one))

    suite = run_first_target_suite(
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    assert suite["fst_suite_id"] == "spectre_fst_first_target_suite_v1"
    assert suite["fst_suite_version"] == "1.0"
    assert suite["fst_rule_profile_id"] == "spectre_fst_first_target_rules_v1"
    assert suite["stress_category"] == "boundary_continuity_stress"
    assert suite["scenario_ids"] == scenario_ids
    assert len(suite["receipts"]) == 4
    assert suite["results_by_scenario_id"] == {
        "fst_first_target_scenario_001": "PARTIAL",
        "fst_first_target_scenario_002": "CONTRADICTION_EXPOSED",
        "fst_first_target_scenario_003": "UNVERIFIABLE",
        "fst_first_target_scenario_004": "UNVERIFIABLE",
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

    print("PASS: fst four-scenario suite, inventory, and receipt identity verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())