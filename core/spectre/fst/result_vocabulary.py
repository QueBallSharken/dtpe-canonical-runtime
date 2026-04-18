from __future__ import annotations

SPECTRE_FST_PRIMARY_RESULTS = (
    "STRONG",
    "PARTIAL",
    "FAIL",
    "UNVERIFIABLE",
    "CONTRADICTION_EXPOSED",
)


def is_valid_primary_result(value: str) -> bool:
    return value in SPECTRE_FST_PRIMARY_RESULTS