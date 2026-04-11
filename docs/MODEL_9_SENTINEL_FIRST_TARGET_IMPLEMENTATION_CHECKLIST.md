# MODEL 9 SENTINEL FIRST TARGET IMPLEMENTATION CHECKLIST

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_SENTINEL_FIRST_INCORPORATION_TARGET.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_ACCEPTANCE_RULES.md

It defines the repo-agnostic implementation checklist for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the repo-agnostic implementation checklist for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It defines only:
- what must be implemented
- what is mandatory versus optional
- what evidence must be emitted
- what downgrade behavior must exist
- what replay support must exist
- what must be explicitly excluded from scope
- what counts as implementation complete
- what claim-relevant crypto handling must exist where applicable

---

## 2. Governing Implementation Rule

The first target must implement only enough architecture to prove one explicitly bounded accompanied segment with:
- one explicitly covered mutation-capable boundary
- one governed transition identity
- one authority basis
- one invariant basis
- one mechanically effective and timely refusal surface
- fail-closed downgrade handling
- replay-sufficient evidence
- claim-relevant crypto posture handling where applicable
- PQC-ready posture preserved as an active requirement

Anything beyond that is optional for the first target.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For the implementation checklist, this means:
- no first-target implementation surface may assume a structurally legacy-only crypto posture
- where crypto posture is relevant to the claim, the implementation must surface and evaluate it
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- first-target implementation must remain compatible with an active PQC-ready posture

This file does not require a full PQC migration program by itself.

It does require that first-target implementation not be architected as if PQC can be deferred without consequence.

---

## 5. First Target Scope Lock

Before implementation starts, the target scope must be locked.

### Mandatory
Implement an explicit scope definition for the first target containing:
- one segment identifier
- one segment start condition
- one segment end condition
- one scope statement
- one covered mutation-capable boundary
- one claimed irreversible primitive for that segment
- one governed transition identity model
- one authority basis model
- one invariant basis model

### Required exclusion
The first target must explicitly exclude:
- end-to-end workflow scope
- multi-boundary coverage
- multi-system continuity
- downstream universal continuity
- alternate-path closure beyond the exact bounded segment unless explicitly implemented
- authority succession
- invariant succession
- identity successor transfer
- broad Model 9 implementation claims
- full PQC migration claims
- full crypto-agility claims

### Completion criterion
Implementation is not complete unless the first target scope is explicit and bounded.

---

## 6. Mandatory Implementation Surfaces

The first target requires the following mandatory surfaces.

### 6.1 Segment Declaration Surface

Must implement a way to declare and carry:
- segment identifier
- segment scope
- segment start
- segment end
- covered boundary identifier
- claimed irreversible primitive for the segment
- authority basis identifier
- invariant basis identifier

Must not rely on:
- narrative description only
- implicit defaults
- runtime memory not surfaced as evidence

Completion criterion:
A declared segment can be created and replay can read what exact scope was claimed.

### 6.2 Governed Transition Identity Surface

Must implement a way to bind the first target segment to one stable governed transition identity.

Must include:
- governed transition identifier
- accompaniment instance identifier, if accompaniment identity is distinct
- explicit binding relation between governed transition and accompanied segment

Must not require:
- identity succession
- merged identities
- split identities
- cross-segment identity stitching

Completion criterion:
Replay can determine which exact transition was governed for the first target segment.

### 6.3 Authority Basis Surface

Must implement a way to bind the segment to one authority basis.

Must include:
- authority basis identifier
- authority binding event or state
- authority continuity status for the segment

Must not require:
- authority succession logic
- multiple authority layers unless already inherent and explicitly surfaced

Completion criterion:
Replay can determine which authority basis governed the segment and that it was bound, not merely declared.

### 6.4 Invariant Basis Surface

Must implement a way to bind the segment to one invariant basis.

Must include:
- invariant basis identifier
- invariant binding event or state
- invariant continuity status for the segment

Must not require:
- invariant succession
- dynamic invariant replacement

