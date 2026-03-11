DTPE Receipt Schema V2

Purpose

This document defines the Phase-5 receipt extension required for
boundary-governed execution decisions.

Goal

Allow independent verifiers to recompute boundary decisions without
trusting the runtime.

Receipt fields

execution_state
reason
authority_hash
policy_state_hash
crypto_profile
state_admissibility_result
stability_result
receipt_canonical
receipt_hash

Phase-6 extension

temporal_invariant_result

Requirements

- receipt fields must be canonical
- receipt fields must be sufficient for offline replay
- receipt schema version must be explicit
- verifier logic must use only canonical recorded inputs

Design rule

If a verifier cannot replay it, the receipt is incomplete.

END OF FILE
