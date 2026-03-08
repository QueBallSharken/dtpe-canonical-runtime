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
    )
    assert_equal(mismatch["execution_state"], "REFUSED_NON_BINDING", "mismatch.execution_state")
    assert_equal(mismatch["reason"], "crypto_profile_mismatch", "mismatch.reason")

    print("PASS: phase4 crypto profile enforcement decision paths verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
