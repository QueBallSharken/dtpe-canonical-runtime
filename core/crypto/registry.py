from typing import Callable, Dict

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from core.crypto.profiles import (
    ED25519_SHA256_CANONICAL_JSON_V1,
    ML_DSA_65_SHA384_CANONICAL_JSON_V1,
)

CryptoVerifyFn = Callable[[bytes, bytes, bytes], bool]

_CRYPTO_REGISTRY: Dict[str, CryptoVerifyFn] = {}


def _verify_ed25519(public_key_bytes: bytes, message_bytes: bytes, signature_bytes: bytes) -> bool:
    public_key = Ed25519PublicKey.from_public_bytes(public_key_bytes)

    try:
        public_key.verify(signature_bytes, message_bytes)
    except InvalidSignature:
        return False

    return True


def _not_implemented(*args, **kwargs):
    raise NotImplementedError("crypto backend not implemented")


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
    if ED25519_SHA256_CANONICAL_JSON_V1 not in _CRYPTO_REGISTRY:
        register_crypto_profile(ED25519_SHA256_CANONICAL_JSON_V1, _verify_ed25519)

    if ML_DSA_65_SHA384_CANONICAL_JSON_V1 not in _CRYPTO_REGISTRY:
        register_crypto_profile(ML_DSA_65_SHA384_CANONICAL_JSON_V1, _not_implemented)
