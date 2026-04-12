# MODEL 9 SENTINEL FIRST TARGET PHASED IMPLEMENTATION PLAN

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_IMPLEMENTATION_CHECKLIST.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_TEST_CASE_CATALOG.md

It defines a repo-agnostic phased implementation plan for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines a repo-agnostic phased implementation plan for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It is not a proof artifact.
It is not an acceptance artifact.

It is the build sequence that should produce the bounded first target already defined.

It defines:
- implementation phases
- objective of each phase
- mandatory outputs of each phase
- phase completion gates
- what must not be broadened in that phase
- how PQC-on / PQC-ready posture must remain preserved

---

## 2. Governing Implementation Rule

Build the smallest architecture slice that can honestly support one explicitly bounded accompanied segment with:
- one covered mutation-capable boundary
- one governed transition identity
- one authority basis
- one invariant basis
- one mechanically effective and timely refusal surface
- fail-closed downgrade behavior
- replay-sufficient evidence
- claim-relevant crypto posture where applicable
- PQC-ready crypto posture preserved as an active requirement

No phase may broaden the claim beyond that target.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Phase Ordering Rule

The phases must be executed in this order:

1. Scope Lock
2. Identity / Authority / Invariant Binding
3. Covered Boundary and Refusal Surface
4. Timing Qualification
5. Claim-Relevant Crypto Handling
6. State and Downgrade Model
7. Evidence Emission
8. Replay Path
9. Acceptance Harness Execution
10. Claim-Language Lock

This order matters.

Reason:
- scope must be fixed before binding
- binding must exist before refusal can count as governance
- refusal must exist before timing can matter
- crypto handling must exist before crypto-dependent stronger claims can stand
- state and downgrade must exist before evidence is meaningful
- evidence must exist before replay
- replay must exist before acceptance
- acceptance must exist before public claim language

---

## 5. Standing PQC Rule Across All Phases

Every phase must preserve this architectural requirement:

PQC must be on and always at the ready.

For this plan, that means:
- no phase may hard-code the first target into a legacy-only cryptographic posture
- no phase may define evidence or replay in a way that hides claim-relevant crypto posture
- no phase may make future PQC readiness dependent on redesigning the first-target architecture from scratch
- where crypto posture is relevant to the bounded claim, mismatch or unsupported posture must remain fail-closed

This does not require full PQC rollout in the first target unless explicitly claimed.

It does require first-target architecture to remain PQC-ready in structure, evidence posture, and replay posture.

---

## 6. Phase 1 - Scope Lock

### 6.1 Objective

Lock the exact first-target shape so implementation cannot drift.

### 6.2 Mandatory outputs

This phase must produce an explicit bounded target definition containing:
- one segment identifier
- one segment start condition
- one segment end condition
- one scope statement
- one covered mutation-capable boundary
- one claimed irreversible primitive for that segment
- one governed transition identity model
- one authority basis model
- one invariant basis model
- one explicit non-claim boundary statement
- one crypto posture statement preserving PQC-on / PQC-ready treatment where claim-relevant

### 6.3 Must not broaden in this phase

Do not broaden to:
- multiple boundaries
- end-to-end continuity
- downstream continuity
- authority succession
- invariant succession
- identity successor transfer
- alternate-path closure beyond exact bounded scope
- full Model 9 implementation
- full PQC migration
- full crypto-agility completion

### 6.4 Completion gate

Phase 1 is complete only if the first target can be stated in one sentence without ambiguity and without broader implied scope.

---

## 7. Phase 2 - Identity / Authority / Invariant Binding

### 7.1 Objective

Create the minimum governance-binding basis that makes accompaniment more than observation.

### 7.2 Mandatory outputs

This phase must implement or define:
- one governed transition identity
- one accompaniment instance identity, if distinct
- one identity binding relation
- one authority basis identifier
- one authority binding relation
- one invariant basis identifier
- one invariant binding relation
- continuity status for identity, authority, and invariant across the exact segment

### 7.3 Required architectural effect

After this phase, the segment must be able to answer:
- which transition is governed
- which authority governs it
- which invariant governs it
- whether those are merely declared or actually bound

### 7.4 Must not broaden in this phase

Do not add:
- successor chains
- multi-authority coordination
- dynamic invariant replacement
- multi-segment continuity stitching

### 7.5 Completion gate

Phase 2 is complete only if replay could identify one governed transition, one authority basis, and one invariant basis bound to the segment without relying on narrative explanation.

---

## 8. Phase 3 - Covered Boundary and Refusal Surface

### 8.1 Objective

Establish one real covered mutation-capable boundary and one real refusal-capable surface.

### 8.2 Mandatory outputs

This phase must implement or define:
- one covered boundary identifier
- one segment-to-boundary association
- one claimed irreversible primitive for the exact segment
- one refusal path identifier
- one refusal-path-to-boundary association
- one refusal activation state
- one refusal result state
- explicit statement that broader boundary coverage is not claimed

### 8.3 Required architectural effect

After this phase, the system must be able to distinguish:
- observed boundary
- covered boundary
- refusal-capable boundary

and must show that the refusal path is mechanically relevant to the covered boundary.

