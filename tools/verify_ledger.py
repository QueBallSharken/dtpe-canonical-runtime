import base64
import json
from pathlib import Path
from typing import Any, Dict, List

from core.canonical import canonical_json
from core.crypto.registry import get_crypto_verifier, initialize_builtin_registry
from core.hashing import sha256_hex_str
from core.identity.identity_registry import load_identity
from core.paths import DATA_DIR


LEDGER_PATH = DATA_DIR / "ledger.log"


def _load_lines(path: Path) -> List[str]:
    if not path.exists():
        raise RuntimeError(f"Ledger file missing: {path}")

    return [line for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def _verify_receipt_payload(payload: Dict[str, Any], index: int) -> None:
    required_fields = [
        "execution_state",
        "reason",
        "authority_hash",
        "policy_state_hash",
        "crypto_profile",
        "receipt_canonical",
        "receipt_hash",
    ]

    for field in required_fields:
        if field not in payload:
            raise RuntimeError(f"Ledger record {index}: payload missing {field}")

    receipt_material = {
        "execution_state": payload.get("execution_state"),
        "reason": payload.get("reason"),
        "authority_hash": payload.get("authority_hash"),
        "policy_state_hash": payload.get("policy_state_hash"),
        "crypto_profile": payload.get("crypto_profile"),
    }

    authority_signature_b64 = payload.get("authority_signature_b64")
    if authority_signature_b64 is not None:
        receipt_material["authority_signature_b64"] = authority_signature_b64

    authority_canonical = payload.get("authority_canonical")
    if authority_canonical is not None:
        receipt_material["authority_canonical"] = authority_canonical

    expected_receipt_canonical = canonical_json(receipt_material)
    if payload["receipt_canonical"] != expected_receipt_canonical:
        raise RuntimeError(f"Ledger record {index}: receipt_canonical mismatch")

    expected_receipt_hash = sha256_hex_str(expected_receipt_canonical)
    if payload["receipt_hash"] != expected_receipt_hash:
        raise RuntimeError(f"Ledger record {index}: receipt_hash mismatch")


def _verify_authority_signature_if_present(payload: Dict[str, Any], index: int) -> None:
    authority_signature_b64 = payload.get("authority_signature_b64")
    if authority_signature_b64 is None:
        return

    authority_canonical = payload.get("authority_canonical")
    if not isinstance(authority_canonical, str) or not authority_canonical:
        raise RuntimeError(
            f"Ledger record {index}: authority signature present but authority_canonical "
            f"is missing or invalid"
        )

    try:
        authority_obj = json.loads(authority_canonical)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Ledger record {index}: authority_canonical is not valid JSON: {exc}"
        ) from None

    if not isinstance(authority_obj, dict):
        raise RuntimeError(
            f"Ledger record {index}: authority_canonical must decode to a JSON object"
        )

    identity_id = authority_obj.get("identity_id")
    if not isinstance(identity_id, str) or not identity_id.strip():
        raise RuntimeError(
            f"Ledger record {index}: authority_canonical missing non-empty identity_id"
        )

    crypto_profile = payload.get("crypto_profile")
    if not isinstance(crypto_profile, str) or not crypto_profile.strip():
        raise RuntimeError(f"Ledger record {index}: crypto_profile missing or invalid")

    identity = load_identity(identity_id)

    public_key_b64 = identity.get("public_key_b64")
    if not isinstance(public_key_b64, str) or not public_key_b64.strip():
        raise RuntimeError(f"Ledger record {index}: identity missing public_key_b64")

    public_key_bytes = base64.b64decode(public_key_b64, validate=True)
    signature_bytes = base64.b64decode(authority_signature_b64, validate=True)
    message_bytes = authority_canonical.encode("utf-8")

    verifier = get_crypto_verifier(crypto_profile)
    verified = verifier(public_key_bytes, message_bytes, signature_bytes)

    if not verified:
        raise RuntimeError(f"Ledger record {index}: authority signature verification failed")


def verify_ledger(path: Path) -> int:
    initialize_builtin_registry()

    lines = _load_lines(path)

    expected_previous_hash = "GENESIS"

    for index, line in enumerate(lines, start=1):
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Ledger record {index}: invalid JSON: {exc}") from None

        if not isinstance(obj, dict):
            raise RuntimeError(f"Ledger record {index}: record must be a JSON object")

        previous_hash = obj.get("previous_hash")
        payload = obj.get("payload")
        record_canonical = obj.get("record_canonical")
        record_hash = obj.get("record_hash")

        if previous_hash != expected_previous_hash:
            raise RuntimeError(
                f"Ledger record {index}: previous_hash mismatch: expected "
                f"{expected_previous_hash!r}, got {previous_hash!r}"
            )

        if not isinstance(payload, dict):
            raise RuntimeError(f"Ledger record {index}: payload missing or invalid")

        if not isinstance(record_canonical, str) or not record_canonical:
            raise RuntimeError(f"Ledger record {index}: record_canonical missing or invalid")

        if not isinstance(record_hash, str) or not record_hash:
            raise RuntimeError(f"Ledger record {index}: record_hash missing or invalid")

        expected_record_material = {
            "previous_hash": previous_hash,
            "payload": payload,
        }
        expected_record_canonical = canonical_json(expected_record_material)

        if record_canonical != expected_record_canonical:
            raise RuntimeError(f"Ledger record {index}: record_canonical mismatch")

        expected_record_hash = sha256_hex_str(expected_record_canonical)
        if record_hash != expected_record_hash:
            raise RuntimeError(f"Ledger record {index}: record_hash mismatch")

        _verify_receipt_payload(payload, index)
        _verify_authority_signature_if_present(payload, index)

        expected_previous_hash = record_hash

    print(f"PASS: verified {len(lines)} ledger record(s)")
    return 0


def main() -> int:
    return verify_ledger(LEDGER_PATH)


if __name__ == "__main__":
    raise SystemExit(main())
