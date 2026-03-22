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
        execution_time="2029-01-01T00:00:00",
        constraint_profile="baseline_constraints_v1",
        temporal_rule_profile="baseline_temporal_rules_v1",
        continuity_required=False,
        transition_mode="DISABLED",
    )

    assert_equal(receipt["execution_state"], "REFUSED_NON_BINDING", "receipt.execution_state")
    assert_equal(receipt["reason"], "BOUNDARY_REFUSED_NON_BINDING", "receipt.reason")

    state_result = receipt.get("state_admissibility_result")
    if not isinstance(state_result, dict):
        raise RuntimeError("receipt missing state_admissibility_result")

    stability_result = receipt.get("stability_result")
    if not isinstance(stability_result, dict):
        raise RuntimeError("receipt missing stability_result")

    temporal_result = receipt.get("temporal_invariant_result")
    if not isinstance(temporal_result, dict):
        raise RuntimeError("receipt missing temporal_invariant_result")

    frame_result = receipt.get("frame_continuity_result")
    if not isinstance(frame_result, dict):
        raise RuntimeError("receipt missing frame_continuity_result")

    assert_equal(state_result["ok"], False, "state_result.ok")
    assert_equal(state_result["reason"], "MISSING_EXECUTION_INTENT", "state_result.reason")
    assert_equal(stability_result["ok"], True, "stability_result.ok")
    assert_equal(stability_result["reason"], "SYSTEM_STABLE", "stability_result.reason")
    assert_equal(temporal_result["ok"], True, "temporal_result.ok")
    assert_equal(temporal_result["reason"], "VALID", "temporal_result.reason")
    assert_equal(receipt["execution_time"], "2029-01-01T00:00:00", "receipt.execution_time")

    assert_equal(frame_result["ok"], True, "frame_result.ok")
    assert_equal(frame_result["reason"], "initial_frame", "frame_result.reason")
    assert_equal(frame_result["continuity_mode"], "INITIAL", "frame_result.continuity_mode")
    assert_equal(receipt["continuity_mode"], "INITIAL", "receipt.continuity_mode")
    assert_equal(receipt["current_execution_time"], "2029-01-01T00:00:00", "receipt.current_execution_time")

    if "invariant_frame_hash" not in receipt:
        raise RuntimeError("receipt missing invariant_frame_hash")

    if "sequence_id" not in receipt:
        raise RuntimeError("receipt missing sequence_id")

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
    assert_equal(payload["temporal_invariant_result"]["reason"], "VALID", "payload.temporal.reason")
    assert_equal(payload["execution_time"], "2029-01-01T00:00:00", "payload.execution_time")
    assert_equal(payload["frame_continuity_result"]["reason"], "initial_frame", "payload.frame.reason")
    assert_equal(payload["continuity_mode"], "INITIAL", "payload.continuity_mode")
    assert_equal(payload["current_execution_time"], "2029-01-01T00:00:00", "payload.current_execution_time")

    if "invariant_frame_hash" not in payload:
        raise RuntimeError("payload missing invariant_frame_hash")

    if "sequence_id" not in payload:
        raise RuntimeError("payload missing sequence_id")

    print("PASS: phase7 refusal replay path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
