DTPE CANONICAL RUNTIME
CRYPTO PROFILE SPECIFICATION

Purpose

Define how cryptographic algorithms are declared and enforced in the DTPE runtime.

The system must never assume a permanent signature scheme.
All cryptographic validation must be driven by an explicit crypto profile.

------------------------------------------------

CRYPTO PROFILE

A crypto profile is a canonical string that defines the cryptographic
algorithms and canonicalization rules used for verification.

Profiles must be versioned and immutable.

Example profiles

ed25519+sha256+canonical_json_v1
hybrid_ed25519_dilithium3+sha256+canonical_json_v1
ml_dsa_65+sha384+canonical_json_v1

Profiles are case-sensitive canonical identifiers.

------------------------------------------------

PROFILE COMPONENTS

A crypto profile defines:

signature algorithm
hash algorithm
canonical serialization format

Example structure

<signature_algorithm> + <hash_algorithm> + <canonicalization_version>

Example

ed25519 + sha256 + canonical_json_v1

Serialized form

ed25519+sha256+canonical_json_v1

------------------------------------------------

PROFILE RULES

1. Profiles must be explicit in all authority-bearing material.

2. Profiles must be included in:

policy snapshots
authority snapshots
execution envelopes
receipts
offline verification artifacts

3. Profile mismatch must never be ignored.

4. Runtime must refuse execution when a profile mismatch occurs
unless policy explicitly authorizes a transition.

5. Runtime must not silently substitute algorithms.

------------------------------------------------

PROFILE GOVERNANCE

Crypto profile changes are governance-significant.

Changing the active profile requires:

policy change
snapshot change
authority recomputation

Profile changes must be visible in:

snapshot hash
authority hash
receipt records

------------------------------------------------

PROFILE VERSIONING

Profiles must be immutable once defined.

New algorithms must use new profile strings.

Example

ed25519+sha256+canonical_json_v1
ed25519+sha256+canonical_json_v2

Profiles must never be redefined.

------------------------------------------------

PROFILE VERIFIER RULE

Verification logic must be selected using the crypto profile.

Verifier must:

read profile from artifact
select verification implementation for that profile
fail if profile is unsupported

Verifier must not:

assume the current system profile
verify using the wrong algorithm
ignore profile mismatch

------------------------------------------------

PROFILE MIGRATION PRINCIPLE

Migration between profiles must be explicit.

Possible migration models include:

legacy profile
hybrid transition profile
post-transition PQC profile

Migration policy must define:

when legacy profiles stop being accepted
whether hybrid signatures are required
how long coexistence is allowed

------------------------------------------------

NON-NEGOTIABLE RULE

All authority, snapshot, decision, receipt, and verifier semantics
must be profile-driven and deterministic across profile transitions.

------------------------------------------------

END
