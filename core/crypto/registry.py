from typing import Callable, Dict

from core.crypto.profiles import (
    ED25519_SHA256_CANONICAL_JSON_V1,
    ML_DSA_65_SHA384_CANONICAL_JSON_V1,
)

CryptoVerifyFn = Callable[[bytes, bytes, bytes], bool]

_CRYPTO_REGISTRY: Dict[str, CryptoVerifyFn] = {}


def register_crypto_profile(profile: str, verifier: CryptoVerifyFn) -> None:
    if not isinstance(profile, str) or not profile.strip():
        raise ValueError("invalid crypto profile")

    if profile in _CRYPTO_REGISTRY:
        raise ValueError("crypto profile already registered")

    _CRYPTO_REGISTRY[profile] = verifier


def get_crypto_verifier(profile: str) -> CryptoVerifyFn:
    if profile not in _CRYPTO_REGISTRY:
        raise ValueError("crypto profile not registered")

    return _CRYPTO_REGISTRY[profile]


def list_registered_profiles() -> Dict[str, CryptoVerifyFn]:
    return dict(_CRYPTO_REGISTRY)


def initialize_builtin_registry() -> None:
    # placeholders for future implementations
    def _not_implemented(*args, **kwargs):
        raise NotImplementedError("crypto backend not implemented")

    register_crypto_profile(ED25519_SHA256_CANONICAL_JSON_V1, _not_implemented)
    register_crypto_profile(ML_DSA_65_SHA384_CANONICAL_JSON_V1, _not_implemented)
