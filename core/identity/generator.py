import base64
import json
from pathlib import Path
from typing import Any, Dict

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from core.canonical import canonical_json
from core.hashing import sha256_hex_bytes
from core.identity.identity_registry import verify_identity_invariant
from core.paths import IDENTITIES_DIR, KEYS_DIR


def _write_json_object(path: Path, obj: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json(obj) + "\n", encoding="utf-8")


def _write_private_key_b64(path: Path, private_key_bytes: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(base64.b64encode(private_key_bytes).decode("ascii") + "\n", encoding="utf-8")


def build_identity_record(
    *,
    identity_id: str,
    owner_id: str,
    role: str,
    expires_at: str,
    public_key_b64: str,
    public_key_fingerprint_sha256: str,
) -> Dict[str, Any]:
    return {
        "identity_id": identity_id,
        "owner_id": owner_id,
        "role": role,
        "expires_at": expires_at,
        "key_type": "ed25519",
        "public_key_b64": public_key_b64,
        "public_key_fingerprint_sha256": public_key_fingerprint_sha256,
    }


def generate_identity(
    *,
    identity_id: str,
    owner_id: str,
    role: str,
    expires_at: str,
    overwrite: bool = False,
) -> Dict[str, Any]:
    identity_path = IDENTITIES_DIR / f"{identity_id}.json"
    private_key_path = KEYS_DIR / f"{identity_id}.ed25519.key"

    if not overwrite:
        if identity_path.exists():
            raise RuntimeError(f"Identity file already exists: {identity_path}")
        if private_key_path.exists():
            raise RuntimeError(f"Private key file already exists: {private_key_path}")

    private_key = Ed25519PrivateKey.generate()

    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    )

    public_key_bytes = private_key.public_key().public_bytes_raw()
    public_key_b64 = base64.b64encode(public_key_bytes).decode("ascii")
    public_key_fingerprint_sha256 = sha256_hex_bytes(public_key_bytes)

    identity = build_identity_record(
        identity_id=identity_id,
        owner_id=owner_id,
        role=role,
        expires_at=expires_at,
        public_key_b64=public_key_b64,
        public_key_fingerprint_sha256=public_key_fingerprint_sha256,
    )

    _write_private_key_b64(private_key_path, private_key_bytes)
    _write_json_object(identity_path, identity)

    loaded_identity = json.loads(identity_path.read_text(encoding="utf-8"))
    verify_identity_invariant(loaded_identity, private_key_path)

    return {
        "identity_path": str(identity_path),
        "private_key_path": str(private_key_path),
        "identity": identity,
    }
