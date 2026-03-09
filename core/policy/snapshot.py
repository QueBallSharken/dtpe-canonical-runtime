import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

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


def _optional_migration_window(
    value: Any,
    permitted_crypto_profiles: List[str],
) -> Optional[Dict[str, str]]:
    if value is None:
        return None

    if not isinstance(value, dict):
        raise RuntimeError("Policy file migration_window must be a JSON object")

    from_crypto_profile = value.get("from_crypto_profile")
    to_crypto_profile = value.get("to_crypto_profile")
    not_before = value.get("not_before")
    not_after = value.get("not_after")

    if not isinstance(from_crypto_profile, str) or not from_crypto_profile.strip():
        raise RuntimeError("Policy file migration_window must contain non-empty from_crypto_profile")

    if not isinstance(to_crypto_profile, str) or not to_crypto_profile.strip():
        raise RuntimeError("Policy file migration_window must contain non-empty to_crypto_profile")

    if not isinstance(not_before, str) or not not_before.strip():
        raise RuntimeError("Policy file migration_window must contain non-empty not_before")

    if not isinstance(not_after, str) or not not_after.strip():
        raise RuntimeError("Policy file migration_window must contain non-empty not_after")

    if from_crypto_profile not in permitted_crypto_profiles:
        raise RuntimeError(
            "Policy file migration_window from_crypto_profile must be permitted by policy"
        )

    if to_crypto_profile not in permitted_crypto_profiles:
        raise RuntimeError(
            "Policy file migration_window to_crypto_profile must be permitted by policy"
        )

    try:
        not_before_dt = datetime.fromisoformat(not_before)
    except ValueError:
        raise RuntimeError("Policy file migration_window not_before must be ISO-8601") from None

    try:
        not_after_dt = datetime.fromisoformat(not_after)
    except ValueError:
        raise RuntimeError("Policy file migration_window not_after must be ISO-8601") from None

    if not_before_dt >= not_after_dt:
        raise RuntimeError("Policy file migration_window not_before must be earlier than not_after")

    return {
        "from_crypto_profile": from_crypto_profile,
        "to_crypto_profile": to_crypto_profile,
        "not_before": not_before,
        "not_after": not_after,
    }


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

    _optional_migration_window(
        obj.get("migration_window"),
        permitted_crypto_profiles,
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

    migration_window = _optional_migration_window(
        policy_obj.get("migration_window"),
        permitted_crypto_profiles,
    )

    policy_canonical = canonical_json(policy_obj)
    policy_state_hash = sha256_hex_str(policy_canonical)

    return {
        "policy_version": policy_version,
        "crypto_profile": crypto_profile,
        "permitted_crypto_profiles": permitted_crypto_profiles,
        "migration_window": migration_window,
        "policy_canonical": policy_canonical,
        "policy_state_hash": policy_state_hash,
    }


def load_policy_snapshot(policy_filename: str) -> Dict[str, Any]:
    path = POLICY_DIR / policy_filename
    policy_obj = load_policy_file(path)
    return build_policy_snapshot(policy_obj)