Completion criterion:
Replay can determine which invariant basis governed the segment and that it remained the governing basis for the claimed scope.

### 6.5 Covered Boundary Surface

Must implement a way to explicitly identify the one covered mutation-capable boundary for the first target.

Must include:
- covered boundary identifier
- association between segment and covered boundary
- statement that no broader boundary coverage is being claimed

Must not allow:
- implicit covered-boundary inference
- ambiguous multi-boundary interpretation

Completion criterion:
Replay can determine which exact boundary was covered and that broader coverage was not claimed.

### 6.6 Refusal Surface

Must implement one refusal mechanism that is mechanically effective at the covered boundary.

Must include:
- refusal path identifier
- binding between refusal path and covered boundary
- refusal activation state
- refusal result state

Must prove in implementation terms:
The refusal surface can actually prevent the mutation at that covered boundary within first-target scope.

Must not be counted as sufficient:
- logging
- alerting
- scoring
- recommendatory output
- after-the-fact revocation
- punitive consequence only

Completion criterion:
The architecture has one real refusal-capable covered boundary, not only advisory presence.

### 6.7 Timing Qualification Surface

Must implement a way to determine whether refusal was live in time relative to mutation completion at the covered boundary.

Must include:
- ordering marker or equivalent
- refusal-ready status
- mutation-completion relation
- timing qualification result

Must not rely on:
- assumption
- informal narrative
- post-hoc inference without surfaced ordering basis

Completion criterion:
Replay can determine whether refusal qualified as timely for the first target boundary.

### 6.8 State Transition Surface

Must implement the minimum first-target success path:
- Uninitialized
- Segment-Declared
- Identity-Bound
- Authority-Bound
- Coverage-Established
- Refusal-Live
- Actively-Accompanying
- Completed

Where crypto posture is claim-relevant, must also implement:
- Crypto-Qualified

Must also implement at least these downgrade-capable states:
- Advisory-Only
- Coverage-Lost
- Crypto-Failed
- Unverifiable
- Failed-Closed

Completion criterion:
The system can represent both success and failure state paths for the first target.

### 6.9 Downgrade Surface

Must implement fail-closed downgrade behavior for at least:
- refusal failure
- timing failure
- coverage loss
- evidence insufficiency
- claim-relevant crypto failure

Must include:
- downgrade trigger
- prior state or classification
- resulting lower state or classification ceiling
- affected scope

Must not allow:
- silent stronger-claim persistence
- broader claim survival by omission

Completion criterion:
When a required active condition fails, the stronger claim ends explicitly.

### 6.10 Evidence Emission Surface

Must implement evidence emission sufficient to support replay of the first target.

Must include, at minimum:
- segment declaration evidence
- identity binding evidence
- authority binding evidence
- invariant binding evidence
- covered boundary evidence
- claimed irreversible primitive evidence
- refusal-path evidence
- refusal-live evidence
- timing qualification evidence
- active-state evidence
- downgrade evidence
- completion evidence
- final classification evidence
- evidence sufficiency result
- claim-relevant crypto posture evidence where applicable

Must not rely on:
- hidden runtime state
- human explanation as substitute for evidence
- future reconstruction from unspecified logs

Completion criterion:
All first-target claim elements are surfaced as evidence, not merely held internally.

### 6.11 Classification Surface

Must implement the ability to issue one of these classifications for the first target segment:
- Actively Accompanied
- Segment-Accompanied
- Advisory-Accompanied
- Observed-Only
- Uncovered
- Unverifiable

Must include:
- classification record
- scope statement
- classification ceiling
- downgrade reason if lower than intended

Completion criterion:
The system can state the strongest supported class without overclaim.

### 6.12 Replay Support Surface

Must implement a replay path capable of determining:
- what was claimed
- what was bound
- what boundary was covered
- whether refusal was live
- whether refusal was timely
- whether downgrade was required
- what final class is justified
- whether claim-relevant crypto posture qualified where applicable

Must not depend on:
- hidden runtime context
- implicit defaults
- non-surfaced human memory

