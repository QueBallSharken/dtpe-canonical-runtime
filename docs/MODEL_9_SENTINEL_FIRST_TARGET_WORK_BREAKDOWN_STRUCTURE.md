# MODEL 9 SENTINEL FIRST TARGET WORK BREAKDOWN STRUCTURE

## Status

This file is a repo-specific work breakdown structure for the bounded Model 9 / SPECTRE-SENTINEL first target.

It is derived from:
- docs/MODEL_9_SENTINEL_DOC_INDEX.md
- docs/MODEL_9_SENTINEL_FIRST_INCORPORATION_TARGET.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_ACCEPTANCE_RULES.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_IMPLEMENTATION_CHECKLIST.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_PROOF_HARNESS_OUTLINE.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_TEST_CASE_CATALOG.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_PHASED_IMPLEMENTATION_PLAN.md

It translates the bounded first-target package into concrete repo work groups and dependencies.

This file is planning-facing only.

It does not authorize broader claims.
It does not replace the canonical architecture documents.
It does not imply that implementation is already complete.

---

## 1. Purpose

This artifact defines the repo-specific work breakdown structure for the bounded Model 9 / SPECTRE-SENTINEL first target.

It defines:
- concrete work packages
- package dependencies
- likely repo work surfaces
- proof and acceptance mapping
- out-of-scope controls
- completion sequencing

It exists to bridge:
- canonical architecture docs
- repo implementation work
- proof and acceptance work

---

## 2. Governing Rule

The work breakdown must preserve the bounded first-target ceiling.

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

No work package may silently broaden the target beyond that ceiling.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For the work breakdown, this means:
- no work package may assume a structurally legacy-only crypto posture
- where crypto posture is relevant to the claim, it must be surfaced and evaluated
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- repo work must not create a first target that would require redesign from scratch to remain PQC-ready

This file does not require a full PQC migration program by itself.

It does require that bounded first-target work preserve PQC-ready posture as active architecture, not as a later note.

---

## 5. Repo-Specific Planning Rule

This work breakdown is repo-specific in sequencing and task grouping, but it is intentionally conservative about exact code-file assignment.

Reason:
- the repo must remain the source of truth
- file assignment must be validated against current repo state before code mutation
- planning must not hard-code file paths that have not been re-verified in the live repo state

Accordingly, this file uses two categories:

### 5.1 Confirmed repo planning surfaces
These are safe planning surfaces already established:
- docs/

### 5.2 Candidate implementation surfaces
These are likely implementation areas that must be validated against current repo state before code changes:
- core/
- tools/
- test or verification surfaces already present in the repo
- any receipt / replay / evidence surfaces already used by the runtime

No candidate surface becomes authoritative implementation assignment until verified against the current repo state.

---

## 6. Work Package Overview

The bounded first-target work is divided into these work packages:

- WP0 - Documentation Baseline Lock
- WP1 - First-Target Scope Binding
- WP2 - Identity / Authority / Invariant Binding Surfaces
- WP3 - Covered Boundary / Refusal Surface
- WP4 - Timing Qualification Surface
- WP5 - Claim-Relevant Crypto / PQC Surface
- WP6 - State / Downgrade Surface
- WP7 - Evidence Emission Surface
- WP8 - Replay Surface
- WP9 - Proof Harness / Test Realization
- WP10 - Acceptance Evaluation Surface
- WP11 - Claim-Language Lock and Repo Presentation

These packages must be executed in dependency order.

---

## 7. Work Package Detail

## WP0 - Documentation Baseline Lock

### Objective
Freeze the canonical doc set as the repo source of truth for the bounded first target.

### Inputs
- canonical Model 9 / Sentinel doc set
- document index

### Repo surfaces
- docs/

### Tasks
- confirm the canonical split set exists in repo
- confirm the document index exists in repo
- confirm the bounded first-target ceiling is explicit
- confirm PQC-ready requirement is explicit in the doc set

### Completion evidence
- canonical docs present
- index present
- no missing split-core artifact
- repo can be used as source-of-truth entry point

### Dependencies
- none

### Out of scope
- implementation mutation
- proof execution
- claim broadening

---

## WP1 - First-Target Scope Binding

### Objective
Bind the first target to one explicit repo-backed bounded segment definition.

### Inputs
- first incorporation target doc
- acceptance rules
- implementation checklist

### Repo surfaces
- docs/
- candidate implementation surfaces to be validated before code assignment

### Tasks
- identify the exact bounded segment to target first
- identify the exact covered mutation-capable boundary to target first
- identify the exact claimed irreversible primitive for that segment
- identify the exact claim limitation statement that must govern implementation
- record repo-specific decision on what is explicitly outside first-target scope

### Completion evidence
- one exact bounded target statement
- one exact covered boundary target statement
- one exact non-claim boundary statement for repo work

### Dependencies
- WP0

### Out of scope
- second boundary
- workflow-wide accompaniment
- downstream universal continuity

---

