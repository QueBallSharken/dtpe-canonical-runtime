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

The runtime is now beyond the initial identity milestone.

------------------------------------------------

NEXT IMPLEMENTATION TARGET

Step 2 — Crypto-Profile Enforcement Expansion

Goal

Strengthen the runtime from crypto-profile-aware structure to stronger
crypto-profile-aware enforcement.

The next implementation must:

1 define accepted crypto profile rules explicitly
2 refuse unsupported crypto profiles
3 refuse missing crypto profile where required
4 prepare decision semantics for profile mismatch handling
5 keep receipt and ledger evidence profile-driven
6 preserve deterministic replay behavior

Current minimum supported profile
ed25519+sha256+canonical_json_v1

------------------------------------------------

WHY THIS IS NEXT

The repository now carries crypto_profile through core runtime artifacts,
but decision semantics are not yet fully profile-enforcing.

To move honestly from PQC-aware toward PQC-capable, the runtime must
enforce crypto-profile rules, not just record them.

------------------------------------------------

EXPECTED OUTPUT

The next completed step should produce:

• deterministic refusal for missing crypto_profile
• deterministic refusal for unsupported crypto_profile
• receipt evidence carrying crypto_profile
• replayable ledger evidence carrying crypto_profile
• docs aligned with runtime semantics

------------------------------------------------

AFTER THIS STEP

Once crypto-profile enforcement is expanded, the next components are:

3 stronger policy semantics for permitted profiles
4 profile mismatch and migration-window rules
5 offline verifier profile selection logic
6 deterministic mixed-profile replay tests

------------------------------------------------

END
