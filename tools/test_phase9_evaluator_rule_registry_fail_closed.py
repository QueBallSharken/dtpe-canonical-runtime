import json

from core.paths import DATA_DIR
from core.phase4.pipeline import execute_request
from tools.verify_ledger import _verify_receipt_payload


LEDGER_PATH = DATA_DIR / "ledger.log"


def main() -> int:
    if LEDGER_PATH.exists():
        LEDGER_PATH.unlink()

    execute_request(
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

    lines = [line for line in LEDGER_PATH.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if len(lines) != 1:
        raise RuntimeError(f"expected 1 ledger line, got {len(lines)}")

    record = json.loads(lines[0])
    payload = record.get("payload")
    if not isinstance(payload, dict):
        raise RuntimeError("payload missing or invalid")

    evaluator_trace = payload.get("evaluator_trace")
    if not isinstance(evaluator_trace, dict):
        raise RuntimeError("payload evaluator_trace missing or invalid")

    evaluator_rule_profile = evaluator_trace.get("evaluator_rule_profile")
    if not isinstance(evaluator_rule_profile, dict):
        raise RuntimeError("payload evaluator_rule_profile missing or invalid")

    evaluator_rule_profile["evaluator_rule_profile_id"] = "spectre_boundary_rules_UNKNOWN"

    try:
        _verify_receipt_payload(payload, 1)
    except RuntimeError as exc:
        message = str(exc)
        if "unknown evaluator rule profile" not in message:
            raise RuntimeError(f"unexpected verifier failure: {message}")
        print("PASS: phase9 evaluator rule registry fail-closed verified")
        return 0

    raise RuntimeError("expected verifier to reject unknown evaluator rule profile")


if __name__ == "__main__":
    raise SystemExit(main())