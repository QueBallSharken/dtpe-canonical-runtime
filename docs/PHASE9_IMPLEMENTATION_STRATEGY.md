# PHASE 9 — IMPLEMENTATION STRATEGY (LOCKED)

## STATUS

- Phase 9 design is locked
- Phase 9 runtime is not implemented
- This document defines implementation order only
- This document does not itself authorize unsafe or out-of-order runtime mutation

---

## PURPOSE

This document defines the safe bounded implementation sequence for Phase 9 — Evaluator Integrity.

Phase 9 implementation must remain:

- deterministic
- canonical
- verifier-reconstructable
- replay-safe
- bounded by already committed Phase 8 structures

---

## PHASE 9 DESIGN INPUTS

Phase 9 design is currently locked across:

- docs/PHASE9_EVALUATOR_INTEGRITY_SPEC.md
- docs/PHASE9B_EVALUATOR_RULE_CONTINUITY_SPEC.md
- docs/PHASE9C_EVALUATOR_OUTPUT_DETERMINISM_SPEC.md

These documents define:

- evaluator identity and context
- evaluator rule continuity binding
- evaluator output determinism binding

Implementation must follow those documents and must not exceed them.

---

## IMPLEMENTATION GOAL

Phase 9 must prove evaluator trustworthiness from canonical recorded state.

At completion, Phase 9 must allow verifier replay to prove:

- the evaluator identity used
- the evaluator rule content used
- the evaluator output produced
- the deterministic relationship between canonical inputs and canonical evaluator output

---

## IMPLEMENTATION ORDER (LOCKED)

Phase 9 must be implemented in this exact order:

1. introduce bounded evaluator_trace construction
2. attach evaluator_trace to receipt_material and final receipt
3. attach evaluator_trace to ledger payload
4. extend verifier reconstruction for evaluator_trace
5. add bounded verifier validation for evaluator_trace fields
6. add replay-safe evaluator hash reconstruction
7. add tests for receipt parity
8. add tests for verifier parity
9. only then permit evaluator-dependent enforcement logic

No later step may be implemented before all earlier steps are complete and verified.

---

## BOUNDED IMPLEMENTATION SLICES

### Phase 9A Runtime Slice

Introduce:

- evaluator_trace
- evaluator_trace_version

This first runtime slice must remain minimal.

It must not introduce:

- rule hashing
- output hashing
- execution gating
- probabilistic evaluation

### Phase 9B Runtime Slice

Extend evaluator_trace with:

- evaluator_rule_hash
- evaluator_rule_version

This slice binds evaluator rule continuity.

It must not introduce:

- evaluator output hashing
- execution gating
- non-canonical rule identities

### Phase 9C Runtime Slice

Extend evaluator_trace with:

- evaluator_output_hash

This slice binds deterministic evaluator output.

It must not introduce:

- execution gating
- hidden runtime output context
- nondeterministic output material

---

## EXPECTED FILE TOUCH ORDER

Implementation should begin with the smallest bounded set of files.

Expected file order:

### First boundary/runtime files
- core/spectre/boundary.py
- core/phase4/receipt.py

### Then verifier
- tools/verify_ledger.py

### Then tests
- tools/test_phase9_evaluator_trace_receipt.py
- tools/test_phase9_evaluator_trace_verifier.py

Additional tests may be added only if directly required by proof.

Do not refactor unrelated files.

Do not expand file touch scope without proof.

---

## PHASE 9A RUNTIME ATTACHMENT RULE

The first implementation slice must attach evaluator_trace as a pure derived structure from already committed canonical inputs.

Allowed initial inputs include:

- authority_hash
- policy_state_hash
- execution_intent
- constraint_profile
- temporal_rule_profile
- signal_profile
- decision_space

No hidden evaluator state may be used.

No inferred evaluator identity may be used.

If evaluator identity has no deterministic committed source, implementation must stop.

---

## RECEIPT IMPACT RULE

When Phase 9 is implemented, evaluator_trace must be:

- added to receipt_material before canonical_json(...)
- copied identically to final receipt payload
- preserved identically in ledger payload

No later mutation is allowed.

If receipt and verifier structures diverge, implementation must stop.

---

## VERIFIER IMPACT RULE

Verifier must evolve together with receipt construction.

For each Phase 9 slice, verifier must:

- validate evaluator_trace exists when required
- validate field presence and types
- reconstruct any required hashes deterministically
- fail on mismatch
- remain independent of hidden runtime context

Verifier must not infer evaluator state.

Verifier must not recreate missing fields from guesswork.

---

## REPLAY RULE

Replay must remain exact at every implementation slice.

Phase 9 implementation is invalid if replay cannot prove exact evaluator consistency from payload only.

Replay-safe progression is:

- Phase 9A: identity/context parity
- Phase 9B: rule continuity parity
- Phase 9C: output determinism parity

---

## HASHING RULE

Any new Phase 9 hashes must use only:

- canonical_json(...)
- sha256_hex_str(...)

No alternative hashing scheme is authorized.

No partial or ad hoc hash inputs are authorized.

---

## PQC / CRYPTO RULE

Phase 9 must remain crypto-agnostic.

Phase 9 must not:

- branch on algorithm type
- include algorithm-specific fields
- bind evaluator integrity to cryptographic mechanism
- violate docs/CRYPTO_AGILITY_PQC_GUARDRAIL.md

Evaluator integrity validates evaluator behavior, not crypto implementation details.

---

## FAILURE CONDITIONS

Implementation must stop immediately if:

- evaluator identity lacks deterministic source
- evaluator rule content lacks deterministic source
- evaluator output lacks deterministic canonical structure
- receipt parity breaks
- verifier reconstruction breaks
- replay parity breaks
- canonical equivalence breaks
- any Phase 9 field requires hidden runtime state
- any Phase 9 slice expands beyond its locked scope

Do not patch around these failures.

Do not continue forward until the exact mismatch is proven.

---

## REQUIRED PASS DISCIPLINE

After each bounded Phase 9 slice, re-run the full existing verification baseline plus the new Phase 9 tests.

At minimum, preserve passing status for:

- python -m tools.test_phase7_frame_continuity
- python -m tools.test_phase7_boundary_frame_path
- python -m tools.test_phase7_pipeline_continuity
- python -m tools.test_phase5_boundary_refusal_replay
- python -m tools.verify_ledger
- python -m tools.test_phase5_boundary_replay_verifier

Plus any new Phase 9 tests added for that slice.

No push is allowed until the full required pass set succeeds.

---

## FIRST IMPLEMENTATION TARGET

The first runtime implementation target is:

- Phase 9A only
- minimal evaluator_trace construction
- receipt insertion
- verifier reconstruction
- parity tests

Do not begin with Phase 9B or Phase 9C.

Do not begin with enforcement logic.

Do not begin with Phase 10.

---

## NON-GOALS

This strategy document does not authorize:

- Phase 10 work
- execution gating changes
- refactoring of prior phases
- redesign of Phase 8 structures
- evaluator heuristics
- probabilistic evaluator outputs
- runtime shortcuts that bypass receipt/verifier parity

---

## FINAL RULE

Phase 9 implementation must proceed from canonical traceability outward.

Not from behavior first.
Not from enforcement first.
Not from convenience first.

Implement the smallest reconstructable evaluator structure, prove receipt/verifier parity, then extend one bounded slice at a time.
