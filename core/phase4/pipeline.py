from typing import Dict

from core.policy.snapshot import load_policy_snapshot
from core.authority.snapshot import build_authority_snapshot
from core.phase4.decision import decide_phase4
from core.phase4.receipt import build_receipt
from core.ledger.append import append_ledger_record


def execute_request(
    *,
    policy_filename: str,
    identity_id: str,
    owner_id: str,
    intent: str,
    action: str,
    expires_at: str,
) -> Dict[str, str]:

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

    decision = decide_phase4(
        authority_snapshot=authority_snapshot,
        expected_crypto_profile=policy_snapshot["crypto_profile"],
    )

    receipt = build_receipt(
        decision=decision,
        authority_hash=authority_snapshot["authority_hash"],
        policy_state_hash=policy_snapshot["policy_state_hash"],
        crypto_profile=policy_snapshot["crypto_profile"],
    )

    append_ledger_record(receipt)

    return receipt
