# Temporal Execution Integrity (Execution-Boundary Constraint)

## Summary

Current integrity models distinguish between:

- detection (how contamination occurs)
- admissibility (whether a state is valid)

This document formalizes a third requirement:

**Temporal Execution Integrity** — whether admissibility holds at the exact moment execution becomes real.

---

## Definition (Normative)

A system has **Temporal Execution Integrity** if and only if:

> At the execution boundary (commit time), admissibility is re-derived against the live state and exact execution time, and that evaluation is atomically bound to the transition that becomes real.

---

## Property vs Constraint

Two distinct claims:

### Admissibility as a Property
A state was legitimately derived.

### Admissibility as a Constraint
That state must still satisfy required conditions at commit time.

A system can satisfy the property and still fail the constraint.

---

## Failure Mode

A system may pass all upstream integrity checks:

- content transmitted faithfully
- agent chain behaves consistently
- trust signals remain intact

Yet still execute from a state that is no longer valid at commit.

This is not a detection failure.

This is a **temporal binding failure**.

---

## Verification Modes

### Replay Verification (Closed-World)
- Re-executes artifact against captured inputs
- Proves consistency
- Does NOT prove completeness or validity at execution time

### Reconstruction Verification (Open-World)
- Re-derives admissibility from canonical inputs + specification
- Independent of execution artifact
- Proves boundary sufficiency and reproducibility

---

## Requirement

Execution integrity requires **reconstruction at commit**, not replay alone.

A system MUST NOT claim execution integrity if it only supports replay verification.

---

## What This Prevents

Without this constraint, systems can produce:

- a correct record of an incomplete evaluation
- a replayable artifact missing decisive inputs
- a valid prior judgment that no longer holds at execution time

All of these produce evidence — but not governance.

---

## Boundary Condition

Execution is only allowed if:

- admissibility is re-established at commit time
- evaluated against live state and execution time
- derived from canonical inputs + specification
- and atomically bound to the committed transition

---

## Reference Implementation

A working example of this constraint in practice:

https://github.com/QueBallSharken/dtpe-canonical-runtime

DTPE / SPECTRE enforces:

- execution-time admissibility recomputation
- canonical execution_time input
- atomic binding of decision → receipt → ledger
- offline independent verification

Current guarantees:

- who authorized
- what inputs were used
- what decision was made
- reproducible verification without trusting the runtime

---

## Position in OWASP Model

This constraint sits at the **execution boundary** and complements:

- detection (upstream contamination)
- admissibility (state validity)

Temporal Execution Integrity ensures:

> What cannot be re-established at execution cannot become real.