Completion criterion:
The first target claim can be independently re-evaluated from surfaced evidence.

### 6.13 Crypto Surface

Where crypto posture is claim-relevant, must implement a way to:
- identify the relevant crypto posture
- bind it to the claim where required
- expose it to evidence and replay
- fail closed or downgrade if unsupported or mismatched

Completion criterion:
A crypto-dependent stronger claim cannot survive on hidden or assumed crypto posture.

---

## 7. Mandatory Implementation Sequence

The first target should be implemented in this order.

### Step 1 - Lock exact first-target scope
Implement:
- segment definition
- covered boundary definition
- claim limitation statement

Do not continue until first-target scope is explicit.

### Step 2 - Implement governed transition identity binding
Implement:
- transition identifier
- accompaniment identifier if distinct
- binding record

Do not continue until one stable governed identity exists.

### Step 3 - Implement authority and invariant binding
Implement:
- authority basis binding
- invariant basis binding
- continuity status for both

Do not continue until both are surfaced.

### Step 4 - Implement covered boundary and claimed irreversible primitive
Implement:
- covered boundary identifier
- segment-to-boundary association
- claimed irreversible primitive record

Do not continue until the target boundary is explicit.

### Step 5 - Implement real refusal surface
Implement:
- refusal path
- refusal activation state
- refusal result state
- covered-boundary association

Do not continue until refusal is mechanically effective.

### Step 6 - Implement timing qualification
Implement:
- ordering basis
- refusal-ready relation
- mutation-completion relation
- timing qualification result

Do not continue until timeliness can be determined.

### Step 7 - Implement claim-relevant crypto handling
Where crypto posture is claim-relevant, implement:
- crypto posture identification
- crypto qualification state
- crypto failure path
- replay-visible crypto evidence

Do not continue until crypto-dependent stronger claims can fail closed.

### Step 8 - Implement state model
Implement:
- minimum success path
- minimum downgrade states

Do not continue until both positive and negative state paths exist.

### Step 9 - Implement downgrade handling
Implement:
- refusal failure downgrade
- timing failure downgrade
- coverage loss downgrade
- evidence insufficiency downgrade
- claim-relevant crypto failure downgrade

Do not continue until stronger claims fail closed.

### Step 10 - Implement evidence emission
Implement:
- all mandatory evidence items
- explicit evidence sufficiency result

Do not continue until claim elements are surfaced as replay inputs.

### Step 11 - Implement final classification and replay support
Implement:
- classification issuance
- replay reconstruction path
- final supported-class evaluation

This is the last mandatory implementation step.

---

## 8. Optional Implementation Items

These may strengthen the first target but are not required for first acceptance.

### Optional O1 - Advisory-state refinement
More precise separation between advisory accompaniment and observed-only.

### Optional O2 - Fine-grained coverage-loss reporting
More precise boundary-loss handling and retained narrower scope reporting.

### Optional O3 - Alternate-path explicit exclusion support
Useful for sharper claim limitation.

### Optional O4 - Truth-boundary support
Useful for stronger confidence that the named boundary is the relevant mutation authority for the bounded scope.

### Optional O5 - Successor continuity support
Not needed for first target; belongs later.

### Optional O6 - Expanded crypto agility support
Useful for future capability growth, but not required for the bounded first target.

These optional items must not delay the mandatory first target.

---

## 9. Required Evidence Emissions Checklist

Each item below must exist before first-target implementation is complete.

- [ ] Segment declaration record
- [ ] Segment scope statement
- [ ] Segment start condition record
- [ ] Segment end condition record
- [ ] Covered boundary record
- [ ] Claimed irreversible primitive record
- [ ] Governed transition identity record
- [ ] Accompaniment instance identity record if distinct
- [ ] Authority basis record
- [ ] Authority binding record
- [ ] Invariant basis record
- [ ] Invariant binding record
- [ ] Refusal path record
- [ ] Refusal activation record
- [ ] Refusal result record
- [ ] Timing qualification record
- [ ] Active accompaniment state record
- [ ] Downgrade event records
- [ ] Completion record
- [ ] Final classification record
- [ ] Evidence sufficiency record
- [ ] Claim-relevant crypto posture record where applicable
- [ ] Crypto qualification or crypto failure record where applicable

