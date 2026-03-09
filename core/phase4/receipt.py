from typing import Dict

from core.canonical import canonical_json
from core.hashing import sha256_hex_str


def build_receipt(
    *,
    decision: Dict[str, str],
    authority_hash: str,
    policy_state_hash: str,
    crypto_profile: str,
    authority_signature_b64: str | None = None,
    authority_canonical: str | None = None,
) -> Dict[str, str]:

    receipt_material = {
        "execution_state": decision.get("execution_state"),
        "reason": decision.get("reason"),
        "authority_hash": authority_hash,
        "policy_state_hash": policy_state_hash,
        "crypto_profile": crypto_profile,
    }

    if authority_signature_b64 is not None:
        receipt_material["authority_signature_b64"] = authority_signature_b64

    if authority_canonical is not None:
        receipt_material["authority_canonical"] = authority_canonical

    receipt_canonical = canonical_json(receipt_material)
    receipt_hash = sha256_hex_str(receipt_canonical)

    receipt = {
        "execution_state": receipt_material["execution_state"],
        "reason": receipt_material["reason"],
        "authority_hash": authority_hash,
        "policy_state_hash": policy_state_hash,
        "crypto_profile": crypto_profile,
        "receipt_canonical": receipt_canonical,
        "receipt_hash": receipt_hash,
    }

    if authority_signature_b64 is not None:
        receipt["authority_signature_b64"] = authority_signature_b64

    if authority_canonical is not None:
        receipt["authority_canonical"] = authority_canonical

    return receipt
