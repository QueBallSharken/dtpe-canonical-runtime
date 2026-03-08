NEXT IMPLEMENTATION STEP

Purpose

This file defines the next implementation target so that any new contributor
or analysis thread can continue work without relying on prior conversation context.

------------------------------------------------

CURRENT STATE

This repository is a clean canonical rebuild of the DTPE runtime.

Core architecture components implemented:

• canonical hashing primitives
• canonical JSON serialization
• deterministic project path handling
• identity generation and registry
• authority snapshot construction
• policy snapshot construction
• Phase4 decision engine
• Phase4 execution pipeline
• receipt construction
• deterministic ledger append

------------------------------------------------

CRYPTO POLICY GOVERNANCE

The runtime now supports policy-governed crypto enforcement.

Policy files define:

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

Runtime behavior:

• execution crypto profile must match policy crypto_profile
• unless a migration window is active
• and the request matches the allowed transition

Migration enforcement occurs inside:

core/phase4/decision.py

The execution pipeline wires this through:

core/phase4/pipeline.py

------------------------------------------------

TEST COVERAGE

Deterministic tests exist for:

• phase4 decision crypto profile enforcement
• phase4 pipeline crypto profile path
• policy snapshot migration window validation
• pipeline execution with migration-window policy

These tests confirm:

• policy snapshot validation
• migration window semantics
• runtime decision behavior
• deterministic ledger evidence

------------------------------------------------

CURRENT CRYPTO SUPPORT

The runtime currently supports one operational crypto profile:

ed25519+sha256+canonical_json_v1

Additional profiles may appear in policy files but will be refused
until they are added to SUPPORTED_CRYPTO_PROFILES.

------------------------------------------------

NEXT IMPLEMENTATION TARGET

Add operational support for additional crypto profiles.

Goal

Allow the runtime to execute under multiple supported crypto profiles.

This includes:

1 expanding SUPPORTED_CRYPTO_PROFILES
2 implementing the cryptographic primitives required for those profiles
3 verifying signature validation and hashing paths remain deterministic
4 ensuring pipeline and receipt logic remain profile-agnostic

Example target profile:

ml_dsa_65+sha384+canonical_json_v1

------------------------------------------------

IMPLEMENTATION CONSTRAINTS

All runtime behavior must remain:

• deterministic
• canonicalized
• replay-verifiable
• ledger-evidenced

Policy must remain the authority controlling which crypto
profiles are permitted at execution time.

------------------------------------------------

END OF FILE
