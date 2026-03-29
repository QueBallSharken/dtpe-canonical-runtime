# CURRENT IMPLEMENTATION STATE

## REPOSITORY STATUS

- branch: main
- working tree: clean
- local state matches origin/main
- no partial runtime changes present

---

## PHASE STATUS

- Phase 7: COMPLETE (runtime stable)
- Phase 8: PARTIALLY IMPLEMENTED (bounded slices committed)
- Phase 9: DESIGN COMPLETE (NO RUNTIME IMPLEMENTATION ACTIVE)

---

## PHASE 9 STATUS

All Phase 9 specifications are locked:

- Phase 9 (Evaluator Integrity)
- Phase 9B (Evaluator Rule Continuity Binding)
- Phase 9C (Evaluator Output Determinism)
- Phase 9 Implementation Strategy

No Phase 9 runtime code is currently committed.

---

## PRIOR LOCAL STATE (REVERTED)

Phase 9A runtime work was attempted locally and reverted.

Attempted components:

- evaluator_trace construction in boundary
- evaluator_trace validation in verifier
- evaluator_trace receipt wiring

These changes were NOT committed and have been fully restored.

Repository is now back to a clean authoritative state.

---

## NEXT IMPLEMENTATION TARGET

Phase 9A — Minimal Evaluator Trace

Scope:

- introduce evaluator_trace as a canonical element
- ensure deterministic structure
- bind evaluator identity to execution boundary

Required files:

- core/spectre/boundary.py
- core/phase4/receipt.py
- tools/verify_ledger.py

---

## REQUIRED CHANGES (PHASE 9A)

### boundary.py

- construct evaluator_trace
- return evaluator_trace in decision object

Minimal structure:

{
  "evaluator_id": str,
  "evaluator_trace_version": str
}

---

### receipt.py

Must perform BOTH:

1. before canonical_json(receipt_material):

    evaluator_trace = decision.get("evaluator_trace")
    if evaluator_trace is not None:
        receipt_material["evaluator_trace"] = evaluator_trace

2. after receipt = { ... } is constructed:

    if evaluator_trace is not None:
        receipt["evaluator_trace"] = evaluator_trace

---

### verify_ledger.py

- extract evaluator_trace from payload
- validate structure
- required fields:
  - evaluator_id: str
  - evaluator_trace_version: str
- insert into reconstructed receipt_material

---

## IMPLEMENTATION RULES

- no regex-based insertion
- no multi-line pattern replacement
- no writes using Set-Content -Encoding utf8 (BOM risk)
- all insertions must be line-index based
- verify diff after each file change
- stop immediately if anchor mismatch occurs

---

## REQUIRED PASS SET

After Phase 9A implementation:

py -m tools.test_phase7_frame_continuity
py -m tools.test_phase7_boundary_frame_path
py -m tools.test_phase7_pipeline_continuity
py -m tools.test_phase5_boundary_refusal_replay
py -m tools.verify_ledger
py -m tools.test_phase5_boundary_replay_verifier

All must PASS before commit.

---

## STOP CONDITIONS

Stop immediately if:

- insertion occurs before variable definition
- insertion occurs before receipt exists
- diff shows merged lines
- BOM or encoding artifacts appear
- verifier reconstruction fails
- replay parity fails

---

## GOAL

Complete Phase 9A only:

- evaluator_trace present in boundary
- evaluator_trace included in receipt
- evaluator_trace included in canonical hash
- evaluator_trace reconstructed by verifier
- replay parity preserved

No Phase 9B or Phase 9C runtime work is authorized.

## PHASE 9 UPDATE

- Phase 9A: IMPLEMENTED
- Phase 9B: BLOCKED PENDING CANONICAL RULE SOURCE
- Phase 9C: DESIGN ONLY

Phase 9A is committed and pushed:
- evaluator_trace construction in boundary
- evaluator_trace receipt wiring
- evaluator_trace verifier reconstruction

Rollback tag:
- phase9a-minimal-evaluator-trace

Phase 9B implementation is not yet authorized.

Blocking reason:
A canonical evaluator rule source was not originally defined as a replay-reconstructable artifact.

Current next safe step:
Define and lock evaluator_rule_profile as the canonical Phase 9B rule source before any runtime implementation begins.