### 8.4 PQC requirement in this phase

If authority or evidence validity depends on crypto posture for the bounded claim, the refusal-governance slice must not silently ignore crypto posture. It must remain compatible with fail-closed crypto posture evaluation.

### 8.5 Must not broaden in this phase

Do not add:
- multiple covered boundaries
- downstream path claims
- generalized continuous governance wording

### 8.6 Completion gate

Phase 3 is complete only if one covered boundary can be identified and one refusal surface can actually prevent mutation at that exact boundary within the first-target scope.

---

## 9. Phase 4 - Timing Qualification

### 9.1 Objective

Prove that refusal is not only present, but timely relative to mutation completion.

### 9.2 Mandatory outputs

This phase must implement or define:
- ordering basis or equivalent
- refusal-ready status
- mutation-completion relation
- timing qualification result
- timing-failure result path

### 9.3 Required architectural effect

After this phase, the system must be able to answer:
- was refusal live
- was refusal timely
- if not timely, what is the resulting classification ceiling

### 9.4 Must not broaden in this phase

Do not turn timing qualification into:
- informal reasoning
- post-hoc narrative
- broad performance claims beyond the bounded segment

### 9.5 Completion gate

Phase 4 is complete only if the architecture can distinguish:
- refusal exists and is timely
- refusal exists but is untimely
- refusal does not qualify

without ambiguity.

---

## 10. Phase 5 - Claim-Relevant Crypto Handling

### 10.1 Objective

Ensure that claim-relevant crypto posture is surfaced, evaluated, and fail-closed where applicable.

### 10.2 Mandatory outputs

Where crypto posture is relevant to the claim, this phase must implement or define:
- claim-relevant crypto posture identifier
- crypto qualification state
- crypto qualification event
- crypto failure event
- crypto downgrade or fail-closed path
- replay-visible crypto evidence

### 10.3 Required architectural effect

After this phase, the system must be able to answer:
- what crypto posture is relevant to the claim
- whether it qualified
- if not, whether the stronger claim correctly failed closed

### 10.4 Must not broaden in this phase

Do not turn this phase into:
- a full PQC migration program
- a full crypto-agility rollout
- a broad multi-profile implementation program unrelated to the bounded first target

### 10.5 Completion gate

Phase 5 is complete only if a crypto-dependent stronger claim cannot survive on hidden, unsupported, or mismatched crypto posture.

---

## 11. Phase 6 - State and Downgrade Model

### 11.1 Objective

Ensure stronger claims fail closed instead of surviving by inertia.

### 11.2 Mandatory outputs

This phase must implement or define the minimum first-target state model:
- Uninitialized
- Segment-Declared
- Identity-Bound
- Authority-Bound
- Coverage-Established
- Refusal-Live
- Crypto-Qualified where claim-relevant
- Actively-Accompanying
- Advisory-Only
- Coverage-Lost
- Crypto-Failed where claim-relevant
- Unverifiable
- Failed-Closed
- Completed

It must also define downgrade behavior for at least:
- refusal failure
- timing failure
- coverage loss
- evidence insufficiency
- crypto failure where claim-relevant

### 11.3 Required architectural effect

After this phase, the system must not be able to preserve a stronger class after a defeating condition appears.

### 11.4 Must not broaden in this phase

Do not add:
- extensive multi-branch state systems unrelated to the first target
- later-phase multi-boundary logic
- workflow-wide continuity states

### 11.5 Completion gate

Phase 6 is complete only if every stronger first-target class has an explicit downgrade path and fail-closed behavior.

---

## 12. Phase 7 - Evidence Emission

### 12.1 Objective

Surface enough evidence for replay and independent verification.

### 12.2 Mandatory outputs

This phase must emit, at minimum:
- segment declaration record
- segment scope statement
- governed transition identity record
- authority basis record
- authority binding record
- invariant basis record
- invariant binding record
- covered boundary record
- claimed irreversible primitive record
- refusal path record
- refusal-live record
- timing qualification record
- active-state record
- downgrade records
- completion record
- final classification record
- evidence sufficiency record
- crypto posture record where claim-relevant
- crypto qualification or crypto failure record where claim-relevant

### 12.3 Required architectural effect

After this phase, the claim must be reconstructable from surfaced evidence rather than hidden runtime state.

### 12.4 PQC requirement in this phase

Evidence must not be structured in a way that makes claim-relevant crypto posture invisible. PQC-ready posture must remain expressible in the evidence model.

### 12.5 Must not broaden in this phase

Do not over-expand evidence into a generalized full-system audit fabric unless needed for the exact bounded target.

### 12.6 Completion gate

Phase 7 is complete only if every mandatory first-target claim element exists as explicit evidence usable by replay.

---

## 13. Phase 8 - Replay Path

### 13.1 Objective

Allow independent re-evaluation of the bounded claim from surfaced evidence only.

### 13.2 Mandatory outputs

This phase must implement or define replay sufficient to determine:
- claimed segment
- claimed scope
- governed transition identity
- authority basis
- invariant basis
- covered boundary
- claimed irreversible primitive
- refusal-live status
- timing qualification
- downgrade events
- evidence sufficiency
- strongest supported final class
- crypto posture result where claim-relevant

