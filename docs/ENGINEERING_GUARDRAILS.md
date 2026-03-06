ENGINEERING GUARDRAILS

Purpose

These rules govern how contributors and automated systems should work on this repository.

This file must be read before proposing architecture or code changes.

------------------------------------------------

CORE PRINCIPLE

Execution cannot inherit authority.
Authority must resolve at the moment the system acts.

------------------------------------------------

MANDATORY INVARIANTS

1 Identity invariant

derived_public_key(private_key)
=
stored_public_key(identity_registry)

Violation must cause runtime failure.

2 Canonical serialization

All canonical JSON must use:

sort_keys=True
separators=(",", ":")
UTF-8 encoding

3 Deterministic hashing

SHA256 is used unless explicitly versioned.

4 Execution boundary

No irreversible mutation may occur before the Phase-4 admissibility decision.

5 Receipt determinism

Receipt hashes must be recomputable from canonical receipt content.

6 Replay verification

Offline verification must validate ledger and signatures using exported artifacts only.

------------------------------------------------

PROHIBITED PRACTICES

Contributors and automated systems must NOT:

• duplicate authority-bearing values without equality checks
• manually copy public keys instead of deriving them
• introduce runtime state that cannot be deterministically reconstructed
• mutate ledger data before a decision object exists
• bypass invariant checks for convenience

------------------------------------------------

DEVELOPMENT ORDER

Work must follow this implementation order:

1 identity key generator
2 identity invariant verification
3 policy snapshot loader
4 authority snapshot recomputation
5 phase-4 decision engine
6 execution boundary
7 receipt generation
8 ledger append
9 offline verifier
10 end-to-end runtime proof

------------------------------------------------

WHEN UNCERTAIN

Prefer:

determinism over convenience
recomputation over stored authority
refusal over silent acceptance

------------------------------------------------

END
