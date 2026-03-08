from core.crypto.registry import (
    initialize_builtin_registry,
    get_crypto_verifier,
    list_registered_profiles,
)

from core.crypto.profiles import (
    ED25519_SHA256_CANONICAL_JSON_V1,
    ML_DSA_65_SHA384_CANONICAL_JSON_V1,
)


def main() -> int:
    initialize_builtin_registry()

    profiles = list_registered_profiles()

    if ED25519_SHA256_CANONICAL_JSON_V1 not in profiles:
        raise RuntimeError("ed25519 profile not registered")

    if ML_DSA_65_SHA384_CANONICAL_JSON_V1 not in profiles:
        raise RuntimeError("ml-dsa profile not registered")

    ed = get_crypto_verifier(ED25519_SHA256_CANONICAL_JSON_V1)
    pq = get_crypto_verifier(ML_DSA_65_SHA384_CANONICAL_JSON_V1)

    if not callable(ed):
        raise RuntimeError("ed25519 verifier not callable")

    if not callable(pq):
        raise RuntimeError("ml-dsa verifier not callable")

    print("PASS: crypto registry initialization verified")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
