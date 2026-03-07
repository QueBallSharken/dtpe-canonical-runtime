from datetime import datetime
from typing import Dict


def decide_phase4(
    *,
    authority_snapshot: Dict[str, str],
) -> Dict[str, str]:

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
