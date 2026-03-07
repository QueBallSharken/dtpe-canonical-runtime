import json
from pathlib import Path
from typing import Any, Dict

from core.canonical import canonical_json
from core.hashing import sha256_hex_str
from core.paths import POLICY_DIR


def load_policy_file(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"Policy file missing: {path}")

    raw = path.read_text(encoding="utf-8-sig")
    obj = json.loads(raw)

    if not isinstance(obj, dict):
        raise RuntimeError("Policy file must contain a JSON object")

    policy_version = obj.get("policy_version")
    if not isinstance(policy_version, str) or not policy_version.strip():
        raise RuntimeError("Policy file must contain non-empty policy_version")

    crypto_profile = obj.get("crypto_profile")
    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        raise RuntimeError("Policy file must contain non-empty crypto_profile")

    return obj


def build_policy_snapshot(policy_obj: Dict[str, Any]) -> Dict[str, str]:
    policy_version = policy_obj.get("policy_version")
    if not isinstance(policy_version, str) or not policy_version.strip():
        raise RuntimeError("Policy object must contain non-empty policy_version")

    crypto_profile = policy_obj.get("crypto_profile")
    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        raise RuntimeError("Policy object must contain non-empty crypto_profile")

    policy_canonical = canonical_json(policy_obj)
    policy_state_hash = sha256_hex_str(policy_canonical)

    return {
        "policy_version": policy_version,
        "crypto_profile": crypto_profile,
        "policy_canonical": policy_canonical,
        "policy_state_hash": policy_state_hash,
    }


def load_policy_snapshot(policy_filename: str) -> Dict[str, str]:
    path = POLICY_DIR / policy_filename
    policy_obj = load_policy_file(path)
    return build_policy_snapshot(policy_obj)
