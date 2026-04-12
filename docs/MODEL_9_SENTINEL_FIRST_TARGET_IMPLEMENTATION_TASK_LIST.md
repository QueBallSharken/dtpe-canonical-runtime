# MODEL 9 SENTINEL FIRST TARGET IMPLEMENTATION TASK LIST

## Status

This file is a repo-specific implementation task list for the bounded Model 9 / SPECTRE-SENTINEL first target.

It is derived from:
- docs/MODEL_9_SENTINEL_DOC_INDEX.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_WORK_BREAKDOWN_STRUCTURE.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_IMPLEMENTATION_CHECKLIST.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_ACCEPTANCE_RULES.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_TEST_CASE_CATALOG.md

It converts the work breakdown structure into concrete task groups and ordered execution tasks.

This file is planning-facing only.

It does not broaden claims.
It does not replace the canonical architecture documents.
It does not imply that implementation is already complete.

---

## 1. Purpose

This artifact defines the concrete repo-specific task list for the bounded Model 9 / SPECTRE-SENTINEL first target.

It defines:
- ordered task groups
- task dependencies
- likely repo work surfaces
- acceptance mapping
- out-of-scope controls
- completion conditions

It exists to bridge:
- architecture documents
- repo work sequencing
- proof and acceptance execution

---

## 2. Governing Rule

Every task in this file must preserve the bounded first-target ceiling.

That means the work is only for:
- one explicitly bounded segment
- one explicitly covered mutation-capable boundary
- one governed transition identity
- one authority basis
- one invariant basis
- one mechanically effective and timely refusal surface
- fail-closed downgrade behavior
- replay-sufficient evidence
- claim-relevant crypto handling where applicable
- PQC-ready posture preserved as an active requirement

No task may silently broaden the target beyond that ceiling.

---

## 3. Standing Architectural Requirement

PQC must be on and always at the ready.

For this task list, that means:
- no task may assume a structurally legacy-only crypto posture
- where crypto posture is relevant to the claim, it must be surfaced and evaluated
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- first-target work must not require redesign from scratch to remain PQC-ready

This file does not require a full PQC migration program by itself.

It does require that bounded first-target work preserve PQC-ready posture as active architecture, not as a future note.

---

## 4. Repo-Specific Planning Rule

This task list is repo-specific in sequencing and task grouping, but intentionally conservative about exact code-file assignment.

Use these planning categories:

### 4.1 Confirmed planning surface
- docs/

### 4.2 Candidate implementation surfaces to verify before code mutation
- core/
- tools/
- existing evidence / receipt / ledger / verifier surfaces already used by the repo
- existing replay / verification tooling already used by the repo

No candidate surface becomes authoritative implementation assignment until validated against live repo state.

---

## 5. Ordered Task Groups

Execute these task groups in order:

- TG0 - Documentation Baseline Check
- TG1 - First-Target Scope Freeze
- TG2 - Identity / Authority / Invariant Surface Mapping
- TG3 - Covered Boundary / Refusal Surface Mapping
- TG4 - Timing Qualification Mapping
- TG5 - Claim-Relevant Crypto / PQC Mapping
- TG6 - State / Downgrade Mapping
- TG7 - Evidence Mapping
- TG8 - Replay Mapping
- TG9 - Proof Harness Realization
- TG10 - Acceptance Execution
- TG11 - Claim-Language Lock

Do not skip dependency order.

---

## 6. Task Group Detail

## TG0 - Documentation Baseline Check

### Objective
Confirm that the repo already contains the canonical bounded first-target document set.

### Likely repo surfaces
- docs/

### Tasks
- [ ] Confirm the document index exists
- [ ] Confirm the consolidation seed exists
- [ ] Confirm the canonical split set exists
- [ ] Confirm the first-target package exists
- [ ] Confirm the work breakdown structure exists
- [ ] Confirm PQC-ready requirement is explicit in the document set

### Done when
- the repo has a complete bounded first-target documentation baseline
- the repo can be used as source of truth without relying on thread history

### Dependencies
- none

---

## TG1 - First-Target Scope Freeze

### Objective
Freeze one exact bounded first target for repo work.

### Likely repo surfaces
- docs/
- candidate runtime surfaces to validate before code mutation

### Tasks
- [ ] Identify the exact bounded segment to target first
- [ ] Identify the exact covered mutation-capable boundary
- [ ] Identify the exact claimed irreversible primitive for that segment
- [ ] Write the explicit non-claim boundary for repo work
- [ ] Confirm that second-boundary and end-to-end claims are outside scope
- [ ] Record whether crypto posture is claim-relevant for this exact first target

### Done when
- one exact bounded target statement exists
- one exact covered boundary target exists
- one explicit non-claim boundary exists
- crypto relevance for the first target is explicitly stated

### Dependencies
- TG0

---

## TG2 - Identity / Authority / Invariant Surface Mapping

### Objective
Map the first target onto one governed transition identity, one authority basis, and one invariant basis.

### Likely repo surfaces
- candidate core/ surfaces
- candidate tools/ verification surfaces
- docs/

