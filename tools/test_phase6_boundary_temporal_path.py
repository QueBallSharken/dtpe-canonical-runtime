from core.spectre.boundary import evaluate_execution_boundary


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def main() -> int:
    allow_result = evaluate_execution_boundary(
        authority_result={"ok": True, "reason": "ALLOW"},
        canonical_current_state={"state": "ready"},
        system_state={"policy": "ok"},
        canonical_transition={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2030-01-01T00:00:00",
        },
        canonical_policy_state_hash="abc123",
        execution_intent="demo.intent",
        authority_hash="def456",
        crypto_profile="ed25519+sha256+canonical_json_v1",
        execution_time="2029-01-01T00:00:00",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        prior_invariant_frame_hash=None,
        prior_execution_time=None,
        continuity_required=False,
    )

    assert_equal(allow_result["ok"], True, "allow.ok")
    assert_equal(allow_result["execution_state"], "ALLOW", "allow.execution_state")
    assert_equal(allow_result["reason"], "BOUNDARY_ALLOW", "allow.reason")
    assert_equal(
        allow_result["temporal_invariant_result"]["reason"],
        "VALID",
        "allow.temporal.reason",
    )

    refused_result = evaluate_execution_boundary(
        authority_result={"ok": True, "reason": "ALLOW"},
        canonical_current_state={"state": "ready"},
        system_state={"policy": "ok"},
        canonical_transition={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2020-01-01T00:00:00",
        },
        canonical_policy_state_hash="abc123",
        execution_intent="demo.intent",
        authority_hash="def456",
        crypto_profile="ed25519+sha256+canonical_json_v1",
        execution_time="2025-01-01T00:00:00",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
        prior_invariant_frame_hash=None,
        prior_execution_time=None,
        continuity_required=False,
    )

    assert_equal(refused_result["ok"], False, "refused.ok")
    assert_equal(
        refused_result["execution_state"],
        "REFUSED_NON_BINDING",
        "refused.execution_state",
    )
    assert_equal(
        refused_result["reason"],
        "BOUNDARY_REFUSED_NON_BINDING",
        "refused.reason",
    )
    assert_equal(
        refused_result["temporal_invariant_result"]["reason"],
        "EXPIRED",
        "refused.temporal.reason",
    )

    print("PASS: phase6 boundary temporal path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
