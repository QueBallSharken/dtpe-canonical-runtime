import json
from datetime import UTC, datetime, timedelta

from core.paths import DATA_DIR
from core.phase4.pipeline import execute_request


LEDGER_PATH = DATA_DIR / "ledger.log"
POLICY_DIR = DATA_DIR / "policy"


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

        try:
            execute_request(
                policy_filename=policy_name,
                identity_id="alice",
                owner_id="alice",
                intent="demo.intent",
                action="execute",
                expires_at="2030-01-01T00:00:00",
            )
        except NotImplementedError:
            if LEDGER_PATH.exists():
                raise RuntimeError("ledger.log should not be created when ML-DSA signing is unimplemented")

            print("PASS: phase4 pipeline migration-window ML-DSA path correctly unimplemented")
            return 0

        raise RuntimeError("execute_request should raise NotImplementedError for ML-DSA signing path")
    finally:
        remove_file(LEDGER_PATH)
        remove_file(POLICY_DIR / policy_name)


if __name__ == "__main__":
    raise SystemExit(main())
