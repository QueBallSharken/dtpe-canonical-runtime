import base64
import json
from pathlib import Path
from typing import Dict, Any

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from core.hashing import sha256_hex_bytes
from core.paths import IDENTITIES_DIR


def load_identity(identity_id: str) -> Dict[str, Any]:
    path = IDENTITIES_DIR / f"{identity_id}.json"
    if not path.exists():
        raise RuntimeError(f"Identity file missing: {path}")

    raw = path.read_text(encoding="utf-8")
    obj = json.loads(raw)

    if not isinstance(obj, dict):
        raise RuntimeError("Identity file must contain a JSON object")

    return obj


def resolve_identity_key_record(identity: Dict[str, Any], crypto_profile: str) -> Dict[str, str]:
    if not isinstance(identity, dict):
        raise RuntimeError("identity must be a JSON object")

    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        raise RuntimeError("crypto_profile must be a non-empty string")

    keys = identity.get("keys")
    if isinstance(keys, dict):
        key_record = keys.get(crypto_profile)
        if not isinstance(key_record, dict):
            raise RuntimeError(
                f"Identity missing key record for crypto_profile {crypto_profile!r}"
            )

        public_key_b64 = key_record.get("public_key_b64")
        if not isinstance(public_key_b64, str) or not public_key_b64.strip():
            raise RuntimeError("Identity key record missing public_key_b64")

        public_key_fingerprint_sha256 = key_record.get("public_key_fingerprint_sha256")
        if (
            not isinstance(public_key_fingerprint_sha256, str)
            or not public_key_fingerprint_sha256.strip()
        ):
            raise RuntimeError("Identity key record missing public_key_fingerprint_sha256")

        return {
            "public_key_b64": public_key_b64,
            "public_key_fingerprint_sha256": public_key_fingerprint_sha256,
        }

    public_key_b64 = identity.get("public_key_b64")
    if not isinstance(public_key_b64, str) or not public_key_b64.strip():
        raise RuntimeError("Identity missing public_key_b64")

    public_key_fingerprint_sha256 = identity.get("public_key_fingerprint_sha256")
    if (
        not isinstance(public_key_fingerprint_sha256, str)
        or not public_key_fingerprint_sha256.strip()
    ):
        raise RuntimeError("Identity missing public_key_fingerprint_sha256")

    return {
        "public_key_b64": public_key_b64,
        "public_key_fingerprint_sha256": public_key_fingerprint_sha256,
    }


def _load_private_key_bytes(private_key_path: Path) -> bytes:
    priv_b64 = private_key_path.read_text(encoding="utf-8").strip()
    priv_bytes = base64.b64decode(priv_b64, validate=True)

    if len(priv_bytes) != 32:
        raise RuntimeError("Invalid Ed25519 private key length")

    return priv_bytes


def derive_public_key_bytes(private_key_path: Path) -> bytes:
    priv_bytes = _load_private_key_bytes(private_key_path)
    priv = Ed25519PrivateKey.from_private_bytes(priv_bytes)
    return priv.public_key().public_bytes_raw()


def derive_public_key_b64(private_key_path: Path) -> str:
    pub = derive_public_key_bytes(private_key_path)
    return base64.b64encode(pub).decode("ascii")


def derive_public_key_fingerprint_sha256(private_key_path: Path) -> str:
    pub = derive_public_key_bytes(private_key_path)
    return sha256_hex_bytes(pub)


def verify_identity_invariant(identity: Dict[str, Any], private_key_path: Path) -> None:
    stored_public_key = identity.get("public_key_b64")
    if not isinstance(stored_public_key, str):
        raise RuntimeError("Identity missing public_key_b64")

    stored_fingerprint = identity.get("public_key_fingerprint_sha256")
    if not isinstance(stored_fingerprint, str):
        raise RuntimeError("Identity missing public_key_fingerprint_sha256")

    derived_public_key = derive_public_key_b64(private_key_path)
    derived_fingerprint = derive_public_key_fingerprint_sha256(private_key_path)

    if stored_public_key != derived_public_key:
        raise RuntimeError(
            "Identity invariant violated: stored public key does not match private key"
        )

    if stored_fingerprint != derived_fingerprint:
        raise RuntimeError(
            "Identity invariant violated: stored fingerprint does not match derived fingerprint"
        )
