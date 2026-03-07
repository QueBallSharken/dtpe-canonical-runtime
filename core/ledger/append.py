import json
from pathlib import Path
from typing import Dict, Any

from core.canonical import canonical_json
from core.hashing import sha256_hex_str
from core.paths import DATA_DIR


LEDGER_PATH = DATA_DIR / "ledger.log"


def append_ledger_record(record: Dict[str, Any]) -> Dict[str, str]:
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)

    previous_hash = "GENESIS"

    if LEDGER_PATH.exists():
        lines = [line for line in LEDGER_PATH.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
        if lines:
            last_obj = json.loads(lines[-1])
            last_hash = last_obj.get("record_hash")
            if not isinstance(last_hash, str) or not last_hash.strip():
                raise RuntimeError("Last ledger record missing record_hash")
            previous_hash = last_hash

    record_material = {
        "previous_hash": previous_hash,
        "payload": record,
    }

    record_canonical = canonical_json(record_material)
    record_hash = sha256_hex_str(record_canonical)

    ledger_record = {
        "previous_hash": previous_hash,
        "payload": record,
        "record_canonical": record_canonical,
        "record_hash": record_hash,
    }

    with LEDGER_PATH.open("a", encoding="utf-8") as f:
        f.write(canonical_json(ledger_record) + "\n")

    return {
        "previous_hash": previous_hash,
        "record_hash": record_hash,
    }
