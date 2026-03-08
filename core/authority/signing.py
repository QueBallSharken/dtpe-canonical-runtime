import base64

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from core.crypto.profiles import (
    ED25519_SHA256_CANONICAL_JSON_V1,
    ML_DSA_65_SHA384_CANONICAL_JSON_V1,
)
from core.paths import KEYS_DIR


def _load_ed25519_private_key(identity_id: str) -> Ed25519PrivateKey:
    key_path = KEYS_DIR / f"{identity_id}.ed25519.key"
    if not key_path.exists():
        raise RuntimeError(f"Private key file missing: {key_path}")

    private_key_b64 = key_path.read_text(encoding="utf-8").strip()
    private_key_bytes = base64.b64decode(private_key_b64, validate=True)

    if len(private_key_bytes) != 32:
        raise RuntimeError("Invalid Ed25519 private key length")

    return Ed25519PrivateKey.from_private_bytes(private_key_bytes)


def sign_authority_canonical_ed25519(*, identity_id: str, authority_canonical: str) -> str:
    if not isinstance(identity_id, str) or not identity_id.strip():
        raise RuntimeError("identity_id must be a non-empty string")

    if not isinstance(authority_canonical, str) or not authority_canonical:
        raise RuntimeError("authority_canonical must be a non-empty string")

    private_key = _load_ed25519_private_key(identity_id)
    signature = private_key.sign(authority_canonical.encode("utf-8"))
    return base64.b64encode(signature).decode("ascii")


def sign_authority_canonical(
    *,
    crypto_profile: str,
    identity_id: str,
    authority_canonical: str,
) -> str | None:
    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        raise RuntimeError("crypto_profile must be a non-empty string")

    if crypto_profile == ED25519_SHA256_CANONICAL_JSON_V1:
        return sign_authority_canonical_ed25519(
            identity_id=identity_id,
            authority_canonical=authority_canonical,
        )

    if crypto_profile == ML_DSA_65_SHA384_CANONICAL_JSON_V1:
        raise NotImplementedError("ML-DSA authority signing backend not implemented")

    raise RuntimeError(f"Unsupported crypto profile for authority signing: {crypto_profile!r}")
