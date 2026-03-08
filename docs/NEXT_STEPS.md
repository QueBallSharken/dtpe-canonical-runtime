NEXT IMPLEMENTATION STEP

Purpose

This file defines the next implementation target so that any new contributor
or analysis thread can continue work without relying on prior conversation context.

------------------------------------------------

CURRENT STATE

This repository now contains a working DTPE runtime skeleton with:

• canonical hashing primitives
• canonical serialization rules
• identity generation and invariant verification
• canonical policy snapshot loader
• canonical authority snapshot builder
• phase-4 admissibility decision engine
• deterministic receipt generation
• deterministic ledger append
• execution pipeline
• crypto_profile bound through policy, authority, decision preconditions, receipt, and replayable ledger evidence
• deterministic refusal for missing crypto_profile
• deterministic refusal for unsupported crypto_profile
• deterministic refusal for crypto_profile mismatch
• replayable ledger evidence carrying crypto_profile
• policy snapshot support for permitted_crypto_profiles
• deterministic refusal when crypto_profile is not permitted by policy

The runtime is now beyond basic crypto-profile enforcement and beyond
policy-level permitted profile enforcement.

------------------------------------------------

NEXT IMPLEMENTATION TARGET

Step 4 — Profile Mismatch and Migration Window Rules

Goal

Introduce deterministic policy-defined migration semantics so a profile
transition can be evaluated without weakening replayability.

The next implementation must:

1 define canonical migration_window policy fields
2 validate migration_window structure in the policy snapshot
3 preserve strict mismatch refusal outside an active migration window
4 prepare decision semantics for policy-defined migration handling
5 preserve deterministic replay behavior
6 keep receipt and replayable evidence policy-driven

Current minimum supported profile
ed25519+sha256+canonical_json_v1

------------------------------------------------

WHY THIS IS NEXT

The runtime now supports permitted crypto profile sets, but still treats all
profile mismatch as immediate refusal.

To move honestly toward profile migration and future PQC-capable operation,
policy must define a deterministic migration window structure before runtime
decision logic expands.

------------------------------------------------

EXPECTED OUTPUT

The next completed step should produce:

• canonical policy support for migration_window
• validation rules for migration window structure
• docs aligned with runtime semantics
• deterministic groundwork for migration-aware mismatch handling

------------------------------------------------

AFTER THIS STEP

Once migration-window policy structure is implemented, the next components are:

5 migration-aware decision enforcement
6 offline verifier profile selection logic
7 deterministic mixed-profile replay tests

------------------------------------------------

END
