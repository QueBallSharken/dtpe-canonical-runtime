from typing import Dict

from core.canonical import canonical_json
from core.hashing import sha256_hex_str


def build_authority_snapshot(
    *,
    identity_id: str,
    owner_id: str,
    intent: str,
    action: str,
    expires_at: str,
    policy_version: str,
    policy_state_hash: str,
    crypto_profile: str,
) -> Dict[str, str]:

    authority_material = {
        "identity_id": identity_id,
        "owner_id": owner_id,
        "intent": intent,
        "action": action,
        "expires_at": expires_at,
        "policy_version": policy_version,
        "policy_state_hash": policy_state_hash,
        "crypto_profile": crypto_profile,
    }

    authority_canonical = canonical_json(authority_material)
    authority_hash = sha256_hex_str(authority_canonical)

    return {
        "identity_id": identity_id,
        "owner_id": owner_id,
        "intent": intent,
        "action": action,
        "expires_at": expires_at,
        "policy_version": policy_version,
        "policy_state_hash": policy_state_hash,
        "crypto_profile": crypto_profile,
        "authority_canonical": authority_canonical,
        "authority_hash": authority_hash,
    }
