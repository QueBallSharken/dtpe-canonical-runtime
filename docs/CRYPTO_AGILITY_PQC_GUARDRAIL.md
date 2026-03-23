# CRYPTO AGILITY / PQC READINESS GUARDRAIL (LOCKED)

## STATUS

Design invariant.
Applies to all current and future phases.

No runtime behavior is modified by this document.
This document constrains allowed design and implementation choices.

---

## PURPOSE

Ensure the system remains:

- cryptographically agile
- post-quantum ready
- replay-verifiable
- canonical and deterministic

Prevent hard-coding of algorithm-specific assumptions that would break future migration.

---

## CORE RULE

The system MUST NOT depend on a specific cryptographic algorithm.

All cryptographic behavior MUST be:

- profile-driven
- canonical
- replayable
- verifier-reconstructable

---

## CRYPTO PROFILE REQUIREMENT

All cryptographic operations MUST be governed by:

    crypto_profile

No phase may:

- assume RSA, ECC, or any specific algorithm
- embed algorithm-specific branching into canonical structures
- derive behavior from key shape or algorithm identity

All cryptographic behavior must flow through:

- crypto registry
- profile-based selection

---

## CANONICAL STRUCTURE RULE

Canonical structures (receipt, boundary, decision-space, etc.):

MUST NOT include:

- raw keys
- algorithm-specific fields
- non-deterministic crypto metadata

MUST include only:

- hashes
- profile identifiers
- canonical inputs

---

## HASHING RULE

All hashing MUST use the repository’s canonical discipline:

- canonical_json(...)
- sha256_hex_str(...)

No new hashing schemes may be introduced unless:

- fully specified
- verifier-reconstructable
- explicitly approved

---

## SIGNATURE RULE

Authority signing:

- MUST remain profile-driven
- MUST be verifiable offline
- MUST be replayable from recorded canonical data

No phase may:

- introduce hidden signing paths
- introduce non-replayable signatures
- bind logic to a specific signature algorithm

---

## PHASE 8 / 9 / 10 CONSTRAINT

Future phases MUST:

- remain crypto-agnostic
- use existing canonical inputs
- avoid introducing algorithm-specific dependencies
- remain fully reconstructable by verifier

Specifically:

Phase 8 (Decision-Space Integrity):
- MUST NOT depend on key type or algorithm
- MUST derive only from canonical inputs and profiles

Phase 9 (Evaluator Integrity):
- MUST validate evaluator behavior independent of crypto implementation details

Phase 10 (Execution Integrity):
- MUST bind execution to validated state, not cryptographic mechanism

---

## VERIFIER REQUIREMENT

All cryptographic behavior must be:

- reproducible from receipt payload only
- independent of runtime environment
- independent of external key state (beyond identity registry)

Verifier MUST NOT:

- infer missing crypto data
- depend on hidden runtime context
- assume algorithm-specific behavior

---

## PROHIBITED PATTERNS

The following are explicitly forbidden:

- hardcoding algorithm names into logic
- branching logic based on algorithm type
- embedding crypto decisions into canonical structures
- introducing non-deterministic crypto metadata
- adding fields that cannot be reconstructed by verifier

---

## DESIGN INTENT

The system must remain:

- migration-ready (classical → PQC → future schemes)
- stable under crypto replacement
- invariant under algorithm substitution

Crypto must be:

- replaceable
- bounded
- controlled
- observable through canonical structures

---

## FINAL RULE

Cryptography is an implementation detail.

Canonical state is the source of truth.

All phases must preserve this separation.
