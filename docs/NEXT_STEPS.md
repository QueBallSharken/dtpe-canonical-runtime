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

The runtime is now beyond the initial identity milestone and beyond
basic crypto-profile enforcement expansion.

------------------------------------------------

NEXT IMPLEMENTATION TARGET

Step 3 — Policy-Level Permitted Crypto Profiles

Goal

Strengthen runtime policy semantics so crypto-profile admissibility is not
limited to a single bound profile string.

The next implementation must:

1 define policy-level permitted crypto profiles canonically
2 require permitted_crypto_profiles in the policy snapshot
3 require policy snapshot crypto_profile to be a member of permitted_crypto_profiles
4 refuse execution when the runtime-enforced crypto_profile is not permitted by policy
5 preserve deterministic replay behavior
6 keep receipts and replayable ledger evidence policy-semantics aware

Current minimum supported profile
ed25519+sha256+canonical_json_v1

------------------------------------------------

WHY THIS IS NEXT

The runtime now enforces missing, unsupported, and mismatch profile cases,
but policy semantics still model only a single bound crypto_profile.

To move honestly toward profile-aware migration and future PQC-capable
operation, policy must explicitly define which crypto profiles are permitted.

------------------------------------------------

EXPECTED OUTPUT

The next completed step should produce:

• policy snapshot support for permitted_crypto_profiles
• deterministic refusal when crypto_profile is not permitted by policy
• docs aligned with runtime semantics
• replayable evidence that remains deterministic under policy profile rules

------------------------------------------------

AFTER THIS STEP

Once policy-level permitted profile semantics are implemented, the next components are:

4 profile mismatch and migration-window rules
5 offline verifier profile selection logic
6 deterministic mixed-profile replay tests

------------------------------------------------

END
