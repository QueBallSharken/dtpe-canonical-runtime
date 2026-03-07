from datetime import datetime
from typing import Dict


SUPPORTED_CRYPTO_PROFILES = {
    "ed25519+sha256+canonical_json_v1",
}


def decide_phase4(
    *,
    authority_snapshot: Dict[str, str],
) -> Dict[str, str]:

    crypto_profile = authority_snapshot.get("crypto_profile")
    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        return {
            "execution_state": "REFUSED_NON_BINDING",
            "reason": "missing_crypto_profile",
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
