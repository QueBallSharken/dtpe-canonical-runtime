from __future__ import annotations

from typing import Dict

from core.canonical import canonical_json
from core.hashing import sha256_hex_str


_BOUNDARY_EVALUATOR_RULE_PROFILE: Dict[str, str] = {
    "evaluator_rule_profile_id": "spectre_boundary_rules_v1",
    "evaluator_rule_version": "1.0",
}


def get_boundary_evaluator_rule_profile() -> Dict[str, str]:
    return dict(_BOUNDARY_EVALUATOR_RULE_PROFILE)


def get_boundary_evaluator_rule_hash() -> str:
    return sha256_hex_str(canonical_json(get_boundary_evaluator_rule_profile()))