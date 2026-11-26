"""Pinned SPECTRE-FST nine-field receipt profile."""
from .offline_input import Unsupported, require
from .rule_profiles import get_first_target_rule_profile
from .scenarios import resolve_scenario

PROFILE = "spectre_fst_minimal_v1"
VERSION = "1.0"
RULE = "spectre_fst_first_target_rules_v1"
RESULTS = frozenset(get_first_target_rule_profile()["allowed_primary_results"])
STRINGS = {
    "fst_profile_id", "fst_profile_version", "fst_rule_profile_id",
    "stress_scenario_id", "stress_category", "fst_result",
}
ARRAYS = {"fst_findings", "fst_gaps", "fst_contradictions"}


def check(receipt):
    if {"fst_suite_id", "fst_aggregate_id", "execution_state", "schema_id"} & receipt.keys():
        raise Unsupported("Expected a bare SPECTRE-FST receipt.")
    require((STRINGS | ARRAYS) <= receipt.keys(), "Required FST fields are missing.")
    for key in sorted(STRINGS):
        require(isinstance(receipt[key], str), f"{key} must be a string.")
    for key in sorted(ARRAYS):
        items = receipt[key]
        require(isinstance(items, list) and all(isinstance(item, str) for item in items),
                f"{key} must be an array of strings.")
    if receipt.keys() != STRINGS | ARRAYS:
        raise Unsupported("Receipt extensions are outside the pinned profile.")
    if (receipt["fst_profile_id"], receipt["fst_profile_version"],
            receipt["fst_rule_profile_id"]) != (PROFILE, VERSION, RULE):
        raise Unsupported("Unknown FST profile or version.")
    if receipt["fst_result"] not in RESULTS:
        raise Unsupported("Result is outside the pinned FST vocabulary.")
    try:
        resolve_scenario(receipt["stress_scenario_id"], receipt["stress_category"])
    except ValueError as error:
        raise Unsupported("Unknown FST scenario and category pair.") from error


def facts(raw_digest, expected, native_digest=None):
    return {
        "raw_native_sha256": raw_digest,
        "expected_raw_native_sha256": expected,
        "expected_raw_digest_check": (
            "NOT_CHECKED" if expected is None or raw_digest is None
            else "MATCH" if raw_digest == expected else "MISMATCH"
        ),
        "native_canonical_sha256": native_digest,
    }
