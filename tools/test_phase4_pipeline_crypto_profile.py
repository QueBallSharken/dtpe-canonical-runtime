import json

from core.paths import DATA_DIR
from core.phase4.pipeline import execute_request


LEDGER_PATH = DATA_DIR / "ledger.log"


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def main() -> int:
    if LEDGER_PATH.exists():
        LEDGER_PATH.unlink()

    receipt = execute_request(
        policy_filename="default.json",
        identity_id="alice",
        owner_id="alice",
        intent="demo.intent",
        action="execute",
        expires_at="2030-01-01T00:00:00",
    )

    assert_equal(receipt["execution_state"], "ALLOW", "receipt.execution_state")
    assert_equal(receipt["reason"], "admissible", "receipt.reason")
    assert_equal(
        receipt["crypto_profile"],
        "ed25519+sha256+canonical_json_v1",
        "receipt.crypto_profile",
    )

    if not LEDGER_PATH.exists():
        raise RuntimeError("ledger.log was not created")

    lines = [line for line in LEDGER_PATH.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if len(lines) != 1:
        raise RuntimeError(f"expected 1 ledger line, got {len(lines)}")

    record = json.loads(lines[0])
    payload = record.get("payload")
    if not isinstance(payload, dict):
        raise RuntimeError("ledger payload missing or invalid")

    assert_equal(payload["execution_state"], "ALLOW", "payload.execution_state")
    assert_equal(payload["reason"], "admissible", "payload.reason")
    assert_equal(
        payload["crypto_profile"],
        "ed25519+sha256+canonical_json_v1",
        "payload.crypto_profile",
    )
    assert_equal(record["previous_hash"], "GENESIS", "record.previous_hash")

    LEDGER_PATH.unlink()

    print("PASS: phase4 pipeline crypto profile path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
