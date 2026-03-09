DTPE CANONICAL RUNTIME INVARIANTS

Invariant 1
Derived public key from canonical private key must equal stored public key.

Invariant 2
Derived public key fingerprint must equal stored fingerprint.

Invariant 3
Policy snapshot hash must be deterministically recomputable from canonical policy.

Invariant 4
Authority snapshot hash must be deterministically recomputable from canonical authority inputs.

Invariant 5
Execution decision must occur before any irreversible mutation.

Invariant 6
Receipt hash must be deterministically recomputable from canonical receipt content.

Invariant 7
Offline verification must validate signatures and receipt hashes from exported artifacts alone.

Invariant 8
If any equality check fails, execution state must be REFUSED_NON_BINDING.

Invariant 9
Policy snapshot must contain a non-empty crypto_profile.

Invariant 10
Authority snapshot must bind crypto_profile into canonical authority material.

Invariant 11
Receipt and replayable ledger evidence must carry crypto_profile.

Invariant 12
If crypto_profile is missing where required, execution state must be REFUSED_NON_BINDING.

Execution and Authorization Invariants

Authority must be recomputed at the execution boundary.

Authority cannot be inherited across requests, processes, or system layers.

Canonical serialization used for hashing must be deterministic and reproducible across environments.

Refusal decisions must not mutate ledger state unless the refusal receipt is the intended recorded artifact.

An offline verifier must be able to reproduce authorization decisions deterministically from stored artifacts.

Crypto profile is governance-significant and must be bound through policy, authority, receipt, and replayable evidence.
