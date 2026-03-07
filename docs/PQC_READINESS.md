Here is a strict checklist you can use.

DTPE Canonical Runtime — PQC Readiness Checklist

Purpose
Ensure the new DTPE repo can migrate to post-quantum cryptography without redesigning authority, snapshots, receipts, or verification later.

Baseline rule
The system must never assume one permanent signature scheme.

All cryptographic validation must be driven by an explicit, versioned crypto profile.

PHASE P0 — Crypto Agility Contract

Goal
Freeze the rule that crypto is profile-driven, not hardcoded.

Must exist
docs/CRYPTO_PROFILE_SPEC.md
docs/PQC_READINESS.md

Must define
crypto profile is mandatory
profile is versioned
profile names are canonical strings
profile changes are governance-significant
profile mismatch causes refusal where required
no runtime layer may silently substitute algorithms

Example profile strings

ed25519+sha256+canonical_json_v1
hybrid_ed25519_dilithium3+sha256+canonical_json_v1
ml_dsa_65+sha384+canonical_json_v1

Status target
REQUIRED BEFORE RUNTIME HARDENING

PHASE P1 — Identity Model Compatibility

Goal
Make the identity registry capable of representing multiple crypto schemes.

Must support
identity bound to crypto profile
public key material labeled by algorithm
key fingerprint derived deterministically
optional support for multiple active keys per identity if migration requires it
explicit profile compatibility checks

Must not assume
Ed25519-only identity format
one fixed key encoding forever
one fixed fingerprint rule forever unless versioned by profile

Needed fields conceptually

identity_id
owner_id
crypto_profile
public_key
public_key_fingerprint
key_encoding
optional valid_from
optional valid_to

Status target
REQUIRED BEFORE PQC OR HYBRID KEYS ARE INTRODUCED

PHASE P2 — Canonical Serialization Stability

Goal
Ensure canonical serialization remains stable regardless of crypto transition.

Must guarantee
canonical JSON is deterministic
hashing input order is fixed
serialization rules do not depend on key type
profile string is serialized exactly
verifier uses the same canonicalization rules as runtime

Must not do
vary serialization by runtime environment
vary canonical order by algorithm
change canonical rules silently during migration

Status target
MANDATORY

PHASE P3 — Policy / Snapshot Binding

Goal
Bind crypto posture into policy and snapshot semantics.

Must include
policy state may reference permitted crypto profiles
snapshot must bind to crypto_profile
snapshot hash must change if crypto profile changes
policy drift involving crypto profile must be detectable

Must define
whether profile drift is always refusal
whether mixed-profile transitions are allowed
whether policy can authorize migration windows

Status target
REQUIRED BEFORE CRYPTO MIGRATION SEMANTICS

PHASE P4 — Authority Snapshot Compatibility

Goal
Ensure authority recomputation is crypto-profile-aware.

Authority recomputation must bind
identity inputs
owner inputs
policy state hash
request / action inputs
admissibility state
crypto profile
snapshot hash context

Must guarantee
authority derived under one profile does not validate under another profile unless explicitly allowed by policy and profile rules
crypto profile drift is visible in recomputation
authority hash changes when crypto profile changes

Must not allow
implicit cross-profile validation
profile substitution after snapshot creation
profile omission from authority materialization

Status target
REQUIRED

PHASE P5 — Decision Engine Rules

Goal
Make PQC posture part of admissibility.

Decision logic must define
when crypto profile mismatch causes REFUSED_NON_BINDING
whether deprecated profiles are allowed
whether hybrid profile is mandatory during transition
whether profile downgrade is always refusal

Refusal examples that should be supported
unsupported crypto profile
profile mismatch
deprecated profile after cutoff
mixed verifier/runtime profile mismatch
invalid signature under declared profile

Must include in decision object
crypto_profile
refusal reason if profile-related
deterministic refusal class

Status target
REQUIRED BEFORE LIVE MIGRATION

PHASE P6 — Runtime Execution Boundary

Goal
Ensure execution boundary enforces crypto posture, not just signature success.

Must enforce
declared crypto profile is present
runtime verifier for that profile is available
profile is allowed by current policy
profile matches snapshot / authority derivation context

Must not do
“signature valid therefore allow”
accept unknown profile strings
silently fall back to legacy verifier
allow profile downgrade without explicit rule

Status target
MANDATORY

PHASE P7 — Receipt and Ledger Compatibility

Goal
Preserve auditability across crypto transitions.

Receipts must include
crypto_profile
signature verification outcome
authority hash
snapshot hash
receipt hash

Ledger rules must define
whether multiple crypto profiles can coexist
whether old records remain valid after migration
whether verifier selection is record-local by profile
whether migration events are explicitly logged

Must not assume
one global verifier for all time
one signature scheme for all receipts
one permanent fingerprint rule unless versioned

Status target
REQUIRED BEFORE MULTI-PROFILE HISTORY

PHASE P8 — Offline Verifier

Goal
Allow offline verification across historical crypto profiles.

Verifier must support
reading crypto profile from record/snapshot/receipt
selecting correct verification logic by profile
rejecting records with unknown or unsupported profiles
deterministic replay across mixed historical profiles if policy permits

Must define
how verifier handles deprecated but historically valid profiles
whether verifier needs bundled trust metadata
whether policy snapshot determines allowed profile at that historical point

Must not do
assume current crypto profile applies to all past records
verify with wrong algorithm and call it equivalent
ignore profile mismatch during replay

Status target
REQUIRED FOR TRUE PQC READINESS

PHASE P9 — Migration Semantics

Goal
Define how the system moves from pre-PQC to hybrid to PQC without ambiguity.

Must define explicitly
legacy profile
hybrid transition profile
post-transition PQC profile
migration start condition
migration completion condition
downgrade refusal rule
coexistence period if any
whether re-signing is required
whether old snapshots remain valid or must be rederived

Status target
REQUIRED BEFORE CLAIMING PQC MIGRATION SUPPORT

PHASE P10 — Testing Requirements

Goal
Prove the system is actually crypto-agile.

Must have tests for
valid legacy profile
valid hybrid profile
valid PQC profile
profile mismatch refusal
profile downgrade refusal
snapshot hash changes on profile change
authority hash changes on profile change
receipt generation under each profile
offline verifier selecting correct profile logic
replay of mixed-profile historical records if allowed

Status target
MANDATORY FOR CLAIMS
