PROJECT CONTEXT

Purpose

Provide the minimum context a new contributor or analysis thread must read before contributing to this repository.

------------------------------------------------

WHY THIS REPOSITORY EXISTS

This repository is a clean rebuild of a prior DTPE prototype.

The earlier repository accumulated architectural drift including:

• identity key mismatch between private key and registry
• multiple key sources
• runtime signature failures
• lack of invariant enforcement
• duplicated authority values

Rather than patching those issues, the runtime architecture was rebuilt from first principles.

------------------------------------------------

ARCHITECTURAL MODEL

DTPE runtime has four logical layers:

Phase 1 — Identity
Phase 2 — Signature verification
Phase 3 — Ledger integrity
Phase 4 — Runtime governance

Execution flow:

client signs request
server verifies signature
authority snapshot recomputed
phase-4 admissibility decision
receipt generation
ledger append

------------------------------------------------

KEY GUARANTEE

Authority must be recomputed at execution time.

Stored authority values must never be blindly trusted.

------------------------------------------------

CURRENT IMPLEMENTATION STATUS

Implemented:

• canonical serialization
• hashing primitives
• identity registry loader
• identity invariant checker

Pending:

• identity key generator
• policy snapshot loader
• authority snapshot computation
• phase-4 decision engine
• ledger append
• offline verifier

------------------------------------------------

NEXT IMPLEMENTATION STEP

Implement deterministic identity key generator that:

1 generates private key
2 derives public key
3 updates identity registry
4 guarantees invariant compliance

------------------------------------------------

END
