# CURRENT IMPLEMENTATION STATE

## REPOSITORY STATUS

Current authoritative baseline:

- branch: `main`
- remote branch: `origin/main`
- latest verified Phase 7 commit: `87dcd33`
- latest verified Phase 7 commit message:
  - `feat(phase7): implement frame continuity + verifier alignment; fix receipt canonical + replay parity`

This repository is currently at a stable, verified stopping point.

Do not assume local-only work exists beyond this point unless it is visible in `git status` and intentionally staged.

---

## MANDATORY OPERATING RULES

Any collaborator working in this repository must follow these rules before making changes:

1. Read this file fully before doing anything else.
2. Do not suggest changes before understanding current state.
3. Do not guess root causes.
4. Do not refactor unrelated logic.
5. Do not change multiple files without direct proof.
6. Do not modify already-working behavior unless a specific mismatch or failure is proven.
7. Preserve determinism, replayability, canonical equivalence, and fail-closed behavior.
8. Do not push to `main` with partial verification.
9. Do not rely on untracked files unless they are intentionally added and committed.
10. Do not assume future phases are active just because design ideas exist.

---

## SYSTEM SCOPE

This repository implements:

- DTPE (Digital Twin Persona Engine)
- IAL (Intent & Accountability Layer)
- SPECTRE (enforcement / boundary system)

Core system properties:

- deterministic execution
- canonical JSON construction
- cryptographic hashing
- ledger-based replay verification
- fail-closed boundary enforcement

---

## CURRENT IMPLEMENTED PHASE STATE

### Phase 6
Implemented and previously verified:
- temporal admissibility
- replayable verification path

### Phase 7
Implemented, committed, pushed, and verified:
- frame continuity
- invariant frame hashing
- sequence continuity support
- continuity metadata in receipts
- verifier receipt reconstruction alignment
- replay parity for boundary verification

Phase 7 is the current stable checkpoint.

---

## PHASE 7 AUTHORITATIVE FILES

Current Phase 7 behavior depends on these files:

- `core/phase4/pipeline.py`
- `core/phase4/receipt.py`
- `core/spectre/boundary.py`
- `core/spectre/frame_continuity.py`
- `tools/verify_ledger.py`
- `tools/test_phase5_boundary_replay_verifier.py`
- `tools/test_phase5_boundary_refusal_replay.py`
- `tools/test_phase7_frame_continuity.py`
- `tools/test_phase7_boundary_frame_path.py`
- `tools/test_phase7_pipeline_continuity.py`

If investigating behavior, read these first before proposing any change.

---

## VERIFIED PASS SET

The following commands passed at the current stable checkpoint:

python -m tools.test_phase7_frame_continuity
python -m tools.test_phase7_boundary_frame_path
python -m tools.test_phase7_pipeline_continuity
python -m tools.test_phase5_boundary_replay_verifier
python -m tools.test_phase5_boundary_refusal_replay
python -m tools.verify_ledger

Do not consider the repository stable after any change unless this full set passes again.

---

## REQUIRED INVESTIGATION METHOD FOR FUTURE FAILURES

If canonical mismatch or replay mismatch appears again, use this order:

1. Read the relevant source files fully.
2. Extract actual runtime structure.
3. Extract verifier reconstruction structure.
4. Compare field-by-field.
5. Compare against actual ledger payload.
6. Prove exact mismatch before changing code.
7. Change only the responsible file.
8. Re-run the full verification set.

Do not patch by intuition.
Do not fix forward without proof.

If `receipt_canonical` fails, the structures are not identical.

Find the difference first.

---

## FILE INTEGRITY RULES

Before any future implementation work:

1. Run `git status --short`
2. Confirm all referenced files exist locally
3. Confirm Python is resolving the intended local files
4. Confirm no temp/debug files are influencing behavior
5. Confirm no untracked critical files are being silently relied on

Temporary debug scripts must not remain in the repository.

---

## PRE-PUSH REQUIREMENT

Do not push to `main` unless all are true:

- repository state is intentional
- no debug artifacts remain
- no partial edits remain
- full verification pass set succeeds
- ledger verification passes
- replay verification passes
- canonical equivalence is preserved
- `git status --short` shows only intended staged changes before commit
- post-commit repo state is clean

---

## HANDOFF SUMMARY

This repository is currently in a good state.

Authoritative checkpoint:

- Phase 7 implemented
- Phase 7 verified
- replay verifier passing
- refusal replay passing
- ledger verification passing
- commit pushed to `origin/main`

Any collaborator must preserve this baseline unless a change is directly proven, minimal, and re-verified end-to-end.
