from core.spectre.frame_continuity import (
    build_invariant_frame,
    compute_invariant_frame_hash,
    evaluate_frame_continuity,
)


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_true(value, label: str) -> None:
    if not value:
        raise RuntimeError(f"{label}: expected truthy value, got {value!r}")


def main() -> int:
    base_frame = build_invariant_frame(
        policy_hash="policy-1",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
    )
    base_hash = compute_invariant_frame_hash(base_frame)

    initial_result = evaluate_frame_continuity(
        policy_hash="policy-1",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        current_execution_time="2029-01-01T00:00:00",
        prior_invariant_frame_hash=None,
        prior_execution_time=None,
        continuity_required=False,
    )
    assert_equal(initial_result["ok"], True, "initial.ok")
    assert_equal(initial_result["reason"], "initial_frame", "initial.reason")
    assert_equal(initial_result["continuity_mode"], "INITIAL", "initial.mode")
    assert_true(initial_result["sequence_id"], "initial.sequence_id")

    exact_result = evaluate_frame_continuity(
        policy_hash="policy-1",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        current_execution_time="2029-01-02T00:00:00",
        prior_invariant_frame_hash=base_hash,
        prior_execution_time="2029-01-01T00:00:00",
        continuity_required=True,
    )
    assert_equal(exact_result["ok"], True, "exact.ok")
    assert_equal(exact_result["reason"], "frame_continuity_ok", "exact.reason")
    assert_equal(exact_result["continuity_mode"], "EXACT", "exact.mode")
    assert_equal(exact_result["temporal_continuity_ok"], True, "exact.temporal_ok")

    missing_prior_hash = evaluate_frame_continuity(
        policy_hash="policy-1",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        current_execution_time="2029-01-02T00:00:00",
        prior_invariant_frame_hash=None,
        prior_execution_time="2029-01-01T00:00:00",
        continuity_required=True,
    )
    assert_equal(missing_prior_hash["ok"], False, "missing_hash.ok")
    assert_equal(missing_prior_hash["reason"], "missing_prior_frame_hash", "missing_hash.reason")

    missing_prior_time = evaluate_frame_continuity(
        policy_hash="policy-1",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        current_execution_time="2029-01-02T00:00:00",
        prior_invariant_frame_hash=base_hash,
        prior_execution_time=None,
        continuity_required=True,
    )
    assert_equal(missing_prior_time["ok"], False, "missing_time.ok")
    assert_equal(missing_prior_time["reason"], "missing_prior_execution_time", "missing_time.reason")

    mismatch_disabled = evaluate_frame_continuity(
        policy_hash="policy-2",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        current_execution_time="2029-01-02T00:00:00",
        prior_invariant_frame_hash=base_hash,
        prior_execution_time="2029-01-01T00:00:00",
        continuity_required=True,
        transition_mode="DISABLED",
    )
    assert_equal(mismatch_disabled["ok"], False, "mismatch_disabled.ok")
    assert_equal(mismatch_disabled["reason"], "frame_mismatch", "mismatch_disabled.reason")

    next_frame = build_invariant_frame(
        policy_hash="policy-2",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
    )
    next_hash = compute_invariant_frame_hash(next_frame)

    authorized_transition = evaluate_frame_continuity(
        policy_hash="policy-2",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        current_execution_time="2029-01-02T00:00:00",
        prior_invariant_frame_hash=base_hash,
        prior_execution_time="2029-01-01T00:00:00",
        continuity_required=True,
        transition_mode="EXPLICIT_MAP",
        allowed_frame_transitions=[{"from": base_hash, "to": next_hash}],
    )
    assert_equal(authorized_transition["ok"], True, "authorized.ok")
    assert_equal(authorized_transition["reason"], "authorized_frame_transition", "authorized.reason")
    assert_equal(authorized_transition["continuity_mode"], "AUTHORIZED_TRANSITION", "authorized.mode")

    temporal_violation = evaluate_frame_continuity(
        policy_hash="policy-1",
        authority_hash="authority-1",
        execution_intent="demo.intent",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        current_execution_time="2028-12-31T00:00:00",
        prior_invariant_frame_hash=base_hash,
        prior_execution_time="2029-01-01T00:00:00",
        continuity_required=True,
    )
    assert_equal(temporal_violation["ok"], False, "temporal_violation.ok")
    assert_equal(temporal_violation["reason"], "temporal_order_violation", "temporal_violation.reason")
    assert_equal(temporal_violation["continuity_mode"], "VIOLATION", "temporal_violation.mode")

    print("PASS: phase7 frame continuity guard verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
