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

---

## EXECUTION INTEGRITY MODEL

DTPE's execution integrity model is defined in:

- docs/EXECUTION_INTEGRITY_MODEL.md
- docs/PHASE9_GAP_STATEMENT.md

All boundary decisions, receipts, ledger records, and verifier logic must remain consistent with:

- execution-bound admissibility
- replay integrity
- reconstruction integrity as the required later proof layer

No change may weaken these guarantees by introducing hidden runtime dependence, inferred evaluator identity, or non-canonical proof artifacts.

---

## MUTATION AUTHORITY INVARIANT

Authorization, execution evidence, and mutation authority are distinct governance roles.

A system is not structurally governable unless the component that controls the state-changing primitive is subordinate to the admissibility predicate at the mutation boundary.

No irreversible mutation may occur unless mutation authority revalidates the bound admissibility predicate against the governing live state at the mutation boundary.

If a side effect can occur before that revalidation, the system is observational rather than governable.

Receipts, attestations, replay, and post-hoc verification are necessary but insufficient unless the state-changing primitive is fail-closed behind mutation authority.

The guarded primitive may include, but is not limited to:

- write
- send
- transfer
- publish
- queue irreversible downstream work
- invoke an external side effect
- commit a state transition

What cannot be re-established at the mutation boundary MUST NOT become real.