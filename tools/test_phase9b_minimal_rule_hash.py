from core.canonical import canonical_json
from core.hashing import sha256_hex_str
from core.phase4.receipt import build_receipt
from core.spectre.boundary import evaluate_execution_boundary


def main() -> int:
    authority_result = {"ok": True}

    canonical_current_state = {"state": "ready"}
    system_state = {"status": "stable"}
    canonical_transition = {
        "action": "ALLOW_TEST",
        "expires_at": "2026-12-31T23:59:59Z",
    }

    canonical_policy_state_hash = "policy_hash_test_v1"
    execution_intent = "EXECUTE_TEST"
    authority_hash = "authority_hash_test_v1"
    crypto_profile = "ed25519+sha256+canonical_json_v1"
    execution_time = "2026-01-01T00:00:00Z"
    constraint_profile = "constraint_profile_v1"
    temporal_rule_profile = "temporal_rule_profile_v1"

    decision = evaluate_execution_boundary(
        authority_result=authority_result,
        canonical_current_state=canonical_current_state,
        system_state=system_state,
        canonical_transition=canonical_transition,
        canonical_policy_state_hash=canonical_policy_state_hash,
        execution_intent=execution_intent,
        authority_hash=authority_hash,
        crypto_profile=crypto_profile,
        execution_time=execution_time,
        constraint_profile=constraint_profile,
        temporal_rule_profile=temporal_rule_profile,
        prior_invariant_frame_hash=None,
        prior_execution_time=None,
        continuity_required=False,
    )

    evaluator_trace = decision.get("evaluator_trace")
    if not isinstance(evaluator_trace, dict):
        raise AssertionError("evaluator_trace missing or invalid")

    expected_profile = {
        "evaluator_rule_profile_id": "spectre_boundary_rules_v1",
        "evaluator_rule_version": "1.0",
    }
    expected_rule_hash = sha256_hex_str(canonical_json(expected_profile))

    if evaluator_trace.get("evaluator_rule_hash") != expected_rule_hash:
        raise AssertionError("evaluator_rule_hash mismatch in boundary output")

    receipt = build_receipt(
        decision=decision,
        authority_hash=authority_hash,
        policy_state_hash=canonical_policy_state_hash,
        crypto_profile=crypto_profile,
        authority_result=authority_result,
        canonical_current_state=canonical_current_state,
        system_state=system_state,
        canonical_transition=canonical_transition,
        execution_intent=execution_intent,
        execution_time=execution_time,
        constraint_profile=constraint_profile,
        temporal_rule_profile=temporal_rule_profile,
    )

    receipt_trace = receipt.get("evaluator_trace")
    if not isinstance(receipt_trace, dict):
        raise AssertionError("receipt evaluator_trace missing or invalid")

    if receipt_trace.get("evaluator_rule_hash") != expected_rule_hash:
        raise AssertionError("evaluator_rule_hash mismatch in receipt")

    print("PASS: phase9b minimal evaluator_rule_hash verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())