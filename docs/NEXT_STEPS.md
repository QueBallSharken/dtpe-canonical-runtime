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
• offline ledger and receipt verifier

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

CURRENT CRYPTO SUPPORT

The runtime currently supports these operational profile identifiers:

• ed25519+sha256+canonical_json_v1
• ml_dsa_65+sha384+canonical_json_v1

Current actual signing / verification implementation exists only for:

• ed25519+sha256+canonical_json_v1

ML-DSA is currently supported at the runtime policy / profile layer,
but does not yet have a real signing or verification backend.

------------------------------------------------

AUTHORITY BINDING STATE

The runtime now includes an initial Ed25519 authority-binding path.

Implemented components:

• core/authority/signing.py
• core/authority/verification.py
• repaired alice identity registry record
• deterministic authority signing test

Current authority flow for Ed25519:

1 build authority snapshot
2 sign authority_canonical
3 include authority_signature_b64 in receipt
4 include authority_canonical in receipt
5 verify signature offline from ledger evidence

Offline verifier currently validates:

• ledger previous_hash chain
• ledger record canonicalization
• ledger record hash
• receipt canonicalization
• receipt hash
• Ed25519 authority signature when present

Verifier entry point:

tools/verify_ledger.py

------------------------------------------------

TEST COVERAGE

Deterministic tests exist for:

• phase4 decision crypto profile enforcement
• phase4 pipeline crypto profile path
• policy snapshot migration window validation
• phase4 pipeline migration-window policy path
• crypto registry initialization
• authority signing and verification

These tests currently pass.

------------------------------------------------

NEXT IMPLEMENTATION TARGET

Add crypto-profile-aware backend dispatch for real signature verification.

Goal

Move from profile identifiers and Ed25519-only helpers to a
runtime-dispatched cryptographic backend layer.

This includes:

1 defining backend dispatch from crypto_profile
2 adding an Ed25519 backend module
3 preparing an ML-DSA backend module scaffold
4 removing profile-specific signing assumptions from pipeline code
5 making offline verification dispatch through crypto profile rules

------------------------------------------------

IMPORTANT CURRENT LIMITATION

Authority signature verification in the offline verifier is currently
hardcoded to identity_id = "alice" for the Ed25519 path.

That is acceptable only as the current single-identity scaffold.

The next implementation stage must remove that assumption.

------------------------------------------------

IMPLEMENTATION CONSTRAINTS

All runtime behavior must remain:

• deterministic
• canonicalized
• replay-verifiable
• ledger-evidenced

Policy must remain the authority controlling which crypto
profiles are permitted at execution time.

No runtime layer may assume one permanent signature scheme.

------------------------------------------------

END OF FILE
