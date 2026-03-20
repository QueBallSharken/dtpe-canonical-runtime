DTPE / IAL / SPECTRE — PHASE 6 (TEMPORAL ADMISSIBILITY)

Status

Locked specification.
Next public implementation target.
Not yet implemented in the current runtime.

Purpose

Phase 6 enforces:

A transition is only valid if a canonical execution-time input satisfies
its temporal constraints at the moment of evaluation.

This prevents:

- stale authority execution
- replay of expired transitions
- hidden runtime clock dependency
- unverifiable temporal decisions

Core invariant

Temporal validity must be:

- evaluated using explicit canonical input
- recorded in receipt
- stored in ledger
- replayed by verifier
- compared deterministically

No implicit time.
No runtime clock.
No hidden temporal state.

Critical rule

Time is a canonical input, not a system computation.

The system must not:

- read system time for decision logic
- generate timestamps internally for temporal admissibility
- depend on runtime clock state

The system must:

- require execution_time as input
- evaluate against canonical temporal constraints
- persist execution_time in the receipt
- replay that same input during verification

Canonical temporal result

temporal_invariant_result = {
  "ok": bool,
  "reason": str,
  "execution_time": str,
  "expires_at": str
}

Locked rules

1. execution_time is required

execution_time must:

- be present at pipeline entry
- be passed unchanged through pipeline -> boundary -> receipt -> ledger -> verifier
- not be generated or modified by runtime logic

2. temporal constraints are canonical

expires_at must:

- be part of canonical transition input
- be deterministic
- be present for temporal validation

3. temporal evaluation is pure

Temporal guard must:

- compare execution_time vs expires_at
- produce deterministic result
- return structured output only

Temporal guard must not:

- access external state
- raise exceptions for normal failure
- introduce side effects

4. enumerated reasons only

temporal_invariant_result.reason must be one of:

- VALID
- MISSING_EXECUTION_TIME
- MISSING_EXPIRES_AT
- EXPIRED

Architecture flow

INPUT (execution_time)
-> pipeline
-> boundary
   - authority_result
   - state_admissibility_result
   - stability_result
   - temporal_invariant_result
-> decision
-> receipt
-> ledger
-> verifier
   - recompute temporal result
   - compare deterministically

Required implementation scope

Phase 6 implementation must update:

- core/spectre/temporal_guard.py
- core/spectre/boundary.py
- core/phase4/pipeline.py
- core/phase4/receipt.py
- tools/test_phase6_temporal_guard.py
- tools/test_phase6_boundary_temporal_path.py
- tools/test_phase4_pipeline_crypto_profile.py
- tools/verify_ledger.py
- tools/test_phase5_boundary_replay_verifier.py
- tools/test_phase5_boundary_refusal_replay.py

Verifier requirement

Verifier must:

- read execution_time from receipt
- recompute temporal result using the same recorded input
- compare stored vs recomputed temporal result

Failure condition:

if recomputed != stored:
    raise RuntimeError("temporal_invariant_result mismatch")

Definition of done

Phase 6 is complete only if:

- execution_time is required at input
- temporal guard exists and is pure
- boundary includes temporal result
- receipt stores execution_time and temporal result
- ledger contains temporal data
- verifier recomputes using recorded execution_time
- mismatch fails deterministically
- all Phase 6 and dependent replay tests pass

Failure modes to prevent

- runtime clock usage
- missing execution_time
- missing expires_at
- non-deterministic timestamps
- verifier not recomputing
- free-form reason strings

PQC safety

Phase 6 remains PQC-safe because:

- crypto_profile handling does not change
- no signature algorithm assumptions are introduced
- temporal logic is independent of cryptography
- canonical JSON remains preserved
- verifier remains deterministic

Relationship to Phase 7

Phase 6 validates a single decision at an explicit canonical execution time.

Phase 7, if implemented later, will validate continuity across decisions.

END OF FILE
