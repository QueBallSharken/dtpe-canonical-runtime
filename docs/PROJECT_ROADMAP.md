DTPE Project Roadmap

Repository
https://github.com/QueBallSharken/dtpe-canonical-runtime

Purpose

This document provides orientation for contributors, reviewers,
and future development sessions. It explains the current system
state and the next architectural phases.

------------------------------------------------

Project Overview

DTPE (Delegated Task Provenance Engine) is a deterministic governance
runtime that produces cryptographically verifiable evidence showing
how automated decisions are made.

The system generates canonical receipts and append-only ledger records
that can be independently verified without trusting the runtime that
produced them.

------------------------------------------------

Core Invariant

verify without trusting the runtime that generated it

All architecture decisions must preserve this property.

------------------------------------------------

Current Runtime Capabilities

The runtime currently supports:

- deterministic authority recomputation
- canonical policy snapshots
- canonical authority snapshots
- cryptographic profile enforcement
- deterministic boundary evaluation
- canonical receipt generation
- append-only ledger evidence
- independent offline verification

Current execution pipeline

request
-> authority evaluation
-> boundary decision
-> canonical receipt
-> ledger append
-> offline verification

------------------------------------------------

Current Stable Baseline

Public repository baseline is Phase 5 complete.

Phase 5 currently covers:

- authority validity
- state admissibility
- system stability

Execution is allowed only when the current boundary constraints evaluate true.

------------------------------------------------

Completed Phases

Phase 4

Deterministic authority enforcement at the execution boundary.

Phase 5

Deterministic boundary control using:

- authority validity
- state admissibility
- system stability

Receipts and ledger records now contain replayable boundary evidence for
the current implemented boundary path.

------------------------------------------------

Next Architecture Evolution

Phase 6

Temporal Admissibility

Goal:

A transition is only valid if a canonical execution_time input satisfies
its temporal constraints at the moment of evaluation.

Phase 6 design rules:

- execution_time is a required canonical input
- runtime clock must not be used
- temporal results must be stored in receipt and ledger
- verifier must replay temporal admissibility from recorded inputs

Primary files expected to change in Phase 6:

- core/spectre/temporal_guard.py
- core/spectre/boundary.py
- core/phase4/pipeline.py
- core/phase4/receipt.py
- tools/verify_ledger.py
- temporal and replay test files

------------------------------------------------

Planned Follow-On Phase

Phase 7

Invariant-Frame Continuity

Phase 7 is currently a locked design direction only.

It is not the current public implementation target.

Its role will be to validate cross-decision continuity after Phase 6 is
fully implemented and verified.

------------------------------------------------

Strategic Direction

The system evolves from a verification runtime into a deterministic
governance kernel for automated systems.

The runtime is moving toward proving:

- who acted
- why the action was authorized
- whether the resulting state was admissible
- whether the system remained stable
- whether the action was temporally admissible
- whether future decisions remain coherent across boundaries

------------------------------------------------

Immediate Implementation Priority

1. Document Phase 6 as the locked next implementation target.
2. Implement temporal admissibility with canonical execution_time input.
3. Bind temporal results into receipt and ledger.
4. Extend offline verifier to replay temporal admissibility.
5. Keep Phase 7 out of the public implementation path until Phase 6 is complete.

END OF FILE
