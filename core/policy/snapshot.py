import json
from pathlib import Path
from typing import Any, Dict, List

from core.canonical import canonical_json
from core.hashing import sha256_hex_str
from core.paths import POLICY_DIR


def _require_permitted_crypto_profiles(value: Any) -> List[str]:
    if not isinstance(value, list) or not value:
        raise RuntimeError("Policy file must contain non-empty permitted_crypto_profiles")

    normalized: List[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise RuntimeError(
                "Policy file permitted_crypto_profiles must contain only non-empty strings"
            )
        normalized.append(item)

    if normalized != sorted(normalized):
        raise RuntimeError("Policy file permitted_crypto_profiles must be deterministically ordered")

    return normalized


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

    permitted_crypto_profiles = _require_permitted_crypto_profiles(
        obj.get("permitted_crypto_profiles")
    )

    if crypto_profile not in permitted_crypto_profiles:
        raise RuntimeError(
            "Policy file crypto_profile must be a member of permitted_crypto_profiles"
        )

    return obj


def build_policy_snapshot(policy_obj: Dict[str, Any]) -> Dict[str, Any]:
    policy_version = policy_obj.get("policy_version")
    if not isinstance(policy_version, str) or not policy_version.strip():
        raise RuntimeError("Policy object must contain non-empty policy_version")

    crypto_profile = policy_obj.get("crypto_profile")
    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        raise RuntimeError("Policy object must contain non-empty crypto_profile")

    permitted_crypto_profiles = _require_permitted_crypto_profiles(
        policy_obj.get("permitted_crypto_profiles")
    )

    if crypto_profile not in permitted_crypto_profiles:
        raise RuntimeError(
            "Policy object crypto_profile must be a member of permitted_crypto_profiles"
        )

    policy_canonical = canonical_json(policy_obj)
    policy_state_hash = sha256_hex_str(policy_canonical)

    return {
        "policy_version": policy_version,
        "crypto_profile": crypto_profile,
        "permitted_crypto_profiles": permitted_crypto_profiles,
        "policy_canonical": policy_canonical,
        "policy_state_hash": policy_state_hash,
    }


def load_policy_snapshot(policy_filename: str) -> Dict[str, Any]:
    path = POLICY_DIR / policy_filename
    policy_obj = load_policy_file(path)
    return build_policy_snapshot(policy_obj)
