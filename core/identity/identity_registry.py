import base64
import json
from pathlib import Path
from typing import Dict, Any

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

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


def derive_public_key_b64(private_key_path: Path) -> str:
    priv_b64 = private_key_path.read_text(encoding="utf-8").strip()
    priv_bytes = base64.b64decode(priv_b64, validate=True)

    if len(priv_bytes) != 32:
        raise RuntimeError("Invalid Ed25519 private key length")

    priv = Ed25519PrivateKey.from_private_bytes(priv_bytes)

    pub = priv.public_key().public_bytes_raw()

    return base64.b64encode(pub).decode("ascii")


def verify_identity_invariant(identity: Dict[str, Any], private_key_path: Path) -> None:
    stored = identity.get("public_key_b64")
    if not isinstance(stored, str):
        raise RuntimeError("Identity missing public_key_b64")

    derived = derive_public_key_b64(private_key_path)

    if stored != derived:
        raise RuntimeError(
            "Identity invariant violated: stored public key does not match private key"
        )
