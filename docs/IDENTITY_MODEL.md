IDENTITY MODEL

Canonical rule
Private key is canonical source.
Public key is derived.
Fingerprint is derived.
Registry values are never manually trusted unless re-derived and checked.

Runtime rule
Startup must fail if:
- derived public key != stored public key
- derived fingerprint != stored fingerprint

Current identity registry stores:
- identity_id
- owner_id
- role
- expires_at
- key_type
- public_key_b64
- public_key_fingerprint_sha256

Current implementation note
The current runtime identity model is Ed25519-shaped and uses a single active key record.

PQC compatibility requirement
The long-term identity model must support profile-driven cryptographic identity semantics.

Future-compatible identity concepts
- identity_id
- owner_id
- crypto_profile
- key material labeled by algorithm or profile
- deterministic fingerprint derivation bound to profile rules
- explicit profile compatibility checks
- optional multiple active keys during migration windows

Constraint
No runtime layer may assume one permanent signature scheme.

Private key material must not be committed.
