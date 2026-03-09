NEXT IMPLEMENTATION STEP

Purpose

This file defines the next implementation target so that any new contributor,
maintainer, or auditor can continue development without relying on external
context.

------------------------------------------------

CURRENT STATE

This repository contains a deterministic canonical runtime for DTPE.

Core architecture components implemented:

• canonical hashing primitives
• canonical JSON serialization
• deterministic path handling
• identity generation and registry
• authority snapshot construction
• policy snapshot construction
• Phase4 decision engine
• Phase4 execution pipeline
• receipt construction
• deterministic ledger append
• offline ledger and receipt verification

------------------------------------------------

CURRENT CHECKPOINT

The following milestone has been completed and tagged:

phase4-runtime-crypto-dispatch-v1

This checkpoint includes:

• crypto profile policy governance
• permitted crypto profile enforcement
• migration window support
• runtime crypto profile propagation
• signing backend dispatch
• verification backend dispatch
• Ed25519 authority signing implementation
• ML-DSA profile scaffold support
• deterministic verification test coverage

------------------------------------------------

CRYPTO PROFILE GOVERNANCE

The runtime supports policy-governed cryptographic profiles.

Policy defines:

• crypto_profile
• permitted_crypto_profiles
• optional migration_window

Migration window structure:

{
  "from_crypto_profile": "...",
  "to_crypto_profile": "...",
  "not_before": "...",
  "not_after": "..."
}

Execution rules:

• execution profile must match policy crypto_profile
• unless a migration window allows a transition
• permitted profiles must include the requested profile

------------------------------------------------

CURRENT CRYPTO SUPPORT

Runtime-recognized profiles:

• ed25519+sha256+canonical_json_v1
• ml_dsa_65+sha384+canonical_json_v1

Operational signing implementation currently exists for:

• ed25519+sha256+canonical_json_v1

ML-DSA support currently exists only at the policy and runtime
profile-dispatch level.

The ML-DSA signing backend is intentionally unimplemented.

------------------------------------------------

CURRENT LIMITATION

The identity registry is currently single-key and Ed25519-shaped.

Current identity record fields:

• identity_id
• owner_id
• role
• expires_at
• key_type
• public_key_b64
• public_key_fingerprint_sha256

The runtime therefore assumes a single active key for each identity.

This model is not yet compatible with multi-profile cryptographic identity.

------------------------------------------------

NEXT IMPLEMENTATION TARGET

Profile-aware identity model.

Goal

Allow identities to carry key material associated with multiple
cryptographic profiles without breaking deterministic verification.

This enables:

• clean cryptographic migration
• multi-algorithm compatibility
• profile-driven signing resolution
• profile-driven verification resolution

------------------------------------------------

ORDERED IMPLEMENTATION PLAN

Step 1

Define a profile-aware identity record format.

Step 2

Update the identity registry loader to read profile-bound key entries.

Step 3

Introduce profile-aware key lookup helpers.

Step 4

Update signing dispatch to resolve keys using crypto_profile.

Step 5

Update verification dispatch to resolve identity keys using crypto_profile.

Step 6

Preserve backward compatibility for existing Ed25519 identities.

------------------------------------------------

CONSTRAINTS

All runtime behavior must remain:

• deterministic
• canonicalized
• replay-verifiable
• ledger-evidenced

Policy remains the authority controlling which crypto profiles
are permitted during execution.

No runtime layer may assume a permanent signature scheme.

Private key material must never be committed to the repository.

------------------------------------------------

END OF FILE
