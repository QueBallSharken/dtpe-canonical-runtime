NEXT IMPLEMENTATION STEP

Purpose

This file defines the next implementation target so that any new contributor
or analysis thread can continue work without relying on prior conversation context.

------------------------------------------------

CURRENT STATE

This repository is a clean canonical rebuild of the DTPE runtime.

The following components are already defined:

• canonical hashing primitives
• canonical serialization rules
• identity model specification
• system invariants
• governance guardrails
• change control policy

These documents define the architecture before runtime code is written.

------------------------------------------------

NEXT IMPLEMENTATION TARGET

Step 1 — Identity Key Generator

Goal

Create an identity generation tool that establishes the canonical
source of identity authority.

The generator must:

1 generate an Ed25519 private key
2 derive the public key from the private key
3 compute a SHA-256 fingerprint of the public key
4 write the private key to data/keys/
5 write data/identities/<identity>.json with the derived public key and fingerprint
6 verify the identity invariant before exiting

Invariant

derived_public_key(private_key)
=
stored_public_key(identity_registry)

derived_fingerprint(public_key)
=
stored_fingerprint(identity_registry)

If either invariant fails, the program must abort.

------------------------------------------------

WHY THIS IS FIRST

Identity is the root of all authority in DTPE.

All later components depend on a correct identity model.

Without correct identity generation, identity drift can occur.

------------------------------------------------

EXPECTED OUTPUT

Running the generator should produce:

data/keys/<identity>.ed25519.key
data/identities/<identity>.json

The identity record must contain:

identity_id
owner_id
role
expires_at
key_type
public_key_b64
public_key_fingerprint_sha256

------------------------------------------------

AFTER THIS STEP

Once identity generation is complete, the next components are:

2 policy snapshot loader
3 authority snapshot recomputation
4 phase-4 decision engine
5 execution boundary
6 receipt generation
7 ledger append
8 offline verifier

------------------------------------------------

END
