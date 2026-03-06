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