### Tasks
- [ ] Identify the repo-level representation of governed transition identity
- [ ] Identify the repo-level representation of authority basis
- [ ] Identify the repo-level representation of invariant basis
- [ ] Define how the three become bound for the first target
- [ ] Define identity continuity loss condition
- [ ] Define authority continuity loss condition
- [ ] Define invariant continuity loss condition

### Done when
- repo-specific identity binding plan exists
- repo-specific authority binding plan exists
- repo-specific invariant binding plan exists
- continuity-loss conditions are explicit

### Dependencies
- TG1

---

## TG3 - Covered Boundary / Refusal Surface Mapping

### Objective
Map the first target to one real covered boundary and one real refusal-capable surface.

### Likely repo surfaces
- candidate runtime enforcement surfaces in core/
- candidate tools/ verification surfaces
- docs/

### Tasks
- [ ] Identify the exact repo surface corresponding to the covered boundary
- [ ] Identify the exact refusal-capable control point
- [ ] Define what counts as mechanical refusal at that point
- [ ] Define what does not count as refusal at that point
- [ ] Define refusal success evidence
- [ ] Define refusal failure evidence
- [ ] Confirm broader boundary coverage is not being claimed

### Done when
- one exact covered boundary assignment exists
- one exact refusal surface assignment exists
- advisory-only behavior is distinguished from real refusal

### Dependencies
- TG2

---

## TG4 - Timing Qualification Mapping

### Objective
Make timeliness a real repo-evaluable condition.

### Likely repo surfaces
- candidate runtime ordering surfaces
- candidate evidence / receipt surfaces
- candidate tools/ verification surfaces

### Tasks
- [ ] Identify how refusal-ready state is represented
- [ ] Identify how mutation completion is represented
- [ ] Define the ordering basis for timing qualification
- [ ] Define timing-pass condition
- [ ] Define timing-failure condition
- [ ] Define timing-failure downgrade behavior

### Done when
- repo-specific timing qualification plan exists
- timing-pass and timing-failure conditions are explicit
- replay-visible timing output is defined

### Dependencies
- TG3

---

## TG5 - Claim-Relevant Crypto / PQC Mapping

### Objective
Preserve active PQC-ready posture and claim-relevant crypto discipline.

### Likely repo surfaces
- candidate crypto / signature / evidence integrity surfaces
- candidate verifier / replay surfaces
- docs/

### Tasks
- [ ] Decide whether crypto posture is claim-relevant for this exact first target
- [ ] If yes, identify the relevant crypto posture surface
- [ ] Define crypto qualification condition
- [ ] Define crypto failure condition
- [ ] Define fail-closed or downgrade behavior for crypto failure
- [ ] Define replay-visible crypto evidence
- [ ] Confirm the first target does not assume a structurally legacy-only posture

### Done when
- crypto relevance is explicitly decided
- crypto qualification / failure logic exists where applicable
- PQC-ready posture is preserved structurally

### Dependencies
- TG2
- TG4

---

## TG6 - State / Downgrade Mapping

### Objective
Realize the minimum first-target state machine and fail-closed downgrade model.

### Likely repo surfaces
- candidate state / decision surfaces in core/
- candidate tools/ verification surfaces
- docs/

### Tasks
- [ ] Map Uninitialized
- [ ] Map Segment-Declared
- [ ] Map Identity-Bound
- [ ] Map Authority-Bound
- [ ] Map Coverage-Established
- [ ] Map Refusal-Live
- [ ] Map Crypto-Qualified where applicable
- [ ] Map Actively-Accompanying
- [ ] Map Advisory-Only
- [ ] Map Coverage-Lost
- [ ] Map Crypto-Failed where applicable
- [ ] Map Unverifiable
- [ ] Map Failed-Closed
- [ ] Map Completed
- [ ] Define downgrade path for refusal failure
- [ ] Define downgrade path for timing failure
- [ ] Define downgrade path for coverage loss
- [ ] Define downgrade path for evidence insufficiency
- [ ] Define downgrade path for crypto failure where applicable

### Done when
- repo-specific state mapping exists
- repo-specific downgrade mapping exists
- no stronger class can survive by omission

### Dependencies
- TG3
- TG4
- TG5

---

## TG7 - Evidence Mapping

### Objective
Map required first-target evidence to repo-backed surfaces.

### Likely repo surfaces
- candidate evidence / receipt / ledger surfaces
- candidate tools/ readers or verifiers
- docs/

### Tasks
- [ ] Map segment declaration evidence
- [ ] Map identity binding evidence
- [ ] Map authority binding evidence
- [ ] Map invariant binding evidence
- [ ] Map covered boundary evidence
- [ ] Map claimed irreversible primitive evidence
- [ ] Map refusal path evidence
- [ ] Map refusal-live evidence
- [ ] Map timing qualification evidence
- [ ] Map active-state evidence
- [ ] Map downgrade evidence
- [ ] Map completion evidence
- [ ] Map final classification evidence
- [ ] Map evidence sufficiency result
- [ ] Map claim-relevant crypto evidence where applicable

### Done when
- repo-specific evidence field map exists
- missing evidence required for first target is identified
- replay input coverage list exists

### Dependencies
- TG6

