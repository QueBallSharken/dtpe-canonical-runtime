import base64

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from core.identity.identity_registry import load_identity


def verify_authority_signature_ed25519(
    *,
    identity_id: str,
    authority_canonical: str,
    signature_b64: str,
) -> bool:
    if not isinstance(identity_id, str) or not identity_id.strip():
        raise RuntimeError("identity_id must be a non-empty string")

    if not isinstance(authority_canonical, str) or not authority_canonical:
        raise RuntimeError("authority_canonical must be a non-empty string")

    if not isinstance(signature_b64, str) or not signature_b64.strip():
        raise RuntimeError("signature_b64 must be a non-empty string")

    identity = load_identity(identity_id)

    public_key_b64 = identity.get("public_key_b64")
    if not isinstance(public_key_b64, str) or not public_key_b64.strip():
        raise RuntimeError("Identity missing public_key_b64")

    public_key_bytes = base64.b64decode(public_key_b64, validate=True)
    signature_bytes = base64.b64decode(signature_b64, validate=True)

    public_key = Ed25519PublicKey.from_public_bytes(public_key_bytes)

    try:
        public_key.verify(signature_bytes, authority_canonical.encode("utf-8"))
    except InvalidSignature:
        return False

    return True