If any required record is missing, implementation is not complete.

---

## 10. Required Downgrade Behavior Checklist

Each downgrade behavior below must exist before first-target implementation is complete.

- [ ] Refusal failure downgrades stronger claim
- [ ] Timing failure downgrades stronger claim
- [ ] Coverage loss downgrades stronger claim
- [ ] Evidence insufficiency downgrades stronger claim
- [ ] Claim-relevant crypto failure downgrades stronger claim where applicable
- [ ] Downgrade is explicit, not implicit
- [ ] Stronger claim does not survive by omission
- [ ] Resulting lower classification ceiling is surfaced
- [ ] Affected scope is surfaced

If any one of these is missing, fail-closed implementation is incomplete.

---

## 11. Required Replay Support Checklist

Each replay capability below must exist before first-target implementation is complete.

- [ ] Replay can identify claimed segment
- [ ] Replay can identify claimed scope
- [ ] Replay can identify governed transition
- [ ] Replay can identify authority basis
- [ ] Replay can identify invariant basis
- [ ] Replay can identify covered boundary
- [ ] Replay can identify claimed irreversible primitive
- [ ] Replay can determine whether refusal was live
- [ ] Replay can determine whether refusal was timely
- [ ] Replay can determine whether downgrade occurred
- [ ] Replay can determine strongest supported final class
- [ ] Replay can reject stronger unsupported claims
- [ ] Replay can determine claim-relevant crypto qualification where applicable

If any one of these is missing, replay support is incomplete.

---

## 12. Explicit Out-of-Scope Checklist

The first target must explicitly remain out of scope for all of the following.

- [ ] Multi-boundary active accompaniment
- [ ] End-to-end workflow accompaniment
- [ ] Universal downstream continuity
- [ ] Alternate-path closure beyond explicitly bounded scope unless explicitly implemented
- [ ] Authority succession
- [ ] Invariant succession
- [ ] Identity transfer or successor chains
- [ ] Broad truth-boundary closure across multiple systems
- [ ] Full Model 9 implementation claim
- [ ] Full BBIS closure claim
- [ ] Full PQC migration claim
- [ ] Full crypto-agility completion claim

If any of these is implicitly treated as included, scope discipline is broken.

---

## 13. Completion Criteria

First-target implementation is complete only if all of the following are true:
- one explicit bounded segment is implemented
- one explicit covered boundary is implemented
- one governed transition identity is bound
- one authority basis is bound
- one invariant basis is bound
- one real mechanically effective refusal surface exists
- refusal timeliness can be determined
- the minimum success state path exists
- the minimum downgrade paths exist
- all mandatory evidence is emitted
- final classification can be issued
- replay can independently validate the bounded claim
- explicit non-claim boundaries are preserved
- claim-relevant crypto posture handling exists where applicable
- PQC-ready posture remains preserved as an active requirement

If any item is missing, implementation is incomplete.

---

## 14. Exact First-Target Implementation Ceiling

Even when complete, the implementation ceiling for the first target is:

bounded single-segment accompaniment with one covered mutation-capable boundary

It must not be presented as:
- end-to-end accompaniment
- full Model 9 incorporation
- full mutation-bound continuity
- full BBIS closure
- full PQC migration
- full crypto-agility completion

That ceiling must remain explicit in implementation and claim language.

---

## 15. Direct Recommendation

The first target should be built as the smallest real architecture slice that can prove:
- one segment
- one identity
- one authority basis
- one invariant basis
- one covered boundary
- one real refusal surface
- one timing qualification
- one downgrade model
- one replay-verifiable evidence chain
- one claim-relevant crypto handling path where applicable
- one active PQC-ready posture

That is the correct implementation target.

---

## 16. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_FIRST_TARGET_PROOF_HARNESS_OUTLINE.md

This file should be committed before moving to the next split artifact.