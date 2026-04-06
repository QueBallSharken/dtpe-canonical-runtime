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

The runtime currently supports deterministic governance behavior,
but the exact current bounded phase classification must be described
consistently with the committed runtime surface before further
implementation planning proceeds.

------------------------------------------------

Current Stable Baseline

The grounded repo state for this thread is beyond a pure Phase 5 baseline.

Visible runtime structures in the grounded repo state include:

- temporal invariant handling
- frame continuity handling
- bounded signal_profile construction
- bounded decision_space construction
- continuity-related receipt fields
- evaluator_trace-related receipt and verifier handling

Accordingly, this roadmap must not describe the current public baseline
as Phase 5 only.

------------------------------------------------

Current Repository Reality

The current repository state shown in this thread includes runtime
structures associated with:

- execution-boundary admissibility
- temporal admissibility
- continuity across linked decisions
- bounded decision-space evidence
- evaluator-trace-related receipt and verifier handling

However, current implementation-state documentation does not describe
these structures consistently.

------------------------------------------------

PQC / Crypto-Agility Guardrail

All repository-state and planning updates must preserve DTPE's
crypto-agility posture.

Nothing in this cleanup authorizes:

- implicit cryptographic behavior
- silent profile substitution
- hard-coding a single permanent algorithm assumption
- weakening replayability across profile transitions

All current and future runtime and documentation alignment must remain
compatible with:

- explicit crypto-profile identity
- policy-governed permitted profiles
- governed migration across profile generations
- independently reconstructable historical evidence
- post-quantum readiness

------------------------------------------------

Immediate Documentation Priority

Before introducing new implementation work, the repository must first
reconcile:

1. current repo-authoritative phase baseline
2. current bounded Phase 8 status
3. current bounded Phase 9 runtime status
4. current planning documents so they match visible committed code

------------------------------------------------

Planning Rule

No roadmap section should describe:

- Phase 5 as the effective live baseline
- Phase 7 as absent from the public repo
- Phase 9 as both absent and implemented

until the repo state is made internally consistent.

END OF FILE