### 13.3 Required architectural effect

After this phase, the system must be able to reject stronger unsupported claims even if emitted by runtime.

### 13.4 Must not broaden in this phase

Do not turn replay into:
- system-wide omniscience
- hidden-context reconstruction
- narrative repair engine

### 13.5 Completion gate

Phase 8 is complete only if replay can deterministically select the strongest justified class for the exact bounded first-target scope.

---

## 14. Phase 9 - Acceptance Harness Execution

### 14.1 Objective

Run the bounded target through required positive and negative proof scenarios.

### 14.2 Mandatory outputs

This phase must exercise at least the mandatory tests from the earlier catalog:
- nominal bounded active segment
- explicit claim limitation
- refusal ineffective leading to downgrade
- refusal untimely leading to downgrade
- coverage loss leading to fail-closed behavior
- missing mandatory evidence causing stronger claim rejection
- evidentiary ceiling enforcement
- silent stronger-claim persistence defeat by replay
- PQC-ready crypto posture preservation
- crypto posture replay visibility where claim-relevant
- crypto posture mismatch fail-closed where claim-relevant

### 14.3 Required architectural effect

After this phase, the architecture must have shown both:
- positive bounded support
- negative discipline against overclaim

### 14.4 Completion gate

Phase 9 is complete only if the acceptance matrix passes for the bounded first target.

---

## 15. Phase 10 - Claim-Language Lock

### 15.1 Objective

Prevent successful bounded implementation from being mislabeled as something broader.

### 15.2 Mandatory outputs

This phase must lock:

Permitted wording:
- bounded Model 9 segment accompaniment
- single covered boundary
- replay-verifiable bounded scope
- fail-closed downgrade discipline
- PQC-ready architectural posture preserved
- claim-relevant crypto handling where applicable

Forbidden wording:
- full Model 9 implementation
- end-to-end accompaniment
- universal downstream continuity
- full BBIS closure
- all mutation paths governed
- continuous governance solved
- full PQC migration completion
- full crypto-agility completion

### 15.3 Required architectural effect

After this phase, public and internal framing must match the first-target ceiling.

### 15.4 Completion gate

Phase 10 is complete only if no supported claim exceeds the strongest replay-validated bounded class.

---

## 16. Phase-by-Phase Deliverable Summary

| Phase | Deliverable |
|---|---|
| 1 | exact bounded target definition |
| 2 | identity / authority / invariant binding basis |
| 3 | one covered boundary and one real refusal surface |
| 4 | timing qualification logic |
| 5 | claim-relevant crypto qualification and failure handling |
| 6 | fail-closed state and downgrade model |
| 7 | mandatory evidence emission |
| 8 | deterministic replay path |
| 9 | acceptance harness results |
| 10 | locked claim-language ceiling |

---

## 17. Mandatory Phase Gates

The project must not advance past a phase unless its gate is met.

### Gate A
Do not start refusal or replay work before scope is locked.

### Gate B
Do not count accompaniment as governance before identity, authority, and invariant are bound.

### Gate C
Do not count refusal as active accompaniment before timing is qualified.

### Gate D
Do not count a crypto-dependent stronger claim before claim-relevant crypto posture is qualified.

### Gate E
Do not count runtime success as sufficient before downgrade behavior exists.

### Gate F
Do not count evidence emission as sufficient before replay can use it.

### Gate G
Do not count implementation as accepted before the proof harness passes.

### Gate H
Do not broaden claim language after acceptance.

---

## 18. Mandatory Out-of-Scope Controls

Throughout all phases, keep the following out of scope unless explicitly opened later:
- multi-boundary active accompaniment
- workflow-wide accompaniment
- downstream universal continuity
- identity successor transfer
- authority succession
- invariant succession
- generalized alternate-path closure
- full PQC migration program
- full crypto-agility program beyond bounded first-target requirements
- full Model 9 implementation
- full BBIS closure

---

## 19. Phase Completion Definition

The phased plan is complete only if:
- the first-target bounded segment exists
- one covered mutation-capable boundary is real and explicit
- one governed transition identity is bound
- one authority basis is bound
- one invariant basis is bound
- refusal is mechanically effective
- refusal is timely
- downgrade is fail-closed
- evidence is surfaced
- replay validates the bounded claim
- claim-relevant crypto posture is handled where applicable
- PQC-on / PQC-ready posture remains preserved
- claim language remains within the bounded ceiling

If any one of those is missing, the phased implementation plan has not yet reached first-target completion.

---

## 20. Direct Recommendation

Build to Tier 3 bounded active segment accompaniment first.

Do not spend first-target effort on breadth.

Spend it on:
- one real governed slice
- one real refusal boundary
- one real replay path
- one real downgrade model
- one real crypto posture that stays PQC-ready and fail-closed where claim-relevant

That is the right implementation plan.

---

## 21. Canonical Split Note

With this file written, the first planned canonical split set for the Model 9 / SPECTRE-SENTINEL bounded first-target package is complete.

Any follow-on artifacts after this should be new extension artifacts, not missing split-core artifacts.