---

## TG8 - Replay Mapping

### Objective
Enable deterministic replay of the bounded first-target claim from repo-backed evidence only.

### Likely repo surfaces
- candidate verifier / replay tools
- candidate evidence readers
- tools/

### Tasks
- [ ] Map replay input set to repo evidence
- [ ] Define replay path for the nominal bounded claim
- [ ] Define replay downgrade logic
- [ ] Define replay insufficiency handling
- [ ] Define replay contradiction handling
- [ ] Define replay scope-inflation rejection
- [ ] Define replay crypto handling where applicable
- [ ] Define replay output format for strongest supported class

### Done when
- repo-specific replay mapping exists
- replay can distinguish stronger and lower classes
- replay can handle claim-relevant crypto failure where applicable

### Dependencies
- TG7

---

## TG9 - Proof Harness Realization

### Objective
Turn the proof harness outline and test case catalog into repo-level test execution work.

### Likely repo surfaces
- tools/
- candidate test runner surfaces already present in repo
- docs/

### Tasks
- [ ] Map T01 nominal bounded active segment
- [ ] Map T02 explicit claim limitation
- [ ] Map T03 refusal ineffective
- [ ] Map T04 refusal untimely
- [ ] Map T06 coverage loss
- [ ] Map T08 scope inflation attempt
- [ ] Map T09 missing mandatory evidence
- [ ] Map T12 evidentiary ceiling enforcement
- [ ] Map T15 silent stronger-claim persistence defeat
- [ ] Map T16 PQC readiness not legacy-only
- [ ] Map T17 crypto posture replay visibility
- [ ] Map T18 wrong or unsupported crypto posture fails closed
- [ ] Map T19 PQC readiness not deferred outside architecture claim boundary

### Done when
- every mandatory test has a repo execution mapping
- every mandatory test has an expected replay result
- every mandatory test has an expected final classification result

### Dependencies
- TG8

---

## TG10 - Acceptance Execution

### Objective
Create the repo-backed acceptance decision path for the bounded first target.

### Likely repo surfaces
- docs/
- tools/
- candidate acceptance or verification runner surfaces

### Tasks
- [ ] Map each acceptance pass condition to repo evidence or test output
- [ ] Map each rejection condition to repo evidence or test output
- [ ] Define repo-specific acceptance checklist
- [ ] Define repo-specific rejection reporting
- [ ] Define strongest allowed accepted claim
- [ ] Define claim-relevant crypto acceptance handling where applicable

### Done when
- repo-specific acceptance matrix exists
- repo-specific pass/fail logic exists
- strongest allowed accepted claim is explicit

### Dependencies
- TG9

---

## TG11 - Claim-Language Lock

### Objective
Ensure repo presentation does not exceed the bounded first-target ceiling.

### Likely repo surfaces
- docs/
- any README or presentation surfaces only if intentionally updated

### Tasks
- [ ] Define exact allowed wording for first-target status
- [ ] Define forbidden overclaim wording
- [ ] Confirm PQC-ready posture is framed as active architecture requirement
- [ ] Confirm the document index remains consistent
- [ ] Confirm no repo-facing language exceeds the first-target ceiling

### Done when
- repo-safe claim language exists
- forbidden wording list exists
- repo navigation and wording are aligned

### Dependencies
- TG10

---

## 7. Dependency Summary

Execution order:
- TG0
- TG1
- TG2
- TG3
- TG4
- TG5
- TG6
- TG7
- TG8
- TG9
- TG10
- TG11

Hard gates:
- no refusal work before scope and binding
- no active claim before timing qualification
- no crypto-dependent stronger claim before crypto handling
- no replay before evidence
- no acceptance before proof harness realization
- no broader repo wording after acceptance

---

## 8. Acceptance Mapping

This task list is complete only when it can satisfy the first-target acceptance package.

That means the completed work must support:
- explicit bounded segment
- explicit covered boundary
- identity / authority / invariant binding
- mechanically effective refusal
- timely refusal
- fail-closed downgrade
- replay sufficiency
- scope discipline
- claim-relevant crypto handling where applicable
- PQC-ready posture preserved as active architecture

No task group counts as complete merely because code exists.

Completion is tied to acceptance-relevant evidence and proof.

---

## 9. Out-of-Scope Controls

These remain out of scope unless explicitly opened later:
- multi-boundary accompaniment
- workflow-wide accompaniment
- downstream universal continuity
- full BBIS closure
- full Model 9 implementation
- full PQC migration program
- full crypto-agility completion
- generalized alternate-path closure
- successor-chain continuity work beyond first-target need

---

## 10. Direct Recommendation

Use this task list this way:
- keep the canonical doc set as authority
- validate candidate implementation surfaces against live repo state before mutating code
- keep every task inside the bounded first-target ceiling
- do not let unrelated work, including the untracked Phase 9 test file, get mixed into this package unless intentionally chosen

That is the correct next planning layer.

---

## 11. Immediate Follow-On

The next useful artifact after this one should be one of:
- a repo-specific acceptance execution checklist
- a repo-specific implementation task tracker

Choose only one next and keep it bounded to the first target.