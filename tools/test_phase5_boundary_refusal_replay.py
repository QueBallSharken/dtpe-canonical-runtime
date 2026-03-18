import json

from core.paths import DATA_DIR
from core.phase4.pipeline import execute_request
from tools.verify_ledger import verify_ledger


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
        intent="",
        action="execute",
        expires_at="2030-01-01T00:00:00",
    )

    assert_equal(receipt["execution_state"], "REFUSED_NON_BINDING", "receipt.execution_state")
    assert_equal(receipt["reason"], "BOUNDARY_REFUSED_NON_BINDING", "receipt.reason")

    state_result = receipt.get("state_admissibility_result")
    if not isinstance(state_result, dict):
        raise RuntimeError("receipt missing state_admissibility_result")

    stability_result = receipt.get("stability_result")
    if not isinstance(stability_result, dict):
        raise RuntimeError("receipt missing stability_result")

    assert_equal(state_result["ok"], False, "state_result.ok")
    assert_equal(state_result["reason"], "MISSING_EXECUTION_INTENT", "state_result.reason")
    assert_equal(stability_result["ok"], True, "stability_result.ok")
    assert_equal(stability_result["reason"], "SYSTEM_STABLE", "stability_result.reason")

    if not LEDGER_PATH.exists():
        raise RuntimeError("ledger.log was not created")

    verify_ledger(LEDGER_PATH)

    lines = [line for line in LEDGER_PATH.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if len(lines) != 1:
        raise RuntimeError(f"expected 1 ledger line, got {len(lines)}")

    record = json.loads(lines[0])
    payload = record.get("payload")
    if not isinstance(payload, dict):
        raise RuntimeError("payload missing or invalid")

    assert_equal(payload["execution_state"], "REFUSED_NON_BINDING", "payload.execution_state")
    assert_equal(payload["reason"], "BOUNDARY_REFUSED_NON_BINDING", "payload.reason")
    assert_equal(payload["state_admissibility_result"]["reason"], "MISSING_EXECUTION_INTENT", "payload.state.reason")
    assert_equal(payload["stability_result"]["reason"], "SYSTEM_STABLE", "payload.stability.reason")

    print("PASS: phase5 refusal replay path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
