from __future__ import annotations

from typing import Any, Dict


REQUIRED_MINIMAL_RECEIPT_FIELDS = (
    "fst_profile_id",
    "fst_profile_version",
    "fst_rule_profile_id",
    "stress_scenario_id",
    "stress_category",
    "fst_result",
    "fst_findings",
    "fst_gaps",
    "fst_contradictions",
)


def validate_minimal_receipt(receipt: Dict[str, Any]) -> None:
    if not isinstance(receipt, dict):
        raise ValueError("receipt must be a dict")

    for field in REQUIRED_MINIMAL_RECEIPT_FIELDS:
        if field not in receipt:
            raise ValueError(f"receipt missing required field: {field}")

    string_fields = (
        "fst_profile_id",
        "fst_profile_version",
        "fst_rule_profile_id",
        "stress_scenario_id",
        "stress_category",
        "fst_result",
    )

    for field in string_fields:
        if not isinstance(receipt[field], str):
            raise ValueError(f"receipt field must be a string: {field}")

    list_fields = (
        "fst_findings",
        "fst_gaps",
        "fst_contradictions",
    )

    for field in list_fields:
        if not isinstance(receipt[field], list):
            raise ValueError(f"receipt field must be a list: {field}")
        if not all(isinstance(item, str) for item in receipt[field]):
            raise ValueError(f"receipt field must contain only strings: {field}")