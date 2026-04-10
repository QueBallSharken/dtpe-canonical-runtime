# PHASE 9 - EVALUATOR INTEGRITY SPEC (LOCKED)

## STATUS

- Phase 9: BOUNDED EVALUATOR-TRACE-RELATED RUNTIME SURFACE IS PRESENT
- The committed runtime already includes bounded evaluator_trace-related boundary, receipt, verifier, and test surface
- Broader Phase 9 remains unimplemented and unauthorized

This document must describe the committed bounded slice conservatively.
It must not broaden Phase 9 by implication.

---

## PURPOSE

Phase 9 ensures the evaluator itself is structurally trustworthy.

In the current committed repository state, the bounded Phase 9 slice is limited to replay-verifiable evaluator_trace evidence.

Phase 9 does not decide whether a request is admissible.
Phase 9 binds evaluator identity, bounded rule identity, and canonical evaluation context to recorded state.

---

## CORE INVARIANT

Evaluator integrity must prove:

- evaluator identity consistency
- bounded evaluator rule identity continuity
- canonical evaluation context binding
- replay fidelity for the currently committed bounded slice

If evaluator-trace evidence cannot be reconstructed from canonical recorded state, verification must fail.

---

## CURRENT BOUNDED SLICE

The current committed Phase 9 slice is:

- evaluator_trace
- evaluator_rule_profile
- evaluator_rule_hash
- decision_space_hash
- signal_profile_hash
- policy_hash
- authority_hash
- execution_intent
- constraint_profile
- temporal_rule_profile
- evaluator_trace_version

This slice is already present in the committed runtime surface.

No broader Phase 9 structure is authorized by this document.

---

## CURRENT COMMITTED CANONICAL STRUCTURE

evaluator_trace = {
  "evaluator_id": str,
  "evaluator_rule_profile": {
    "evaluator_rule_profile_id": str,
    "evaluator_rule_version": str
  },
  "evaluator_rule_hash": str,
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

## CURRENT SOURCE RULES

The current committed bounded slice must remain:

- deterministic
- canonical
- replay-verifiable
- free of hidden runtime state
- free of inferred fields

Current committed source mapping is bounded to:

- evaluator_id
  - fixed canonical identifier for the current evaluator surface

- evaluator_rule_profile
  - fixed canonical evaluator rule profile object for the current bounded evaluator surface

- evaluator_rule_hash
  - deterministic SHA-256 over canonical_json(evaluator_rule_profile)

- decision_space_hash
  - deterministic SHA-256 over canonical_json(decision_space)

- signal_profile_hash
  - deterministic SHA-256 over canonical_json(signal_profile)

- policy_hash
  - canonical policy state hash already present in the runtime boundary inputs

- authority_hash
  - canonical authority hash already present in the runtime boundary inputs

- execution_intent
  - canonical execution intent already present in the runtime boundary inputs

- constraint_profile
  - canonical constraint profile already present in the runtime boundary inputs

- temporal_rule_profile
  - canonical temporal rule profile already present in the runtime boundary inputs

- evaluator_trace_version
  - fixed version string for the bounded slice

No additional Phase 9 source fields are authorized here.

---

## CURRENT RECEIPT / LEDGER / VERIFIER STATE

The current committed runtime already includes all of the following:

- evaluator_trace construction in boundary
- evaluator_trace inclusion in receipt_material before canonical_json
- evaluator_trace inclusion in final receipt payload
- ledger payload carrying evaluator_trace through receipt append
- verifier validation for evaluator_rule_profile shape
- verifier validation for evaluator_rule_hash
- verifier validation for decision_space_hash
- verifier validation for signal_profile_hash
- verifier validation for policy_hash equality
- verifier validation for authority_hash equality
- verifier validation for execution_intent equality
- verifier validation for constraint_profile equality
- verifier validation for temporal_rule_profile equality
- committed evaluator-trace-related test coverage

Accordingly, this repository must not be described as having no Phase 9 runtime, receipt, verifier, or replay fields.

---

## DEFERRED / NOT IMPLEMENTED IN THE CURRENT BOUNDED SLICE

No additional contextual fields remain deferred inside the current bounded Phase 9 evaluator_trace slice.

Any further Phase 9 expansion requires a new explicit bounded authorization.

---

## PROHIBITED CONTENT

The current bounded evaluator_trace MUST NOT include:

- raw keys
- algorithm-specific crypto metadata
- hidden runtime environment identifiers
- memory addresses
- process identifiers
- inferred fallback values
- probabilistic scores
- opaque blobs that verifier cannot reconstruct
- any new field not explicitly authorized by this document

---

## REPLAY RULE

Replay for the current bounded slice must remain exact.

Verifier must be able to confirm:

- the same evaluator_id is reconstructed
- the same evaluator_rule_profile is reconstructed
- the same evaluator_rule_hash is reconstructed
- the same decision_space_hash is reconstructed
- the same signal_profile_hash is reconstructed
- the same policy_hash is reconstructed
- the same authority_hash is reconstructed
- the same execution_intent is reconstructed
- the same constraint_profile is reconstructed
- the same temporal_rule_profile is reconstructed
- the same evaluator_trace_version is reconstructed

If replay cannot prove evaluator-trace consistency exactly, verification must fail.

---

## NON-GOALS

Phase 9 does NOT currently authorize:

- redefining decision_space
- redefining signal_profile
- introducing execution gating
- replacing Phase 10
- introducing alternatives analysis
- introducing risk scoring
- introducing new authority derivation
- mutating prior-phase results
- broadening evaluator_trace beyond the committed bounded slice

---

## DEPENDENCIES

The current bounded Phase 9 slice depends on:

- committed earlier-phase canonical state
- exact canonical hashing discipline
- receipt-safe construction
- ledger-safe persistence
- verifier-safe reconstruction
- crypto agility / PQC guardrail compliance

Broader Phase 9 work must not proceed until documentation remains consistent with the current committed bounded slice.

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

Implementation or documentation alignment must stop if:

- evaluator identity has no deterministic canonical source
- evaluator_rule_profile cannot be reconstructed exactly
- evaluator_rule_hash cannot be reconstructed exactly
- decision_space_hash cannot be reconstructed exactly
- signal_profile_hash cannot be reconstructed exactly
- policy_hash cannot be reconstructed exactly
- authority_hash cannot be reconstructed exactly
- execution_intent cannot be reconstructed exactly
- constraint_profile cannot be reconstructed exactly
- temporal_rule_profile cannot be reconstructed exactly
- replay parity would diverge
- any broader Phase 9 field requires hidden runtime state
- any broader Phase 9 field is treated as already implemented without committed runtime proof
- any Phase 9 change violates the PQC guardrail

---

## IMPLEMENTATION RULE

This document authorizes no broader runtime change beyond the already committed bounded slice.

The current repository-authoritative rule is:

- keep the bounded evaluator_trace-related slice explicit
- do not describe Phase 9 as absent
- do not broaden Phase 9 by implication
- do not start additional Phase 9 implementation planning from contradictory documentation

---

## FINAL RULE

Evaluator integrity is not assumed from correct output.

In the current repository state, the committed bounded evaluator_trace slice is present and replay-verifiable.
Broader evaluator integrity remains explicitly deferred until separately authorized.