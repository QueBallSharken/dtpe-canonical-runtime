# DTPE / IAL / SPECTRE - Phase 6 (Temporal Admissibility)

## Status

Locked specification.
Next public implementation target.
Not yet implemented in the current runtime.

## Purpose

Phase 6 enforces temporal validity as a canonical execution-boundary requirement.

A transition is only valid if a canonical execution-time input satisfies the temporal constraints of the proposed transition.

This prevents:

- stale authority execution
- replay of expired transitions
- hidden runtime clock dependency
- unverifiable temporal decisions

Temporal validity is a subordinate component of DTPE boundary integrity.

For the integrated mutation-boundary governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Core invariant

Temporal validity must be:

- evaluated using explicit canonical input
- recorded in receipts
- stored in ledger
- replayed by verifier
- compared deterministically

No implicit time.
No runtime clock.
No hidden wall-clock state.

## Critical rule

Time is a canonical input, not a runtime computation.

The system must not:

- read system time for decision logic
- generate timestamps internally for admissibility
- depend on runtime clock state

The system must:

- receive execution time as input
- use that input against temporal constraints
- persist execution time for replay verification

## Locked rules

### 1. execution_time is required

`execution_time` must:

- be present at pipeline entry
- be passed unchanged through pipeline, boundary, receipt, ledger, and verifier
- not be generated or modified by runtime logic

### 2. temporal constraints are canonical

`expires_at` must:

- be part of canonical transition input
- be deterministically evaluated
- be present for temporal validation

### 3. temporal evaluation is pure

Temporal guard must:

- consume canonical temporal inputs only
- produce deterministic result
- return structured output only

Temporal guard must not:

- access external state
- raise exceptions for normal failures
- introduce side effects

### 4. enumerated reasons only

`temporal_invariant_result.reason` must be one of:

- `VALID`
- `MISSING_EXECUTION_TIME`
- `MISSING_EXPIRES_AT`
- `EXPIRED`

## Canonical temporal result

The canonical result format is:

- `ok`
- `reason`
- `execution_time`
- `expires_at`

## Architecture flow

`INPUT (execution_time) -> pipeline -> boundary`

Boundary output includes:

- `authority_result`
- `state_admissibility_result`
- `stability_result`
- `temporal_invariant_result`

Then:

`decision -> receipt -> ledger -> verifier`

Verifier must:

- recompute temporal result
- compare stored versus recomputed result deterministically

## Boundary requirement

Temporal admissibility is not transferable across time.

A valid evaluation at one time does not imply validity at a later time.

Temporal validity must therefore be re-derived from canonical inputs at the execution boundary.

A temporally invalid action must refuse rather than mutate.

## Required implementation scope

Phase 6 implementation must update:

- `core/spectre/temporal_guard.py`
- `core/spectre/boundary.py`
- `core/phase4/pipeline.py`
- `core/phase4/receipt.py`
- `tools/test_phase6_temporal_guard.py`
- `tools/test_phase6_boundary_temporal_path.py`
- `tools/test_phase4_pipeline_crypto_profile.py`
- `tools/verify_ledger.py`
- `tools/test_phase5_boundary_replay_verifier.py`
- `tools/test_phase5_boundary_refusal_replay.py`

## Verifier requirement

Verifier must:

- read `execution_time` from receipt
- recompute temporal result using the same recorded input
- compare stored versus recomputed temporal result

Failure condition:

if recomputed != stored: raise

`RuntimeError("temporal_invariant_result mismatch")`

## Definition of done

Phase 6 is complete only if:

- `execution_time` is required at input
- temporal guard exists and is pure
- boundary includes temporal result
- receipt stores `execution_time` and temporal result
- ledger contains temporal data
- verifier recomputes using recorded `execution_time`
- mismatch fails deterministically
- all Phase 6 and dependent replay tests pass

## Failure modes to prevent

- runtime clock usage
- missing `execution_time`
- missing `expires_at`
- non-deterministic timestamps
- verifier not recomputing
- free-form reason strings

## PQC safety

Phase 6 remains PQC-safe because:

- crypto-profile handling does not change
- no signature algorithm assumptions are introduced
- temporal logic is independent of cryptography
- canonical JSON remains preserved
- verifier remains deterministic

## Relationship to Phase 7

Phase 6 validates a single decision at an explicit canonical execution time.

Phase 7, if implemented later, will validate continuity across decisions.
