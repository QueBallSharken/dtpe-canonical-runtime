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
        prior_invariant_frame_hash=None,
        prior_execution_time=None,
        continuity_required=False,
    )

    assert_equal(receipt["execution_state"], "ALLOW", "receipt.execution_state")
    assert_equal(receipt["reason"], "BOUNDARY_ALLOW", "receipt.reason")

    for field in [
        "frame_continuity_result",
        "invariant_frame_hash",
        "sequence_id",
        "continuity_mode",
        "current_execution_time",
    ]:
        if field not in receipt:
            raise RuntimeError(f"receipt missing {field}")

    assert_equal(
        receipt["frame_continuity_result"]["reason"],
        "initial_frame",
        "receipt.frame_continuity_result.reason",
    )
    assert_equal(receipt["continuity_mode"], "INITIAL", "receipt.continuity_mode")
    assert_equal(
        receipt["current_execution_time"],
        "2029-01-01T00:00:00",
        "receipt.current_execution_time",
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

    for field in [
        "frame_continuity_result",
        "invariant_frame_hash",
        "sequence_id",
        "continuity_mode",
        "current_execution_time",
    ]:
        if field not in payload:
            raise RuntimeError(f"payload missing {field}")

    assert_equal(
        payload["frame_continuity_result"]["reason"],
        "initial_frame",
        "payload.frame_continuity_result.reason",
    )
    assert_equal(payload["continuity_mode"], "INITIAL", "payload.continuity_mode")
    assert_equal(
        payload["current_execution_time"],
        "2029-01-01T00:00:00",
        "payload.current_execution_time",
    )

    print("PASS: phase7 pipeline continuity path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
