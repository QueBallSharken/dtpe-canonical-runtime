from core.spectre.boundary import evaluate_execution_boundary


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_true(value, label: str) -> None:
    if not value:
        raise RuntimeError(f"{label}: expected truthy value, got {value!r}")


def main() -> int:
    authority_result = {"ok": True}

    canonical_current_state = {"dummy": "state"}
    system_state = {"dummy": "system"}
    canonical_transition = {
        "identity_id": "alice",
        "owner_id": "alice",
        "intent": "demo.intent",
        "action": "execute",
        "expires_at": "2030-01-01T00:00:00",
    }

    base_inputs = dict(
        authority_result=authority_result,
        canonical_current_state=canonical_current_state,
        system_state=system_state,
        canonical_transition=canonical_transition,
        canonical_policy_state_hash="policy-1",
        execution_intent="demo.intent",
        authority_hash="authority-1",
        crypto_profile="test-profile",
        execution_time="2029-01-02T00:00:00",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
    )

    result_initial = evaluate_execution_boundary(
        **base_inputs,
        prior_invariant_frame_hash=None,
        prior_execution_time=None,
        continuity_required=False,
    )

    assert_equal(result_initial["ok"], True, "initial.ok")
    assert_true(result_initial["frame_continuity_result"], "initial.frame_result")

    prior_hash = result_initial["invariant_frame_hash"]

    result_exact = evaluate_execution_boundary(
        **base_inputs,
        prior_invariant_frame_hash=prior_hash,
        prior_execution_time="2029-01-01T00:00:00",
        continuity_required=True,
    )

    assert_equal(result_exact["ok"], True, "exact.ok")

    result_temporal_fail = evaluate_execution_boundary(
        **base_inputs,
        prior_invariant_frame_hash=prior_hash,
        prior_execution_time="2030-01-01T00:00:00",
        continuity_required=True,
    )

    assert_equal(result_temporal_fail["ok"], False, "temporal_fail.ok")

    print("PASS: phase7 boundary frame continuity path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
