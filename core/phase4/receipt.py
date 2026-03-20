from typing import Any, Dict

from core.canonical import canonical_json
from core.hashing import sha256_hex_str


def build_receipt(
    *,
    decision: Dict[str, Any],
    authority_hash: str,
    policy_state_hash: str,
    crypto_profile: str,
    authority_signature_b64: str | None = None,
    authority_canonical: str | None = None,
    authority_result: Dict[str, Any] | None = None,
    canonical_current_state: Dict[str, Any] | None = None,
    system_state: Dict[str, Any] | None = None,
    canonical_transition: Dict[str, Any] | None = None,
    execution_intent: str | None = None,
    execution_time: str | None = None,
) -> Dict[str, Any]:

    receipt_material = {
        "execution_state": decision.get("execution_state"),
        "reason": decision.get("reason"),
        "authority_hash": authority_hash,
        "policy_state_hash": policy_state_hash,
        "crypto_profile": crypto_profile,
    }

    state_admissibility_result = decision.get("state_admissibility_result")
    if state_admissibility_result is not None:
        receipt_material["state_admissibility_result"] = state_admissibility_result

    stability_result = decision.get("stability_result")
    if stability_result is not None:
        receipt_material["stability_result"] = stability_result

    temporal_invariant_result = decision.get("temporal_invariant_result")
    if temporal_invariant_result is not None:
        receipt_material["temporal_invariant_result"] = temporal_invariant_result

    if authority_result is not None:
        receipt_material["authority_result"] = authority_result

    if canonical_current_state is not None:
        receipt_material["canonical_current_state"] = canonical_current_state

    if system_state is not None:
        receipt_material["system_state"] = system_state

    if canonical_transition is not None:
        receipt_material["canonical_transition"] = canonical_transition

    if execution_intent is not None:
        receipt_material["execution_intent"] = execution_intent

    if execution_time is not None:
        receipt_material["execution_time"] = execution_time

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

    if state_admissibility_result is not None:
        receipt["state_admissibility_result"] = state_admissibility_result

    if stability_result is not None:
        receipt["stability_result"] = stability_result

    if temporal_invariant_result is not None:
        receipt["temporal_invariant_result"] = temporal_invariant_result

    if authority_result is not None:
        receipt["authority_result"] = authority_result

    if canonical_current_state is not None:
        receipt["canonical_current_state"] = canonical_current_state

    if system_state is not None:
        receipt["system_state"] = system_state

    if canonical_transition is not None:
        receipt["canonical_transition"] = canonical_transition

    if execution_intent is not None:
        receipt["execution_intent"] = execution_intent

    if execution_time is not None:
        receipt["execution_time"] = execution_time

    if authority_signature_b64 is not None:
        receipt["authority_signature_b64"] = authority_signature_b64

    if authority_canonical is not None:
        receipt["authority_canonical"] = authority_canonical

    return receipt
