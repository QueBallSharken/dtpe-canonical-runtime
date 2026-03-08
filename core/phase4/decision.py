from datetime import datetime
from typing import Dict, List, Optional, Set


SUPPORTED_CRYPTO_PROFILES = {
    "ed25519+sha256+canonical_json_v1",
}


def _normalize_permitted_crypto_profiles(value: object) -> Optional[List[str]]:
    if value is None:
        return None

    if not isinstance(value, list) or not value:
        return []

    normalized: List[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            return []
        normalized.append(item)

    return normalized


def decide_phase4(
    *,
    authority_snapshot: Dict[str, str],
    expected_crypto_profile: str,
    permitted_crypto_profiles: Optional[List[str]] = None,
) -> Dict[str, str]:

    crypto_profile = authority_snapshot.get("crypto_profile")
    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        return {
            "execution_state": "REFUSED_NON_BINDING",
            "reason": "missing_crypto_profile",
        }

    if not isinstance(expected_crypto_profile, str) or not expected_crypto_profile.strip():
        return {
            "execution_state": "REFUSED_NON_BINDING",
            "reason": "missing_expected_crypto_profile",
        }

    normalized_permitted = _normalize_permitted_crypto_profiles(permitted_crypto_profiles)
    if normalized_permitted is not None:
        if not normalized_permitted:
            return {
                "execution_state": "REFUSED_NON_BINDING",
                "reason": "missing_permitted_crypto_profiles",
            }

        permitted_set: Set[str] = set(normalized_permitted)
        if crypto_profile not in permitted_set:
            return {
                "execution_state": "REFUSED_NON_BINDING",
                "reason": "crypto_profile_not_permitted_by_policy",
            }

    if crypto_profile != expected_crypto_profile:
        return {
            "execution_state": "REFUSED_NON_BINDING",
            "reason": "crypto_profile_mismatch",
        }

    if crypto_profile not in SUPPORTED_CRYPTO_PROFILES:
        return {
            "execution_state": "REFUSED_NON_BINDING",
            "reason": "unsupported_crypto_profile",
        }

    expires_at = authority_snapshot.get("expires_at")

    if not isinstance(expires_at, str):
        return {
            "execution_state": "REFUSED_NON_BINDING",
            "reason": "missing_expires_at",
        }

    try:
        expiry = datetime.fromisoformat(expires_at)
    except ValueError:
        return {
            "execution_state": "REFUSED_NON_BINDING",
            "reason": "invalid_expiry_format",
        }

    now = datetime.utcnow()

    if now >= expiry:
        return {
            "execution_state": "REFUSED_NON_BINDING",
            "reason": "identity_expired",
        }

    return {
        "execution_state": "ALLOW",
        "reason": "admissible",
    }
