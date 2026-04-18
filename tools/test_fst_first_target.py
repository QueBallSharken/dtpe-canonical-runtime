from core.spectre.fst.evaluator import evaluate_first_target


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
        scenario_id="fst_first_target_scenario_001",
        stress_category="boundary_continuity_stress",
        rule_profile_id="spectre_fst_first_target_rules_v1",
    )

    assert receipt_one == receipt_two
    _assert_minimal_receipt_shape(receipt_one)

    assert receipt_one["fst_result"] == "PARTIAL"
    assert receipt_one["fst_findings"] == [
        "local refusal boundary remained live"
    ]
    assert receipt_one["fst_gaps"] == [
        "system-wide refusal continuity not proven under in-flight authority change"
    ]
    assert receipt_one["fst_contradictions"] == []

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
        "unsupported stress_category",
    )

    print("PASS: fst first target deterministic result, minimal receipt, and negative-path validation verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())