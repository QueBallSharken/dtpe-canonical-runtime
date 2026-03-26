# PHASE 9C — EVALUATOR OUTPUT DETERMINISM SPEC (LOCKED)

## STATUS

- Phase 9C: DESIGN LOCKED (NOT IMPLEMENTED)

This document defines the third bounded Phase 9 slice.

No runtime implementation is authorized.

---

## PURPOSE

Phase 9C binds evaluator outputs to deterministic canonical identity.

It ensures evaluator results are:

- reproducible
- verifier-reconstructable
- identical across replay

---

## CORE INVARIANT

Evaluator output determinism must prove:

- identical inputs produce identical outputs
- evaluator output is not inferred
- evaluator output is not probabilistic

If evaluator output cannot be reproduced exactly, verification must fail.

---

## NEW CANONICAL ELEMENT

Phase 9C introduces:

- evaluator_output_hash

---

## CANONICAL STRUCTURE (EXTENSION TO PHASE 9A/9B)

evaluator_trace = {
  ...
  "evaluator_output_hash": str
}

---

## FIELD PURPOSE

- evaluator_output_hash
  - canonical hash of evaluator output

---

## DERIVATION RULES

evaluator_output_hash must be derived from:

- canonical representation of evaluator output
- canonical_json(...)
- sha256_hex_str(...)

No alternative hashing scheme is allowed.

---

## INPUT BINDING REQUIREMENT

evaluator_output_hash must be bound to:

- decision_space_hash
- signal_profile_hash
- evaluator_rule_hash

This ensures output is a deterministic function of canonical inputs.

---

## PROHIBITED CONTENT

Phase 9C MUST NOT introduce:

- probabilistic outputs
- floating-point nondeterminism
- runtime-only values
- hidden evaluator context
- partial output hashing

---

## VERIFIER REQUIREMENT (FUTURE)

Verifier must:

- reconstruct evaluator output deterministically
- compute evaluator_output_hash
- compare against recorded value
- fail on mismatch

---

## REPLAY REQUIREMENT

Replay must prove:

- evaluator_output_hash is identical
- evaluator inputs are identical
- evaluator rules are identical

---

## DEPENDENCIES

Phase 9C depends on:

- Phase 9A evaluator_trace
- Phase 9B evaluator_rule_hash
- Phase 8 decision_space and signal_profile stability

---

## NON-GOALS

Phase 9C does NOT:

- introduce execution gating
- modify decision_space
- modify signal_profile
- introduce scoring systems
- introduce approximations

---

## FINAL RULE

Evaluator output correctness is not assumed.

Evaluator output must be proven deterministic through canonical hashing and replay.
