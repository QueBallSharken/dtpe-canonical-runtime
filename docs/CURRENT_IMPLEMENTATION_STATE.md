# CURRENT IMPLEMENTATION STATE

## PURPOSE

This document defines the current implementation state of the repository, the immediate blocker, the required constraints on future changes, and the intended direction of work.

This repository must remain the authoritative source of implementation truth.

---

## REPOSITORY STATUS

Branch:
- main

Current implementation position:
- Phase 7 specification is locked in documentation
- Phase 7 implementation is in progress
- Core Phase 7 continuity logic exists
- Full verifier alignment is not yet complete

Current condition:
- dedicated Phase 7 guard, boundary, and pipeline tests pass
- replay/verifier path is not yet fully aligned
- no implementation commit should be made until verifier alignment is complete

---

## VERIFIED PASSING TESTS

The following commands are confirmed passing at the current stop point:

- `python -m tools.test_phase7_frame_continuity`
- `python -m tools.test_phase7_boundary_frame_path`
- `python -m tools.test_phase7_pipeline_continuity`

These passes confirm:

- deterministic invariant frame construction
- deterministic frame continuity evaluation
- boundary integration for Phase 7
- pipeline emission of Phase 7 continuity fields

---

## CURRENT BLOCKER

The current blocking failure is:

- `RuntimeError: Ledger record 1: receipt_canonical mismatch`

This occurs during:

- `python -m tools.verify_ledger`
- `python -m tools.test_phase5_boundary_replay_verifier`
- `python -m tools.test_phase5_boundary_refusal_replay`

This means:

- receipt construction and verifier reconstruction are not perfectly aligned
- the remaining problem is narrow and deterministic
- the current issue is not a broad Phase 7 logic failure

---

## KNOWN PROBLEM SCOPE

The remaining issue must be treated as isolated to receipt/verifier alignment unless direct inspection proves otherwise.

Primary files requiring inspection:

- `core/phase4/receipt.py`
- `tools/verify_ledger.py`

Additional files that may need to be referenced for alignment, but must not be changed without proof:

- `core/phase4/pipeline.py`
- `core/spectre/boundary.py`
- `core/spectre/frame_continuity.py`
- `tools/test_phase5_boundary_replay_verifier.py`
- `tools/test_phase5_boundary_refusal_replay.py`
- `tools/test_phase7_pipeline_continuity.py`

Observed mismatch candidate:

- `constraint_profile` values differ between pipeline/test inputs and ledger payload
- `temporal_rule_profile` values differ between pipeline/test inputs and ledger payload

This mismatch may affect `receipt_canonical` construction and verifier reconstruction.
This must be verified directly before any code changes are made.

Phase 7 introduced new receipt fields:

- `constraint_profile`
- `temporal_rule_profile`

These fields must be included identically in:
- receipt construction
- verifier reconstruction

Any asymmetry will cause `receipt_canonical` mismatch.

---

## REQUIRED NEXT ACTIONS

The next collaborator must proceed in this order:

1. Read the current contents of the relevant files completely.
2. Compare exactly:
   - the `receipt_material` used to build `receipt_canonical`
   - the verifier reconstruction used to compute `expected_receipt_canonical`
   - the actual payload written to `data/ledger.log`
3. Identify the exact field mismatch.
4. Fix only the exact mismatch.
5. Re-run all required Phase 7 tests.
6. Only commit after the verifier path passes completely.

Required verification commands:

- `python -m tools.test_phase7_frame_continuity`
- `python -m tools.test_phase7_boundary_frame_path`
- `python -m tools.test_phase7_pipeline_continuity`
- `python -m tools.test_phase5_boundary_replay_verifier`
- `python -m tools.test_phase5_boundary_refusal_replay`
- `python -m tools.verify_ledger`

---

## MUST-DO RULES

Any collaborator working from this state must:

- preserve deterministic behavior
- preserve replayability
- preserve verifier reconstructability
- inspect actual file contents before changing anything
- prove the mismatch before editing a file
- keep fixes minimal and isolated
- rerun all required verification commands before commit
- treat the repository as the only implementation authority

---

## MUST-NOT-DO RULES

Any collaborator working from this state must not:

- guess
- redesign Phase 7
- expand scope
- refactor unrelated code
- change files “just in case”
- change multiple files without direct justification
- introduce new behavior while resolving the verifier mismatch
- commit partial fixes
- push unfinished Phase 7 work

A file must not be changed unless there is direct evidence that changing it is necessary and safe.

---

## SAFE CHANGE POLICY

A file may only be modified if all of the following are true:

1. the file is directly involved in the proven mismatch
2. the exact mismatch is understood
3. the proposed change is minimal
4. the change does not alter intended Phase 7 behavior
5. the change can be verified immediately through deterministic tests

If any of these conditions are not met, the file must not be changed.

---

## PHASE 8 DIRECTION

Phase 8 is the next planned structural direction after Phase 7 is complete.

Phase 8 concerns:
- decision-space integrity
- defensibility of the visible option space before final admissibility
- preservation of upstream signal / constraint / risk framing structure
- replay-verifiable validation that a decision emerged from a structurally valid decision space

Phase 8 must not begin until:
- Phase 7 verifier alignment is complete
- replay paths are stable
- ledger reconstruction is deterministic end-to-end

---

## PHASE 9 DIRECTION

Phase 9 follows after Phase 8.

Phase 9 concerns:
- evaluator integrity
- validation that the checking layer itself remains structurally trustworthy
- protection against degraded or self-confirming evaluation layers
- replay-verifiable evidence that the evaluator remains within its own admissible integrity frame

Phase 9 must not begin until:
- Phase 7 is complete
- Phase 8 is stable
- the repository remains deterministic and verifier-sound

---

## IMPLEMENTATION PRINCIPLE

The repository must continue to enforce:

- canonical construction
- deterministic comparison
- ledger-based replay
- failure on structural mismatch
- no hidden runtime dependence

No future work should weaken these properties.

---

## STOP CONDITION FOR PHASE 7

Phase 7 may be treated as complete only when all of the following are true:

- dedicated Phase 7 tests pass
- replay verifier test passes
- refusal replay test passes
- `tools.verify_ledger` passes
- `receipt_canonical` matches exactly
- no unresolved schema mismatch remains
- changes are committed cleanly

Until then, Phase 7 is still in progress.

---

## FINAL INSTRUCTION

This repository must not be moved in a new direction while resolving the current blocker.

The immediate task is to finish Phase 7 cleanly, minimally, and deterministically.
