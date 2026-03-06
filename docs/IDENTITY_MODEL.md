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

Identity registry stores:
- identity_id
- owner_id
- role
- expires_at
- key_type
- public_key_b64
- public_key_fingerprint_sha256

Private key material must not be committed.
