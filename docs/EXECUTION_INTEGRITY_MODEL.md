# DTPE - EXECUTION INTEGRITY MODEL

## STATUS

- Normative model
- Repo-authoritative
- Applies to current DTPE execution-bound governance path

---

## PURPOSE

This document defines DTPE's execution integrity model.

It formalizes what DTPE proves today, what remains incomplete, and how later phases must extend integrity without violating canonical replay and verification rules.

This model is internal to DTPE.

It does not depend on external frameworks.

---

## CORE MODEL

DTPE governs execution at the boundary.

Execution is permitted only when admissibility holds at commit.

All boundary decisions must be:

- canonically defined
- deterministically evaluated
- verifier-checkable
- replay-verifiable
- independent of hidden runtime state

---

## CURRENT GUARANTEES

### 1. Execution-Bound Admissibility

DTPE permits execution only if required admissibility conditions hold at the execution boundary.

Current boundary evaluation includes:

- authority validity
- state admissibility
- system stability
- temporal admissibility
- frame continuity
- temporal continuity across linked decisions

Failure results in:

- REFUSED_NON_BINDING
- no binding state mutation

---

### 2. Temporal Enforcement

DTPE treats execution_time as canonical input.

Temporal admissibility must be evaluated from canonical inputs only.

No runtime clock may be used.

No hidden temporal state may be used.

---

### 3. Continuity Enforcement

DTPE enforces continuity through canonical frame identity and linked temporal ordering.

Continuity violations must refuse binding execution.

---

### 4. Canonical Evidence Model

DTPE produces canonical evidence through:

- canonical receipt construction
- append-only ledger records
- offline verifier replay

---

## WHAT DTPE PROVES TODAY

DTPE currently proves:

- who authorized
- what canonical inputs were used
- what boundary decision was made
- that the recorded decision can be replayed deterministically

This is replay integrity.

---

## REPLAY INTEGRITY

Replay integrity means:

- recorded canonical inputs reproduce the recorded decision
- receipt and ledger structures remain consistent
- verifier can reconstruct the same canonical artifact path without trusting runtime

Replay integrity does not by itself prove that evaluator rule identity is independently established.

---

## RECONSTRUCTION INTEGRITY

Reconstruction integrity is the stronger requirement that admissibility and evaluator behavior be independently derivable from canonical inputs and canonical evaluator identity artifacts.

Reconstruction integrity requires:

- explicit canonical evaluator rule identity
- deterministic evaluator semantics
- verifier reconstruction without inference
- no dependence on recorded decision artifacts as the sole source of truth

DTPE does not yet fully complete this layer.

---

## PHASE ALIGNMENT

### Phase 5

Provides execution-bound admissibility.

### Phase 6

Provides temporal admissibility from canonical execution time.

### Phase 7

Provides frame continuity and temporal continuity enforcement.

### Phase 8

Provides bounded decision_space and signal_profile structures plus verifier reconstruction discipline.

Phase 8 is partially implemented because only bounded, proven slices were committed.
Remaining authorized scope was intentionally deferred rather than guessed.

### Phase 9A

Provides bounded evaluator identity trace.

### Phase 9B

Must bind canonical evaluator rule identity.

### Phase 9C

Must bind deterministic evaluator output identity.

---

## CURRENT GAP

DTPE already enforces execution-bound admissibility and replay integrity.

DTPE does not yet fully prove reconstruction integrity for evaluator rules and evaluator semantics.

That remaining gap aligns with Phase 9B and Phase 9C.

---

## FORMAL DTPE STATEMENTS

What cannot be re-established at execution MUST NOT become real.

What cannot be independently reconstructed from canonical inputs MUST NOT be treated as proven.

Correct output alone does not prove correct governance.

A binding decision must be supported by canonical, reconstructable, verifier-checkable evidence.

---

## ENFORCEMENT RULE

If any required integrity layer fails:

- execution must refuse
- verification must fail
- no binding mutation may be treated as valid

---

## FINAL RULE

DTPE integrity expands from execution integrity to replay integrity to reconstruction integrity.

Later phases must strengthen proof without introducing hidden runtime dependence, inferred artifacts, or non-canonical authority.
---

## MUTATION AUTHORITY

DTPE distinguishes between:

- authorization integrity
- execution evidence
- mutation authority
- mutation-time admissibility

Mutation authority is the component that controls the state-changing primitive itself.

It is not identical to:

- the component that evaluated policy
- the component that issued a receipt
- the component that later attested or recorded what happened

DTPE's integrity model requires that mutation authority be subordinate to the admissibility predicate at the mutation boundary.

A system may be able to prove what it decided and what it later recorded, yet still fail governance if the irreversible side effect could cross the mutation boundary without the same admissibility predicate being revalidated against the governing live state.

This is the difference between:

- gate integrity
- boundary integrity

A receipt required at evaluation time is evidence.

A mutation path that is structurally impossible unless the same admissibility predicate still holds at mutation time is governance.

---

## MUTATION INTEGRITY DIRECTION

DTPE already enforces execution-bound admissibility and replay integrity.

A later integrity layer may need to make mutation authority explicit wherever the component that changes reality is not identical to the component enforcing the execution boundary.

Until that boundary is explicit, governance claims must not silently assume that execution boundary and mutation boundary are the same thing.