## WP2 - Identity / Authority / Invariant Binding Surfaces

### Objective
Map the bounded first target onto one governed transition identity, one authority basis, and one invariant basis.

### Inputs
- tightening spec
- conformance and classification rules
- state model
- first-target implementation checklist

### Repo surfaces
- candidate implementation surfaces in core/
- candidate verification surfaces in tools/
- docs/

### Tasks
- identify the repo-level representation of governed transition identity
- identify the repo-level representation of authority basis
- identify the repo-level representation of invariant basis
- define how those become bound for the first target
- define what continuity loss would look like for each

### Completion evidence
- repo-specific identity binding plan
- repo-specific authority binding plan
- repo-specific invariant binding plan
- explicit continuity-loss conditions

### Dependencies
- WP1

### Out of scope
- successor-chain support
- multi-authority coordination
- dynamic invariant replacement beyond first-target need

---

## WP3 - Covered Boundary / Refusal Surface

### Objective
Identify and realize one real refusal-capable covered boundary for the first target.

### Inputs
- first incorporation target doc
- implementation checklist
- proof harness outline

### Repo surfaces
- candidate runtime enforcement surfaces in core/
- candidate verification surfaces in tools/
- docs/

### Tasks
- identify the exact repo surface that corresponds to the covered boundary
- identify the exact refusal-capable control point for that boundary
- define the difference between observation and real refusal at that point
- define how refusal success and refusal failure will be surfaced

### Completion evidence
- one exact covered boundary assignment
- one exact refusal surface assignment
- proof that the boundary is not advisory-only by design
- explicit statement of what mutation is prevented at that point

### Dependencies
- WP2

### Out of scope
- multiple covered boundaries
- downstream path governance
- broad continuous accompaniment claims

---

## WP4 - Timing Qualification Surface

### Objective
Make timeliness a real repo-level evaluable condition rather than a narrative claim.

### Inputs
- conformance and classification rules
- state model
- replay rules
- implementation checklist

### Repo surfaces
- candidate runtime ordering / event surfaces
- candidate evidence / receipt surfaces
- candidate verification surfaces in tools/

### Tasks
- identify how refusal-ready state is represented
- identify how mutation-completion relation is represented
- define the ordering basis required for first-target timing qualification
- define timing-failure evidence and downgrade behavior

### Completion evidence
- repo-specific timing qualification plan
- explicit timing-failure path
- replay-visible timing outcome

### Dependencies
- WP3

### Out of scope
- general performance benchmarking
- broad timing guarantees outside the first target

---

## WP5 - Claim-Relevant Crypto / PQC Surface

### Objective
Preserve active PQC-ready posture and claim-relevant crypto discipline in the bounded first target.

### Inputs
- tightening spec
- evidence schema
- replay rules
- minimal architecture profile
- implementation checklist

### Repo surfaces
- candidate crypto / signature / evidence integrity surfaces
- candidate replay / verifier surfaces
- docs/

### Tasks
- identify where claim-relevant crypto posture exists in the repo architecture
- define whether the first target actually depends on claim-relevant crypto posture
- if yes, define how that crypto posture is surfaced, evaluated, and downgraded on failure
- ensure the first target does not hard-code a structurally legacy-only posture
- ensure replay can see claim-relevant crypto posture where applicable

### Completion evidence
- repo-specific claim-relevant crypto handling plan
- explicit crypto qualification or crypto non-relevance statement for the bounded first target
- fail-closed crypto mismatch behavior where applicable

### Dependencies
- WP2
- WP4

### Out of scope
- full PQC migration program
- broad crypto-agility completion program
- unrelated multi-profile crypto redesign

---

## WP6 - State / Downgrade Surface

### Objective
Realize the minimum first-target state machine and fail-closed downgrade behavior in repo terms.

### Inputs
- state model
- conformance and classification rules
- implementation checklist

### Repo surfaces
- candidate state / decision surfaces in core/
- candidate verification surfaces in tools/
- docs/

### Tasks
- map first-target states to repo implementation surfaces
- map downgrade triggers to repo implementation surfaces
- ensure no stronger claim can survive by omission
- include claim-relevant crypto-failure state path where applicable

### Completion evidence
- repo-specific state mapping
- repo-specific downgrade mapping
- explicit fail-closed behavior for:
  - refusal failure
  - timing failure
  - coverage loss
  - evidence insufficiency
  - crypto failure where applicable

### Dependencies
- WP3
- WP4
- WP5

### Out of scope
- multi-boundary state expansion
- workflow-wide continuity state expansion

---

## WP7 - Evidence Emission Surface

### Objective
Emit enough repo-backed evidence to support bounded replay and acceptance.

### Inputs
- evidence schema
- state model
- implementation checklist

### Repo surfaces
- candidate receipt / evidence surfaces
- candidate ledger / verification surfaces already used by the repo
- candidate tooling in tools/

### Tasks
- map required evidence fields to repo surfaces
- identify which evidence is already available
- identify missing evidence required for first target
- ensure claim-relevant crypto evidence is surfaced where applicable
- ensure downgrade evidence is explicit

