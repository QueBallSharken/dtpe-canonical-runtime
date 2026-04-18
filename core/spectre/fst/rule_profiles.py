from __future__ import annotations

from typing import Any, Dict, Tuple

from core.canonical import canonical_json
from core.hashing import sha256_hex_str


_FIRST_TARGET_RULE_PROFILE_ID = "spectre_fst_first_target_rules_v1"
_FIRST_TARGET_RULE_PROFILE_VERSION = "1.0"

_FIRST_TARGET_RULE_PROFILE: Dict[str, Any] = {
    "fst_rule_profile_id": _FIRST_TARGET_RULE_PROFILE_ID,
    "fst_rule_profile_version": _FIRST_TARGET_RULE_PROFILE_VERSION,
    "allowed_stress_categories": [
        "boundary_continuity_stress",
        "authority_continuity_stress",
        "temporal_continuity_stress",
        "state_continuity_stress",
        "path_continuity_stress",
    ],
    "allowed_primary_results": [
        "PARTIAL",
        "UNVERIFIABLE",
        "CONTRADICTION_EXPOSED",
    ],
    "single_primary_result_required": True,
    "scope_discipline_required": True,
    "determinism_required": True,
    "minimal_receipt_required": True,
    "downgrade_required_when_stronger_claim_fails": True,
}

_RULE_PROFILE_REGISTRY: Dict[Tuple[str, str], Dict[str, Any]] = {
    (_FIRST_TARGET_RULE_PROFILE_ID, _FIRST_TARGET_RULE_PROFILE_VERSION): _FIRST_TARGET_RULE_PROFILE,
}


def resolve_rule_profile(
    rule_profile_id: str,
    rule_profile_version: str,
) -> Dict[str, Any]:
    key = (rule_profile_id, rule_profile_version)
    if key not in _RULE_PROFILE_REGISTRY:
        raise ValueError(f"unknown FST rule profile: {rule_profile_id}@{rule_profile_version}")
    return dict(_RULE_PROFILE_REGISTRY[key])


def get_first_target_rule_profile() -> Dict[str, Any]:
    return resolve_rule_profile(
        rule_profile_id=_FIRST_TARGET_RULE_PROFILE_ID,
        rule_profile_version=_FIRST_TARGET_RULE_PROFILE_VERSION,
    )


def get_first_target_rule_profile_hash() -> str:
    return sha256_hex_str(canonical_json(get_first_target_rule_profile()))