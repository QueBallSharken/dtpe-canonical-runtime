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
        execution_time="2029-01-01T00:00:00",
        constraint_profile="constraint-profile-v1",
        temporal_rule_profile="temporal-rule-profile-v1",
    )

    assert_equal(receipt["execution_state"], "ALLOW", "receipt.execution_state")
    assert_equal(receipt["reason"], "BOUNDARY_ALLOW", "receipt.reason")
    assert_equal(
        receipt["crypto_profile"],
        "ed25519+sha256+canonical_json_v1",
        "receipt.crypto_profile",
    )

    if "state_admissibility_result" not in receipt:
        raise RuntimeError("receipt missing state_admissibility_result")

    if "stability_result" not in receipt:
        raise RuntimeError("receipt missing stability_result")

    if "temporal_invariant_result" not in receipt:
        raise RuntimeError("receipt missing temporal_invariant_result")

    if "execution_time" not in receipt:
        raise RuntimeError("receipt missing execution_time")

    assert_equal(
        receipt["state_admissibility_result"]["reason"],
        "STATE_ADMISSIBLE",
        "receipt.state_admissibility_result.reason",
    )
    assert_equal(
        receipt["stability_result"]["reason"],
        "SYSTEM_STABLE",
        "receipt.stability_result.reason",
    )
    assert_equal(
        receipt["temporal_invariant_result"]["reason"],
        "VALID",
        "receipt.temporal_invariant_result.reason",
    )
    assert_equal(
        receipt["execution_time"],
        "2029-01-01T00:00:00",
        "receipt.execution_time",
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
    assert_equal(payload["reason"], "BOUNDARY_ALLOW", "payload.reason")
    assert_equal(
        payload["crypto_profile"],
        "ed25519+sha256+canonical_json_v1",
        "payload.crypto_profile",
    )

    if "state_admissibility_result" not in payload:
        raise RuntimeError("payload missing state_admissibility_result")

    if "stability_result" not in payload:
        raise RuntimeError("payload missing stability_result")

    if "temporal_invariant_result" not in payload:
        raise RuntimeError("payload missing temporal_invariant_result")

    if "execution_time" not in payload:
        raise RuntimeError("payload missing execution_time")

    assert_equal(
        payload["state_admissibility_result"]["reason"],
        "STATE_ADMISSIBLE",
        "payload.state_admissibility_result.reason",
    )
    assert_equal(
        payload["stability_result"]["reason"],
        "SYSTEM_STABLE",
        "payload.stability_result.reason",
    )
    assert_equal(
        payload["temporal_invariant_result"]["reason"],
        "VALID",
        "payload.temporal_invariant_result.reason",
    )
    assert_equal(
        payload["execution_time"],
        "2029-01-01T00:00:00",
        "payload.execution_time",
    )

    assert_equal(record["previous_hash"], "GENESIS", "record.previous_hash")

    print("PASS: phase6 pipeline temporal path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
