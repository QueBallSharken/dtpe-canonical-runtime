IDENTITY MODEL

Purpose

This document defines the canonical identity structure used by the DTPE runtime
and the evolution path required to support profile-driven cryptographic identity.

The identity model must remain deterministic, verifiable, and compatible with
the runtime governance invariants.

------------------------------------------------

CANONICAL PRINCIPLES

Private key material is the canonical source of authority.

Public keys are derived from private keys.

Fingerprints are derived deterministically from public keys.

Registry values must never be trusted without recomputation and verification.

Private key material must never be committed to the repository.

------------------------------------------------

CURRENT IMPLEMENTATION

The current runtime identity model supports a single active key.

Identity records currently contain:

• identity_id
• owner_id
• role
• expires_at
• key_type
• public_key_b64
• public_key_fingerprint_sha256

Current implementation characteristics:

• one key per identity
• Ed25519-shaped identity records
• deterministic fingerprint verification
• private key stored separately from identity registry
• identity invariants enforced at runtime startup

The runtime verifies:

derived_public_key == stored_public_key

derived_fingerprint == stored_fingerprint

If either check fails, execution must halt.

------------------------------------------------

CURRENT LIMITATION

The identity model currently assumes a single cryptographic key per identity.

However the runtime now supports multiple cryptographic profiles through
policy-governed crypto profile enforcement.

This creates a structural mismatch between:

runtime cryptographic capabilities

and

identity registry structure.

The identity model must therefore evolve to support profile-bound keys.

------------------------------------------------

PROFILE-AWARE IDENTITY MODEL

Future identity records must support keys bound to specific crypto profiles.

This allows:

• clean cryptographic migration
• support for multiple algorithms
• deterministic key selection
• runtime verification based on policy crypto profile

Conceptual structure:

identity_id
owner_id
role
expires_at
active_crypto_profile

keys:

    ed25519+sha256+canonical_json_v1
        public_key_b64
        public_key_fingerprint_sha256

    ml_dsa_65+sha384+canonical_json_v1
        public_key_b64
        public_key_fingerprint_sha256

Each key entry is associated with a specific crypto profile.

------------------------------------------------

ACTIVE PROFILE SELECTION

The runtime must determine which key to use based on:

policy crypto_profile

If the identity does not contain a key compatible with the required
crypto profile, execution must be refused as non-binding.

Key resolution must therefore occur using the crypto_profile value
propagated through:

policy snapshot
authority snapshot
execution decision
receipt
ledger evidence

------------------------------------------------

MIGRATION SUPPORT

The profile-aware identity model must allow temporary coexistence of
multiple key types during cryptographic migration windows.

Example scenario:

identity contains both

ed25519+sha256+canonical_json_v1
ml_dsa_65+sha384+canonical_json_v1

Policy migration windows determine which profile is currently valid.

The runtime must select the key matching the active profile.

------------------------------------------------

IDENTITY INVARIANTS

The following conditions must always hold.

Invariant 1

Derived public key from canonical private key must equal stored public key.

Invariant 2

Derived fingerprint must equal stored fingerprint.

Invariant 3

Key records must be deterministically associated with a crypto profile.

Invariant 4

Runtime key resolution must use the crypto_profile propagated through
policy, authority snapshot, receipt, and ledger evidence.

Invariant 5

If no compatible key exists for the required crypto profile,
execution must be refused as non-binding.

------------------------------------------------

IMPLEMENTATION NOTE

The current runtime still uses the single-key identity structure.

The profile-aware identity model defined in this document is the
next evolution step and must be implemented according to the
ordered plan defined in:

docs/NEXT_STEPS.md

------------------------------------------------

END OF FILE
