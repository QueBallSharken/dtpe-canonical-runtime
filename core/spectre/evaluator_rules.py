from __future__ import annotations

from typing import Dict, Tuple

from core.canonical import canonical_json
from core.hashing import sha256_hex_str


_BOUNDARY_EVALUATOR_RULE_PROFILE_ID = "spectre_boundary_rules_v1"
_BOUNDARY_EVALUATOR_RULE_VERSION = "1.0"


_EVALUATOR_RULE_REGISTRY: Dict[Tuple[str, str], Dict[str, str]] = {
    (
        _BOUNDARY_EVALUATOR_RULE_PROFILE_ID,
        _BOUNDARY_EVALUATOR_RULE_VERSION,
    ): {
        "evaluator_rule_profile_id": _BOUNDARY_EVALUATOR_RULE_PROFILE_ID,
        "evaluator_rule_version": _BOUNDARY_EVALUATOR_RULE_VERSION,
    }
}


def resolve_evaluator_rule_profile(
    evaluator_rule_profile_id: str,
    evaluator_rule_version: str,
) -> Dict[str, str]:
    key = (evaluator_rule_profile_id, evaluator_rule_version)
    if key not in _EVALUATOR_RULE_REGISTRY:
        raise ValueError(
            f"unknown evaluator rule profile: {evaluator_rule_profile_id}@{evaluator_rule_version}"
        )
    return dict(_EVALUATOR_RULE_REGISTRY[key])


def get_evaluator_rule_hash(
    evaluator_rule_profile_id: str,
    evaluator_rule_version: str,
) -> str:
    profile = resolve_evaluator_rule_profile(
        evaluator_rule_profile_id=evaluator_rule_profile_id,
        evaluator_rule_version=evaluator_rule_version,
    )
    return sha256_hex_str(canonical_json(profile))


def get_boundary_evaluator_rule_profile() -> Dict[str, str]:
    return resolve_evaluator_rule_profile(
        evaluator_rule_profile_id=_BOUNDARY_EVALUATOR_RULE_PROFILE_ID,
        evaluator_rule_version=_BOUNDARY_EVALUATOR_RULE_VERSION,
    )


def get_boundary_evaluator_rule_hash() -> str:
    return get_evaluator_rule_hash(
        evaluator_rule_profile_id=_BOUNDARY_EVALUATOR_RULE_PROFILE_ID,
        evaluator_rule_version=_BOUNDARY_EVALUATOR_RULE_VERSION,
    )
_EVALUATOR_TRACE_VERSION = "1.0"

def get_evaluator_trace_version() -> str:
    return _EVALUATOR_TRACE_VERSION


def resolve_evaluator_trace_version(evaluator_trace_version: str) -> str:
    if evaluator_trace_version != _EVALUATOR_TRACE_VERSION:
        raise ValueError(f"unknown evaluator trace version: {evaluator_trace_version}")
    return _EVALUATOR_TRACE_VERSION