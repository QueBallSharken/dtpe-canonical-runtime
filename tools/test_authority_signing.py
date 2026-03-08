from core.authority.snapshot import build_authority_snapshot
from core.authority.signing import sign_authority_canonical_ed25519
from core.authority.verification import verify_authority_signature_ed25519


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def main() -> int:
    snapshot = build_authority_snapshot(
        identity_id="alice",
        owner_id="alice",
        intent="demo.intent",
        action="execute",
        expires_at="2030-01-01T00:00:00",
        policy_version="v1",
        policy_state_hash="abc123",
        crypto_profile="ed25519+sha256+canonical_json_v1",
    )

    signature_b64 = sign_authority_canonical_ed25519(
        identity_id="alice",
        authority_canonical=snapshot["authority_canonical"],
    )

    verified = verify_authority_signature_ed25519(
        identity_id="alice",
        authority_canonical=snapshot["authority_canonical"],
        signature_b64=signature_b64,
    )
    assert_equal(verified, True, "verified")

    tampered_verified = verify_authority_signature_ed25519(
        identity_id="alice",
        authority_canonical=snapshot["authority_canonical"] + "x",
        signature_b64=signature_b64,
    )
    assert_equal(tampered_verified, False, "tampered_verified")

    print("PASS: authority signing and verification verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
