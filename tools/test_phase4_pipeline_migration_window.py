import json
from datetime import UTC, datetime, timedelta

from core.paths import DATA_DIR
from core.phase4.pipeline import execute_request


LEDGER_PATH = DATA_DIR / "ledger.log"
POLICY_DIR = DATA_DIR / "policy"


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def write_policy(filename: str, obj: dict) -> None:
    path = POLICY_DIR / filename
    path.write_text(json.dumps(obj, sort_keys=True, separators=(",", ":")), encoding="utf-8")


def remove_file(path) -> None:
    if path.exists():
        path.unlink()


def main() -> int:
    policy_name = "migration_active.json"

    remove_file(LEDGER_PATH)

    now = datetime.now(UTC).replace(tzinfo=None)
    active_not_before = (now - timedelta(minutes=5)).isoformat()
    active_not_after = (now + timedelta(minutes=5)).isoformat()

    try:
        write_policy(
            policy_name,
            {
                "crypto_profile": "ml_dsa_65+sha384+canonical_json_v1",
                "migration_window": {
                    "from_crypto_profile": "ed25519+sha256+canonical_json_v1",
                    "not_after": active_not_after,
                    "not_before": active_not_before,
                    "to_crypto_profile": "ml_dsa_65+sha384+canonical_json_v1",
                },
                "permitted_crypto_profiles": [
                    "ed25519+sha256+canonical_json_v1",
                    "ml_dsa_65+sha384+canonical_json_v1",
                ],
                "policy_version": "v1",
            },
        )

        receipt = execute_request(
            policy_filename=policy_name,
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
            "ml_dsa_65+sha384+canonical_json_v1",
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
            "ml_dsa_65+sha384+canonical_json_v1",
            "payload.crypto_profile",
        )
        assert_equal(record["previous_hash"], "GENESIS", "record.previous_hash")

        print("PASS: phase4 pipeline migration-window policy path verified")
        return 0
    finally:
        remove_file(LEDGER_PATH)
        remove_file(POLICY_DIR / policy_name)


if __name__ == "__main__":
    raise SystemExit(main())
