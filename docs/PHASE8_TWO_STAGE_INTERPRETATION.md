# PHASE 8 TWO-STAGE INTERPRETATION (LOCKED)

## STATUS

Design clarification locked.
No runtime implementation is authorized by this document.

This document clarifies the internal timing structure of Phase 8 without renumbering phases or authorizing code changes.

---

## PURPOSE

Phase 8 remains:

- Phase 8 = Decision-Space Integrity

This document clarifies that Phase 8 must be interpreted as a two-stage structure in order to preserve:

- determinism
- canonical equivalence
- replay verification
- compatibility with actual runtime signal timing
- crypto agility / PQC guardrail compliance

---

## LOCKED INTERPRETATION

Phase 8 is divided into:

- Phase 8A — Decision-Space Seed
- Phase 8B — Decision-Space Resolution

This does NOT create new numbered phases.

It is an internal timing clarification of Phase 8 only.

---

## PHASE 8A — DECISION-SPACE SEED

Phase 8A occurs:

- after canonical inputs are known
- before admissibility evaluation
- before final decision is computed

Phase 8A may contain only fields with deterministic sources available before boundary guard evaluation.

At minimum, Phase 8A is the location for candidate fields such as:

- policy_hash
- authority_hash
- execution_intent
- constraint_profile

No Phase 8A field may be inferred, approximated, or derived from future guard outputs.

---

## PHASE 8B — DECISION-SPACE RESOLUTION

Phase 8B occurs:

- after boundary guard evaluation
- before final decision materialization into receipt / ledger
- before verifier-relevant canonical structures are finalized

Phase 8B is the location for fields that depend on evaluated decision-space signals.

At minimum, Phase 8B is the location for:

- signal_profile

Additional Option B fields such as:

- visible_alternatives_profile
- risk_frame_profile

remain unresolved until their source and derivation rules are explicitly locked.

---

## SIGNAL PROFILE RULE

`signal_profile` belongs to Phase 8B, not Phase 8A.

Reason:

Current runtime produces the relevant signal inputs only during boundary evaluation, including:

- state_admissibility_result
- stability_result
- temporal_invariant_result
- frame_continuity_result

Therefore `signal_profile` cannot be treated as a pre-admissibility seed-only field.

---

## SEQUENCE_ID NOTE

Current runtime analysis shows that `sequence_id` is produced during frame continuity evaluation.

Therefore `sequence_id` is not currently proven as a valid Phase 8A field.

Until explicitly resolved, `sequence_id` remains timing-sensitive and must not be assumed available at seed construction time.

---

## CANONICAL CONSTRAINT

Any future Phase 8 implementation must preserve:

- exact verifier reconstruction
- exact replay parity
- canonical JSON equivalence
- fail-closed behavior
- crypto-agnostic structure
- PQC readiness

No two-stage interpretation may be used to justify hidden runtime-only data or non-reconstructable receipt fields.

---

## RELATION TO OTHER DOCS

This clarification is subordinate to:

- docs/CURRENT_IMPLEMENTATION_STATE.md
- docs/PHASE8_PHASE9_SPEC.md
- docs/PHASE8_DECISION_SPACE_IMPLEMENTATION_STRATEGY.md
- docs/CRYPTO_AGILITY_PQC_GUARDRAIL.md

If implementation work conflicts with these constraints, implementation must stop until the documentation is explicitly updated.

---

## FINAL RULE

Phase 8 is locked as a two-stage design interpretation:

- 8A = seed
- 8B = resolution

This interpretation preserves Option B without violating runtime reality or repository invariants.
