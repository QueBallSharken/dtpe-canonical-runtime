DTPE DEMONSTRATION

Purpose

This document defines the minimal demonstration path for the DTPE runtime.

The goal is to allow a reviewer to execute one request, produce one receipt,
write one ledger record, and independently verify that ledger evidence.

------------------------------------------------

DEMONSTRATION GOAL

Show that the runtime can:

- execute a deterministic request
- bind policy and authority into a receipt
- append a ledger record
- verify the ledger record offline

Expected result:

PASS: verified 1 ledger record(s)

------------------------------------------------

REPOSITORY ROOT

Use this repository root:

C:\Users\Stevil\code\dtpe-canonical-runtime

------------------------------------------------

STEP 1

Set working directory to repository root.

Command:

Set-Location "C:\Users\Stevil\code\dtpe-canonical-runtime"

------------------------------------------------

STEP 2

Execute one deterministic request through the runtime.

Command:

py -c "from core.phase4.pipeline import execute_request; print(execute_request(policy_filename='default.json', identity_id='alice', owner_id='alice', intent='demo.intent', action='execute', expires_at='2030-01-01T00:00:00'))"

Expected behavior:

- receipt object printed
- data\ledger.log created

------------------------------------------------

STEP 3

Verify the ledger offline.

Command:

py -m tools.verify_ledger

Expected behavior:

PASS: verified 1 ledger record(s)

------------------------------------------------

STEP 4

Optional cleanup.

Command:

Remove-Item ".\data\ledger.log"

This removes generated demo ledger output if the artifact is not intended
to remain in the repository working tree.

------------------------------------------------

NOTES

The current demonstration uses:

- default policy
- alice identity
- Ed25519 signing path
- deterministic receipt and ledger generation

ML-DSA profile support is currently scaffolded at the governance layer
but does not yet include a signing backend.

------------------------------------------------

END OF FILE
