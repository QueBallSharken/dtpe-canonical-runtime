from core.authority.signing import sign_authority_canonical


def main() -> int:
    try:
        sign_authority_canonical(
            crypto_profile="ml_dsa_65+sha384+canonical_json_v1",
            identity_id="alice",
            authority_canonical="{}",
        )
    except NotImplementedError:
        print("PASS: ML-DSA signing correctly unimplemented")
        return 0

    raise RuntimeError("ML-DSA signing should raise NotImplementedError")


if __name__ == "__main__":
    raise SystemExit(main())
