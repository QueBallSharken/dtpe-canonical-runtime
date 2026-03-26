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

    signal_profile = receipt.get("signal_profile")
    decision_space = receipt.get("decision_space")

    if not isinstance(signal_profile, dict):
        raise RuntimeError("receipt missing signal_profile")

    if not isinstance(decision_space, dict):
        raise RuntimeError("receipt missing decision_space")

    assert_equal(decision_space["policy_hash"], receipt["policy_state_hash"], "decision_space.policy_hash")
    assert_equal(decision_space["authority_hash"], receipt["authority_hash"], "decision_space.authority_hash")
    assert_equal(decision_space["execution_intent"], receipt["execution_intent"], "decision_space.execution_intent")
    assert_equal(decision_space["constraint_profile"], receipt["constraint_profile"], "decision_space.constraint_profile")
    assert_equal(decision_space["signal_profile"], signal_profile, "decision_space.signal_profile")
    assert_equal(decision_space["decision_space_version"], "v1", "decision_space.version")

    for forbidden_field in [
        "visible_alternatives_profile",
        "risk_frame_profile",
        "sequence_id",
    ]:
        if forbidden_field in decision_space:
            raise RuntimeError(f"decision_space contains forbidden field: {forbidden_field}")

    verify_ledger(LEDGER_PATH)

    lines = [line for line in LEDGER_PATH.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if len(lines) != 1:
        raise RuntimeError(f"expected 1 ledger line, got {len(lines)}")

    record = json.loads(lines[0])
    payload = record.get("payload")
    if not isinstance(payload, dict):
        raise RuntimeError("payload missing or invalid")

    if "signal_profile" not in payload:
        raise RuntimeError("payload missing signal_profile")

    if "decision_space" not in payload:
        raise RuntimeError("payload missing decision_space")

    assert_equal(payload["decision_space"], decision_space, "payload.decision_space")

    print("PASS: phase8 decision_space receipt and verifier path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
