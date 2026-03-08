from datetime import datetime, timedelta

from core.phase4.decision import decide_phase4


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def main() -> int:
    supported = decide_phase4(
        authority_snapshot={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2030-01-01T00:00:00",
            "policy_version": "v1",
            "policy_state_hash": "abc123",
            "crypto_profile": "ed25519+sha256+canonical_json_v1",
        },
        expected_crypto_profile="ed25519+sha256+canonical_json_v1",
        permitted_crypto_profiles=["ed25519+sha256+canonical_json_v1"],
    )
    assert_equal(supported["execution_state"], "ALLOW", "supported.execution_state")
    assert_equal(supported["reason"], "admissible", "supported.reason")

    missing = decide_phase4(
        authority_snapshot={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2030-01-01T00:00:00",
            "policy_version": "v1",
            "policy_state_hash": "abc123",
        },
        expected_crypto_profile="ed25519+sha256+canonical_json_v1",
        permitted_crypto_profiles=["ed25519+sha256+canonical_json_v1"],
    )
    assert_equal(missing["execution_state"], "REFUSED_NON_BINDING", "missing.execution_state")
    assert_equal(missing["reason"], "missing_crypto_profile", "missing.reason")

    unsupported = decide_phase4(
        authority_snapshot={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2030-01-01T00:00:00",
            "policy_version": "v1",
            "policy_state_hash": "abc123",
            "crypto_profile": "ml_dsa_65+sha384+canonical_json_v1",
        },
        expected_crypto_profile="ml_dsa_65+sha384+canonical_json_v1",
        permitted_crypto_profiles=["ml_dsa_65+sha384+canonical_json_v1"],
    )
    assert_equal(unsupported["execution_state"], "REFUSED_NON_BINDING", "unsupported.execution_state")
    assert_equal(unsupported["reason"], "unsupported_crypto_profile", "unsupported.reason")

    mismatch = decide_phase4(
        authority_snapshot={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2030-01-01T00:00:00",
            "policy_version": "v1",
            "policy_state_hash": "abc123",
            "crypto_profile": "ed25519+sha256+canonical_json_v1",
        },
        expected_crypto_profile="ml_dsa_65+sha384+canonical_json_v1",
        permitted_crypto_profiles=[
            "ed25519+sha256+canonical_json_v1",
            "ml_dsa_65+sha384+canonical_json_v1",
        ],
    )
    assert_equal(mismatch["execution_state"], "REFUSED_NON_BINDING", "mismatch.execution_state")
    assert_equal(mismatch["reason"], "crypto_profile_mismatch", "mismatch.reason")

    not_permitted = decide_phase4(
        authority_snapshot={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2030-01-01T00:00:00",
            "policy_version": "v1",
            "policy_state_hash": "abc123",
            "crypto_profile": "ed25519+sha256+canonical_json_v1",
        },
        expected_crypto_profile="ed25519+sha256+canonical_json_v1",
        permitted_crypto_profiles=["ml_dsa_65+sha384+canonical_json_v1"],
    )
    assert_equal(
        not_permitted["execution_state"],
        "REFUSED_NON_BINDING",
        "not_permitted.execution_state",
    )
    assert_equal(
        not_permitted["reason"],
        "crypto_profile_not_permitted_by_policy",
        "not_permitted.reason",
    )

    now = datetime.utcnow()
    active_not_before = (now - timedelta(minutes=5)).isoformat()
    active_not_after = (now + timedelta(minutes=5)).isoformat()
    inactive_not_before = (now + timedelta(minutes=10)).isoformat()
    inactive_not_after = (now + timedelta(minutes=20)).isoformat()

    active_migration = decide_phase4(
        authority_snapshot={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2030-01-01T00:00:00",
            "policy_version": "v1",
            "policy_state_hash": "abc123",
            "crypto_profile": "ed25519+sha256+canonical_json_v1",
        },
        expected_crypto_profile="ml_dsa_65+sha384+canonical_json_v1",
        permitted_crypto_profiles=[
            "ed25519+sha256+canonical_json_v1",
            "ml_dsa_65+sha384+canonical_json_v1",
        ],
        migration_window={
            "from_crypto_profile": "ed25519+sha256+canonical_json_v1",
            "to_crypto_profile": "ml_dsa_65+sha384+canonical_json_v1",
            "not_before": active_not_before,
            "not_after": active_not_after,
        },
    )
    assert_equal(
        active_migration["execution_state"],
        "ALLOW",
        "active_migration.execution_state",
    )
    assert_equal(
        active_migration["reason"],
        "admissible_during_migration_window",
        "active_migration.reason",
    )

    inactive_migration = decide_phase4(
        authority_snapshot={
            "identity_id": "alice",
            "owner_id": "alice",
            "intent": "demo.intent",
            "action": "execute",
            "expires_at": "2030-01-01T00:00:00",
            "policy_version": "v1",
            "policy_state_hash": "abc123",
            "crypto_profile": "ed25519+sha256+canonical_json_v1",
        },
        expected_crypto_profile="ml_dsa_65+sha384+canonical_json_v1",
        permitted_crypto_profiles=[
            "ed25519+sha256+canonical_json_v1",
            "ml_dsa_65+sha384+canonical_json_v1",
        ],
        migration_window={
            "from_crypto_profile": "ed25519+sha256+canonical_json_v1",
            "to_crypto_profile": "ml_dsa_65+sha384+canonical_json_v1",
            "not_before": inactive_not_before,
            "not_after": inactive_not_after,
        },
    )
    assert_equal(
        inactive_migration["execution_state"],
        "REFUSED_NON_BINDING",
        "inactive_migration.execution_state",
    )
    assert_equal(
        inactive_migration["reason"],
        "crypto_profile_mismatch",
        "inactive_migration.reason",
    )

    print("PASS: phase4 crypto profile enforcement decision paths verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
