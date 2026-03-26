from core.spectre.boundary import evaluate_execution_boundary


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def main() -> int:
    authority_result = {"ok": True, "execution_state": "ALLOW", "reason": "ok"}
    canonical_current_state = {"dummy": "state"}
    system_state = {"dummy": "system"}
    canonical_transition = {
        "identity_id": "alice",
        "owner_id": "alice",
        "intent": "demo.intent",
        "action": "execute",
        "expires_at": "2030-01-01T00:00:00",
    }

    result = evaluate_execution_boundary(
        authority_result=authority_result,
        canonical_current_state=canonical_current_state,
        system_state=system_state,
        canonical_transition=canonical_transition,
        canonical_policy_state_hash="policy-1",
        execution_intent="demo.intent",
        authority_hash="authority-1",
        crypto_profile="test-profile",
        execution_time="2029-01-01T00:00:00",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        prior_invariant_frame_hash=None,
        prior_execution_time=None,
        continuity_required=False,
    )

    signal_profile = result.get("signal_profile")
    if not isinstance(signal_profile, dict):
        raise RuntimeError("signal_profile missing or invalid")

    assert_equal(signal_profile["state_admissibility"]["ok"], True, "signal.state.ok")
    assert_equal(signal_profile["system_stability"]["ok"], True, "signal.stability.ok")
    assert_equal(signal_profile["temporal_invariant"]["ok"], True, "signal.temporal.ok")
    assert_equal(signal_profile["frame_continuity"]["ok"], True, "signal.frame.ok")
    assert_equal(signal_profile["signal_profile_version"], "v1", "signal.version")

    print("PASS: phase8 signal_profile verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
