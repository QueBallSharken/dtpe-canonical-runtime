# PHASE 9B — EVALUATOR RULE CONTINUITY SPEC (LOCKED)

## STATUS

- Phase 9B: DESIGN LOCKED (NOT IMPLEMENTED)

This document defines the second bounded Phase 9 slice.

No runtime implementation is authorized.

---

## PURPOSE

Phase 9B binds evaluator rule content to a deterministic canonical identity.

It ensures evaluator rule behavior is:

- stable across time
- detectable when changed
- reconstructable during replay

---

## CORE INVARIANT

Evaluator rule continuity must prove:

- evaluator rule content is identical between execution and replay
- evaluator rule identity is not inferred
- evaluator rule drift is detectable

If evaluator rule content cannot be reconstructed exactly, verification must fail.

---

## NEW CANONICAL ELEMENTS

Phase 9B introduces:

- evaluator_rule_hash
- evaluator_rule_version

---

## CANONICAL STRUCTURE (EXTENSION TO PHASE 9A)

evaluator_trace = {
  ...
  "evaluator_rule_profile": str,
  "evaluator_rule_hash": str,
  "evaluator_rule_version": str
}

---

## FIELD PURPOSES

- evaluator_rule_hash
  - canonical hash of evaluator rule content

- evaluator_rule_version
  - version identifier for evaluator rule set

---

## DERIVATION RULES

evaluator_rule_hash must be derived from:

- canonical representation of evaluator rule set
- canonical_json(...)
- sha256_hex_str(...)

No alternative hashing scheme is allowed.

---

## PROHIBITED CONTENT

Phase 9B MUST NOT introduce:

- runtime-generated rule representations
- partial rule definitions
- inferred rule content
- opaque rule identifiers without canonical backing

---

## VERIFIER REQUIREMENT (FUTURE)

Verifier must:

- reconstruct evaluator_rule_hash deterministically
- compare against recorded evaluator_rule_hash
- fail on mismatch

---

## REPLAY REQUIREMENT

Replay must prove:

- evaluator_rule_hash is identical
- evaluator_rule_version is identical
- evaluator behavior is reproducible

---

## DEPENDENCIES

Phase 9B depends on:

- Phase 9A evaluator_trace
- canonical hashing discipline
- Phase 8 decision_space stability

---

## NON-GOALS

Phase 9B does NOT:

- introduce execution gating
- redefine evaluator_trace
- modify Phase 8 structures
- introduce probabilistic evaluation

---

## FINAL RULE

Evaluator rule identity is not assumed.

Evaluator rule identity must be proven through canonical, deterministic hashing.
