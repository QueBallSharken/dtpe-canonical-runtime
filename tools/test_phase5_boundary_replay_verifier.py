import json

from core.paths import DATA_DIR
from tools.verify_ledger import verify_ledger


LEDGER_PATH = DATA_DIR / "ledger.log"


def main() -> int:
    if not LEDGER_PATH.exists():
        raise RuntimeError("ledger.log missing before replay verifier test")

    verify_ledger(LEDGER_PATH)

    lines = [line for line in LEDGER_PATH.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if len(lines) != 1:
        raise RuntimeError(f"expected 1 ledger line, got {len(lines)}")

    record = json.loads(lines[0])
    payload = record.get("payload")
    if not isinstance(payload, dict):
        raise RuntimeError("payload missing or invalid")

    required_replay_fields = [
        "authority_result",
        "canonical_current_state",
        "system_state",
        "canonical_transition",
        "execution_intent",
        "execution_time",
        "temporal_invariant_result",
        "frame_continuity_result",
        "invariant_frame_hash",
        "sequence_id",
        "continuity_mode",
        "current_execution_time",
    ]
    for field in required_replay_fields:
        if field not in payload:
            raise RuntimeError(f"payload missing replay field: {field}")

    print("PASS: phase7 boundary replay verifier path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
