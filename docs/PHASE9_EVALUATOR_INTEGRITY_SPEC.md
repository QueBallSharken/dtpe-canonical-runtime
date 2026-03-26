# PHASE 9 — EVALUATOR INTEGRITY SPEC (LOCKED)

## STATUS

- Phase 9: DESIGN LOCKED (NOT IMPLEMENTED)

Repository runtime does not yet implement Phase 9.

No runtime fields, receipt fields, verifier fields, or replay fields currently exist for Phase 9.

This document defines the first bounded Phase 9 design lock.

---

## PURPOSE

Phase 9 ensures the evaluator itself is structurally trustworthy.

Phase 9 does not decide whether a request is admissible.

Phase 9 verifies that the component producing evaluation results is itself consistent, replayable, and bound to canonical state.

---

## CORE INVARIANT

Evaluator integrity must prove:

- evaluator identity consistency
- evaluator rule continuity
- evaluator replay fidelity

If evaluator integrity cannot be proven from canonical recorded state, execution MUST resolve as non-binding.

---

## PHASE BOUNDARY

Phase 9 follows Phase 8.

Phase 9 depends on already committed canonical state from earlier phases, including:

- authority_hash
- policy_state_hash
- execution_intent
- constraint_profile
- temporal_rule_profile
- signal_profile
- decision_space
- frame continuity state where present

Phase 9 does not redefine those structures.

Phase 9 binds evaluator trustworthiness to them.

---

## FIRST BOUNDED SLICE

The first bounded Phase 9 slice is:

- evaluator_trace
- evaluator_trace_version

This slice is documentation-only.

No implementation is authorized by this document.

---

## EVALUATOR TRACE PURPOSE

evaluator_trace is the canonical structure that records the evaluator identity and rule context used to produce an evaluation result.

It exists to make evaluator behavior reconstructable and verifier-checkable.

It must not contain hidden runtime state.

It must not contain inferred values.

---

## CANONICAL STRUCTURE (FIRST BOUNDED SLICE)

evaluator_trace = {
  "evaluator_id": str,
  "evaluator_rule_profile": str,
  "decision_space_hash": str,
  "signal_profile_hash": str,
  "policy_hash": str,
  "authority_hash": str,
  "execution_intent": str,
  "constraint_profile": str,
  "temporal_rule_profile": str,
  "evaluator_trace_version": str
}

---

## FIELD PURPOSES

- evaluator_id
  - canonical identifier for the evaluator configuration or evaluator profile in use

- evaluator_rule_profile
  - canonical identifier for the evaluator rule set being applied

- decision_space_hash
  - canonical hash of the already-built decision_space structure

- signal_profile_hash
  - canonical hash of the already-built signal_profile structure

- policy_hash
  - canonical policy state hash already present in the system

- authority_hash
  - canonical authority hash already present in the system

- execution_intent
  - execution intent already present in canonical state

- constraint_profile
  - existing constraint profile already present in canonical state

- temporal_rule_profile
  - existing temporal rule profile already present in canonical state

- evaluator_trace_version
  - fixed version string for the bounded Phase 9 structure

---

## DERIVATION RULES

Phase 9 fields must be derived only from canonical state already present or from locked evaluator identifiers explicitly defined by committed documentation.

Allowed derivations:

- decision_space_hash from canonical_json(decision_space) plus sha256_hex_str(...)
- signal_profile_hash from canonical_json(signal_profile) plus sha256_hex_str(...)

No new hashing scheme is authorized.

No hidden runtime-only evaluator metadata is authorized.

No probabilistic evaluator scoring is authorized.

---

## PROHIBITED CONTENT

evaluator_trace MUST NOT include:

- raw keys
- algorithm-specific crypto metadata
- timestamps not already required by earlier committed phases
- hidden runtime environment identifiers
- memory addresses
- process identifiers
- inferred fallback values
- probabilistic scores
- opaque blobs that verifier cannot reconstruct

---

## RECEIPT ATTACHMENT RULE

When Phase 9 is eventually implemented, evaluator_trace may be added to receipt_material only if:

- it is complete before canonical_json(receipt_material)
- it is identical in final receipt payload
- it is identical in ledger payload
- verifier can reconstruct it exactly
- replay parity remains exact

Until implementation is authorized, no runtime mutation is permitted.

---

## VERIFIER RULE

When Phase 9 is eventually implemented, verifier must:

1. read evaluator_trace from payload
2. validate required fields and types
3. reconstruct decision_space_hash deterministically
4. reconstruct signal_profile_hash deterministically
5. confirm evaluator_trace matches exactly
6. fail on any mismatch

Verifier MUST NOT:

- infer evaluator identity
- infer evaluator rules
- invent missing fields
- use hidden runtime context
- depend on algorithm-specific crypto assumptions

---

## REPLAY RULE

Phase 9 replay must remain exact.

If evaluator_trace is later introduced, replay must prove that:

- the same canonical evaluator context is reconstructed
- the same decision_space_hash is reconstructed
- the same signal_profile_hash is reconstructed
- the same evaluator rule profile is observed

If replay cannot prove evaluator consistency exactly, verification must fail.

---

## NON-GOALS

Phase 9 does NOT:

- redefine decision_space
- redefine signal_profile
- introduce execution gating
- replace Phase 10
- introduce alternatives analysis
- introduce risk scoring
- introduce new authority derivation
- mutate prior-phase results

---

## DEPENDENCIES

Phase 9 requires:

- committed and internally consistent Phase 8 documentation
- committed Phase 8 runtime structures
- committed Phase 8 verifier reconstruction
- exact canonical hashing discipline
- crypto agility / PQC guardrail compliance

---

## PQC / CRYPTO GUARDRAIL

Phase 9 must remain:

- crypto-agnostic
- profile-driven where cryptographic behavior exists
- reconstructable by verifier
- independent of algorithm-specific branching

Evaluator integrity validates evaluator behavior, not cryptographic mechanism.

---

## FAILURE CONDITIONS

Implementation must stop if:

- evaluator identity has no deterministic canonical source
- evaluator_rule_profile has no deterministic canonical source
- decision_space_hash cannot be reconstructed exactly
- signal_profile_hash cannot be reconstructed exactly
- replay parity would diverge
- any Phase 9 field requires hidden runtime state
- any Phase 9 field violates the PQC guardrail

---

## IMPLEMENTATION STATUS

This document authorizes no runtime change.

This document locks only the first bounded Phase 9 design slice.

Any future implementation must be minimal, receipt-safe, verifier-safe, and replay-safe.

---

## FINAL RULE

Evaluator integrity is not assumed from correct output.

Evaluator integrity must be proven from canonical, reconstructable, verifier-checkable state.
