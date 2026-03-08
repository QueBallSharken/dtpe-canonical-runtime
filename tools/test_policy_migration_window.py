import json

from core.paths import DATA_DIR
from core.policy.snapshot import load_policy_snapshot


POLICY_DIR = DATA_DIR / "policy"


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_raises_message(fn, expected_substring: str, label: str) -> None:
    try:
        fn()
    except RuntimeError as exc:
        message = str(exc)
        if expected_substring not in message:
            raise RuntimeError(
                f"{label}: expected error containing {expected_substring!r}, got {message!r}"
            )
        return

    raise RuntimeError(f"{label}: expected RuntimeError")


def write_policy(filename: str, obj: dict) -> None:
    path = POLICY_DIR / filename
    path.write_text(json.dumps(obj, sort_keys=True, separators=(",", ":")), encoding="utf-8")


def remove_policy(filename: str) -> None:
    path = POLICY_DIR / filename
    if path.exists():
        path.unlink()


def main() -> int:
    valid_name = "migration_valid.json"
    invalid_order_name = "migration_invalid_order.json"
    invalid_profile_name = "migration_invalid_profile.json"

    try:
        write_policy(
            valid_name,
            {
                "crypto_profile": "ed25519+sha256+canonical_json_v1",
                "migration_window": {
                    "from_crypto_profile": "ed25519+sha256+canonical_json_v1",
                    "not_after": "2030-01-02T00:00:00",
                    "not_before": "2030-01-01T00:00:00",
                    "to_crypto_profile": "ml_dsa_65+sha384+canonical_json_v1",
                },
                "permitted_crypto_profiles": [
                    "ed25519+sha256+canonical_json_v1",
                    "ml_dsa_65+sha384+canonical_json_v1",
                ],
                "policy_version": "v1",
            },
        )

        write_policy(
            invalid_order_name,
            {
                "crypto_profile": "ed25519+sha256+canonical_json_v1",
                "migration_window": {
                    "from_crypto_profile": "ed25519+sha256+canonical_json_v1",
                    "not_after": "2030-01-01T00:00:00",
                    "not_before": "2030-01-02T00:00:00",
                    "to_crypto_profile": "ml_dsa_65+sha384+canonical_json_v1",
                },
                "permitted_crypto_profiles": [
                    "ed25519+sha256+canonical_json_v1",
                    "ml_dsa_65+sha384+canonical_json_v1",
                ],
                "policy_version": "v1",
            },
        )

        write_policy(
            invalid_profile_name,
            {
                "crypto_profile": "ed25519+sha256+canonical_json_v1",
                "migration_window": {
                    "from_crypto_profile": "ed25519+sha256+canonical_json_v1",
                    "not_after": "2030-01-02T00:00:00",
                    "not_before": "2030-01-01T00:00:00",
                    "to_crypto_profile": "slh_dsa_128f+sha256+canonical_json_v1",
                },
                "permitted_crypto_profiles": [
                    "ed25519+sha256+canonical_json_v1",
                    "ml_dsa_65+sha384+canonical_json_v1",
                ],
                "policy_version": "v1",
            },
        )

        valid = load_policy_snapshot(valid_name)
        migration_window = valid.get("migration_window")
        if not isinstance(migration_window, dict):
            raise RuntimeError("valid.migration_window missing or invalid")

        assert_equal(
            migration_window["from_crypto_profile"],
            "ed25519+sha256+canonical_json_v1",
            "valid.from_crypto_profile",
        )
        assert_equal(
            migration_window["to_crypto_profile"],
            "ml_dsa_65+sha384+canonical_json_v1",
            "valid.to_crypto_profile",
        )
        assert_equal(
            migration_window["not_before"],
            "2030-01-01T00:00:00",
            "valid.not_before",
        )
        assert_equal(
            migration_window["not_after"],
            "2030-01-02T00:00:00",
            "valid.not_after",
        )

        assert_raises_message(
            lambda: load_policy_snapshot(invalid_order_name),
            "not_before must be earlier than not_after",
            "invalid_order",
        )

        assert_raises_message(
            lambda: load_policy_snapshot(invalid_profile_name),
            "to_crypto_profile must be permitted by policy",
            "invalid_profile",
        )

        print("PASS: migration window policy validation verified")
        return 0
    finally:
        remove_policy(valid_name)
        remove_policy(invalid_order_name)
        remove_policy(invalid_profile_name)


if __name__ == "__main__":
    raise SystemExit(main())