### Completion evidence
- repo-specific evidence field map
- explicit list of new evidence outputs required
- explicit replay input coverage list

### Dependencies
- WP6

### Out of scope
- generalized audit fabric beyond first-target need
- unrelated evidence expansion

---

## WP8 - Replay Surface

### Objective
Enable deterministic replay of the bounded first-target claim from repo-backed evidence only.

### Inputs
- replay rules
- evidence schema
- implementation checklist
- test case catalog

### Repo surfaces
- candidate verifier / replay tools
- candidate evidence readers
- tools/

### Tasks
- map replay inputs to repo evidence
- define first-target replay pass/fail logic
- define replay downgrade logic
- define crypto-aware replay handling where applicable
- define replay output for strongest supported class

### Completion evidence
- repo-specific replay mapping
- replay support for stronger/lower class differentiation
- replay handling for evidence insufficiency and crypto failure where applicable

### Dependencies
- WP7

### Out of scope
- generalized omniscient replay
- hidden-context replay repair
- broader workflow replay beyond bounded scope

---

## WP9 - Proof Harness / Test Realization

### Objective
Convert the proof harness outline and test case catalog into actual repo-level verification work.

### Inputs
- proof harness outline
- test case catalog
- acceptance rules

### Repo surfaces
- tools/
- candidate test runner surfaces already present in repo
- docs/

### Tasks
- map each mandatory first-target test to repo execution steps
- define nominal bounded success path test
- define refusal ineffective test
- define refusal untimely test
- define coverage loss test
- define missing evidence test
- define scope inflation rejection test
- define PQC readiness and crypto-failure tests where applicable

### Completion evidence
- repo-specific test mapping for mandatory tests
- explicit expected outcome for each mandatory test
- explicit replay confirmation step for each mandatory test

### Dependencies
- WP8

### Out of scope
- extra test expansion unrelated to first-target acceptance
- broad integration test matrix beyond the bounded target

---

## WP10 - Acceptance Evaluation Surface

### Objective
Create the repo-backed acceptance decision path for the bounded first target.

### Inputs
- acceptance rules
- proof harness outline
- test case catalog
- phased implementation plan

### Repo surfaces
- docs/
- tools/
- candidate acceptance or verification runner surfaces

### Tasks
- define the acceptance checklist in repo-executable terms
- map each acceptance pass condition to repo evidence or test result
- map each rejection condition to repo evidence or test result
- define claim ceiling enforcement in acceptance output
- include claim-relevant crypto acceptance handling where applicable

### Completion evidence
- repo-specific acceptance matrix
- repo-specific pass/fail decision logic
- explicit statement of strongest allowed accepted claim

### Dependencies
- WP9

### Out of scope
- broader program certification
- workflow-wide acceptance

---

## WP11 - Claim-Language Lock and Repo Presentation

### Objective
Ensure repo presentation does not exceed the bounded first-target ceiling.

### Inputs
- first incorporation target
- acceptance rules
- phased implementation plan
- document index

### Repo surfaces
- docs/
- any README or presentation surfaces only if intentionally updated

### Tasks
- define the exact allowed repo wording for first-target status
- define forbidden overclaim wording
- ensure PQC-ready posture is framed as active architecture requirement, not decorative note
- ensure the repo entry point points readers to the bounded first-target package

### Completion evidence
- repo-safe claim language
- forbidden wording list
- index / navigation consistency

### Dependencies
- WP10

### Out of scope
- public claim expansion
- marketing-style restatement
- broader capability claims

---

## 8. Dependency Graph Summary

Minimum dependency order:

- WP0
- WP1
- WP2
- WP3
- WP4
- WP5
- WP6
- WP7
- WP8
- WP9
- WP10
- WP11

Critical dependency points:
- no refusal work before scope and binding
- no stronger claim before timing
- no crypto-dependent stronger claim before crypto handling
- no replay before evidence
- no acceptance before proof harness realization
- no broader wording after acceptance

---

## 9. Acceptance Mapping

The work breakdown is complete only when it can satisfy the first-target acceptance package.

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

No work package should be counted complete merely because code exists.

Completion is tied to acceptance-relevant evidence and proof.

---

## 10. Out-of-Scope Controls

The following remain out of scope for this work breakdown unless explicitly opened later:
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

## 11. Direct Recommendation

The correct use of this work breakdown is:

- use the canonical doc set as the authority
- use this file to break repo work into concrete packages
- validate candidate implementation surfaces against current repo state before mutating code
- keep every package within the bounded first-target ceiling
- do not let the untracked Phase 9 test file become mixed into this package unless you intentionally decide it belongs to this work

That is the correct next planning layer.

---

## 12. Immediate Follow-On

The next useful artifact after this one is not another architecture split file.

The next useful artifact is either:
- a repo-specific implementation task list
- or a repo-specific acceptance execution checklist

Choose only one next and keep it bounded to the first target.