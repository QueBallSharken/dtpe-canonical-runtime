# PHASE 8 — DECISION SPACE COMPOSITION SPEC (LOCKED)

## STATUS

Design specification locked.
No runtime implementation is authorized by this document.

This document defines the canonical composition rules for:

    decision_space

within the Phase 8 two-stage model.

---

## PURPOSE

`decision_space` is the canonical Phase 8 structure representing the bounded, deterministic decision context used for decision-space integrity.

---

## PHASE OWNERSHIP

Phase 8 is composed of:

- Phase 8A — Seed (pre-admissibility)
- Phase 8B — Resolution (post-signal, pre-finalization)

`decision_space` is only valid after Phase 8B completes.

---

## CANONICAL STRUCTURE (CURRENT AUTHORIZED)

{
  "policy_hash": str,
  "authority_hash": str,
  "execution_intent": str,
  "constraint_profile": str,
  "signal_profile": { ... },
  "decision_space_version": str
}

---

## INCLUDED FIELDS

Allowed:

- policy_hash
- authority_hash
- execution_intent
- constraint_profile
- signal_profile
- decision_space_version

---

## EXCLUDED FIELDS (LOCKED)

MUST NOT appear:

- visible_alternatives_profile
- risk_frame_profile
- sequence_id

---

## SOURCE RULES

- policy_hash ← canonical_policy_state_hash
- authority_hash ← authority_hash
- execution_intent ← execution_intent
- constraint_profile ← constraint_profile
- signal_profile ← Phase 8B signal_profile
- decision_space_version ← fixed constant ("v1")

---

## COMPOSITION RULE

`decision_space` MUST:

- be built after signal_profile exists
- be complete before entering receipt_material
- not exist as a partial canonical object

---

## RECEIPT RULE

If added to runtime:

- must be included in receipt_material before canonical_json
- must be identical during replay
- must not include deferred fields

---

## VERIFIER RULE

Verifier must:

- reconstruct decision_space exactly
- include it in canonical_json
- fail on mismatch

Verifier must NOT:

- infer values
- regenerate signals
- depend on runtime state

---

## PQC RULE

decision_space MUST:

- remain crypto-agnostic
- not include algorithm-specific data
- not include keys or crypto internals

---

## FAILURE CONDITIONS

STOP if:

- any field lacks deterministic source
- signal_profile mismatch occurs
- deferred fields are required
- canonical equivalence breaks

---

## FINAL RULE

decision_space is currently limited to:

- seed inputs
- signal_profile
- explicit versioning

No additional fields are authorized.
