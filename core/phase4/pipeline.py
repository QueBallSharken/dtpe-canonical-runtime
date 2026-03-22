from typing import Any, Dict, List

from core.crypto.registry import initialize_builtin_registry
from core.policy.snapshot import load_policy_snapshot
from core.authority.snapshot import build_authority_snapshot
from core.authority.signing import sign_authority_canonical
from core.phase4.decision import decide_phase4
from core.phase4.receipt import build_receipt
from core.ledger.append import append_ledger_record
from core.spectre.boundary import evaluate_execution_boundary


def execute_request(
    *,
    policy_filename: str,
    identity_id: str,
    owner_id: str,
    intent: str,
    action: str,
    expires_at: str,
    execution_time: str,
    constraint_profile: str,
    temporal_rule_profile: str,
    prior_invariant_frame_hash: str | None = None,
    prior_execution_time: str | None = None,
    continuity_required: bool = False,
    transition_mode: str = "DISABLED",
    allowed_frame_transitions: List[Dict[str, str]] | None = None,
) -> Dict[str, Any]:

    initialize_builtin_registry()

    policy_snapshot = load_policy_snapshot(policy_filename)

    authority_snapshot = build_authority_snapshot(
        identity_id=identity_id,
        owner_id=owner_id,
        intent=intent,
        action=action,
        expires_at=expires_at,
        policy_version=policy_snapshot["policy_version"],
        policy_state_hash=policy_snapshot["policy_state_hash"],
        crypto_profile=policy_snapshot["crypto_profile"],
    )

    authority_signature_b64 = sign_authority_canonical(
        crypto_profile=policy_snapshot["crypto_profile"],
        identity_id=identity_id,
        authority_canonical=authority_snapshot["authority_canonical"],
    )

    phase4_result = decide_phase4(
        authority_snapshot=authority_snapshot,
        expected_crypto_profile=policy_snapshot["crypto_profile"],
        permitted_crypto_profiles=policy_snapshot["permitted_crypto_profiles"],
        migration_window=policy_snapshot["migration_window"],
    )

    authority_result = {
        "ok": phase4_result.get("execution_state") == "ALLOW",
        "execution_state": phase4_result.get("execution_state"),
        "reason": phase4_result.get("reason"),
    }

    canonical_transition = {
        "identity_id": identity_id,
        "owner_id": owner_id,
        "intent": intent,
        "action": action,
        "expires_at": expires_at,
    }

    boundary_result = evaluate_execution_boundary(
        authority_result=authority_result,
        canonical_current_state=authority_snapshot,
        system_state=policy_snapshot,
        canonical_transition=canonical_transition,
        canonical_policy_state_hash=policy_snapshot["policy_state_hash"],
        execution_intent=intent,
        authority_hash=authority_snapshot["authority_hash"],
        crypto_profile=policy_snapshot["crypto_profile"],
        execution_time=execution_time,
        constraint_profile=constraint_profile,
        temporal_rule_profile=temporal_rule_profile,
        prior_invariant_frame_hash=prior_invariant_frame_hash,
        prior_execution_time=prior_execution_time,
        continuity_required=continuity_required,
        transition_mode=transition_mode,
        allowed_frame_transitions=allowed_frame_transitions,
    )

    receipt = build_receipt(
        decision=boundary_result,
        authority_hash=authority_snapshot["authority_hash"],
        policy_state_hash=policy_snapshot["policy_state_hash"],
        crypto_profile=policy_snapshot["crypto_profile"],
        authority_signature_b64=authority_signature_b64,
        authority_canonical=authority_snapshot["authority_canonical"],
        authority_result=authority_result,
        canonical_current_state=authority_snapshot,
        system_state=policy_snapshot,
        canonical_transition=canonical_transition,
        execution_intent=intent,
        execution_time=execution_time,
        constraint_profile=constraint_profile,
        temporal_rule_profile=temporal_rule_profile,
    )

    append_ledger_record(receipt)

    return receipt
