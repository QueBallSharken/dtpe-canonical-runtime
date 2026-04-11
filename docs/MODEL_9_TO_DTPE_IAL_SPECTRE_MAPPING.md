# MODEL 9 TO DTPE / IAL / SPECTRE / SPECTRE-SENTINEL MAPPING

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_TIGHTENING_SPEC.md

It maps the tightened form of Model 9 into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL in architecture terms only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact maps the tightened form of Model 9 into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL in architecture terms only.

It defines:
- the architecture role of Model 9
- the enforcement surfaces required to support it
- the evidence surfaces required to prove it
- the downgrade states required to prevent overclaim
- the failure mapping required for strict classification
- the replay mapping required for independent verification
- the non-claim boundary required to keep incorporation honest
- the PQC-ready posture that must remain active where crypto posture is relevant to the claim

---

## 2. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

BBIS defines:
- what must survive
- what continuity means
- what counts as survival
- what counts as failure
- what evidence is sufficient
- what replay must prove

DTPE / IAL / SPECTRE / SPECTRE-SENTINEL supplies:
- the actual execution-bound enforcement structure
- authority binding
- refusal-capable boundary logic
- receipt and evidence surfaces
- deterministic replay paths
- fail-closed behavior

Do not merge them conceptually.

---

## 3. Standing Architectural Requirement

PQC must be on and always at the ready.

For this mapping, that means:
- architecture must not assume a structurally legacy-only crypto posture
- relevant crypto posture must be visible to evidence and replay where claim-relevant
- unsupported or mismatched claim-relevant crypto posture must fail closed
- bounded first-target support must not depend on deferring PQC readiness outside the architecture posture

This does not by itself require a full PQC migration program.

It does require that the architecture remain PQC-ready in structure, evidence posture, and replay posture.

---

## 4. Architectural Position of Model 9

### 4.1 Model 9 is not a replacement for execution-bound enforcement

Model 9 is not a substitute for the initial governed boundary.

It is a bounded continuity extension that attempts to keep the governing invariant live across explicitly covered mutation-capable boundaries after initial execution-bound evaluation.

### 4.2 Safe incorporation claim

The only safe incorporation claim is:

DTPE / IAL / SPECTRE / SPECTRE-SENTINEL can support bounded active accompaniment where the system can maintain identity-bound, authority-bound, refusal-capable continuity across explicitly covered mutation-capable boundaries, with sufficient evidence for deterministic replay and independent verification.

Anything broader is overclaim.

---

## 5. Required Enforcement Surfaces

Model 9 can only map into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL if the architecture can expose refusal-capable enforcement surfaces.

These are conceptual surfaces, not repo surfaces.

### 5.1 Transition Identity Surface

The architecture must expose a stable governed transition identity that can remain bound across the claimed accompanied segment.

This surface must support:
- creation of governed transition identity
- continuity of that identity across covered boundaries
- proof that the identity was not replaced or split without governed handling

Without this, Model 9 cannot prove accompaniment continuity.

### 5.2 Authority Binding Surface

The architecture must expose the authority basis governing the accompanied segment.

This surface must support:
- identification of governing authority basis
- binding of authority basis to transition identity
- proof of continuity or governed succession of authority basis
- fail-closed behavior when authority continuity cannot be proven

Without this, Model 9 cannot prove authority continuity.

### 5.3 Invariant Binding Surface

The architecture must expose the governing invariant in a form that remains bound to the accompanied transition.

This surface must support:
- identification of invariant basis
- continuity of invariant basis across covered segment boundaries
- proof that invariant drift did not occur silently
- explicit governed handling if invariant basis changes

Without this, accompaniment becomes descriptive rather than governed.

### 5.4 Refusal Surface

The architecture must expose a refusal-capable mechanism that is mechanically connected to each claimed covered mutation-capable boundary.

This surface must support:
- pre-mutation refusal
- refusal timing before mutation completion
- refusal effectiveness at the actual covered path
- prevention of mutation through alternate uncontrolled paths within claimed scope

If the system can only warn, revoke later, or annotate, this surface is insufficient for Model 9.

### 5.5 Boundary Coverage Surface

The architecture must expose which mutation-capable boundaries are covered by accompaniment and which are not.

This surface must support:
- explicit segment start
- explicit segment end
- explicit list of covered boundaries
- explicit list of uncovered or downgraded boundaries
- explicit identification of claimed irreversible primitive for the segment

Without this, Model 9 cannot avoid scope inflation.

### 5.6 Coverage Continuity Surface

The architecture must expose whether accompaniment remained live across the claimed segment.

This surface must support:
- continuity start event
- continuity maintenance events or proofs
- continuity loss event
- downgrade trigger
- continuity end event

Without this, persistent accompaniment cannot be independently demonstrated.

### 5.7 Alternate Path Closure Surface

The architecture must expose whether the governed mutation could occur through a path outside accompaniment coverage.

This surface must support either:
- proof that no alternate mutation path exists for the claimed scope, or
- explicit downgrade because not all mutation paths are covered, or
- explicit claim limitation excluding those paths

This is necessary because accompaniment on one path does not govern a mutation that can escape elsewhere.

### 5.8 Crypto Posture Surface

Where crypto posture is relevant to the claim, the architecture must expose the crypto posture governing the accompanied segment.

This surface must support:
- identification of relevant crypto posture
- binding of crypto posture to the claim where required
- fail-closed handling when required crypto posture is unsupported or mismatched
- replay visibility of crypto posture where claim-relevant

Without this, a PQC-ready posture is not materially preserved in claim evaluation.

---

## 6. Required Evidence Surfaces

Model 9 only materially strengthens DTPE / IAL / SPECTRE / SPECTRE-SENTINEL if its claims are replay-verifiable.

The architecture therefore needs evidence surfaces sufficient to support offline verification.

### 6.1 Minimum Evidence Set

For each claimed accompanied segment, the evidence surface must be sufficient to show:
- governed transition identity
- accompaniment instance identity
- governing authority identity
- governing invariant identity
- segment start
- segment end
- covered boundaries
- claimed irreversible primitive
- refusal path identity
- refusal capability state at each covered boundary
- pass or refuse result at each covered boundary
- coverage continuity state
- coverage loss events
- downgrade events
- final claim class
- crypto posture relevant to the claim where applicable

### 6.2 Timing Evidence

The architecture must expose enough timing structure to show that refusal was live before the mutation completed.

This does not require exposing irrelevant runtime internals.

It does require evidence sufficient to distinguish:
- refusal existed but too late
- refusal existed and was timely
- refusal was absent
- refusal status cannot be proven

### 6.3 Truth-Boundary Evidence

The architecture must expose the claimed mutation boundary in a way that can be tested against the actual effective mutation authority.

Otherwise a system can claim accompaniment at a boundary that is not the real commit point.

### 6.4 Evidence Sufficiency Rule

If evidence cannot support independent verification of accompaniment continuity, the accompanied claim must be downgraded to a weaker class.

No descriptive claim should survive as a strong governance claim without sufficient evidence.

---

## 7. Required Downgrade States

To map Model 9 safely, the architecture must support strict downgrade classification.

These downgrade states must be explicit and non-collapsible.

### 7.1 Actively Accompanied

Use only when:
- identity continuity is proven
- authority continuity is proven
- invariant continuity is proven
- refusal is mechanically effective
- covered boundaries are explicit
- no relevant alternate mutation path escapes coverage for the claimed scope
- evidence is sufficient for replay
- crypto posture is compatible with the claim where claim-relevant

### 7.2 Segment-Accompanied

Use when active accompaniment is proven only for a bounded segment and no end-to-end claim is made.

This is likely the most common honest Model 9 class.

### 7.3 Advisory-Accompanied

Use when a persistent accompaniment process exists but cannot mechanically refuse the mutation.

This is not governance continuity.

### 7.4 Observed-Only

Use when the system has visibility but no valid accompaniment claim.

### 7.5 Uncovered

Use when no active accompaniment claim applies to the segment.

### 7.6 Unverifiable

Use when a stronger claim may have been intended, but the evidence surface is insufficient to prove it.

### 7.7 Downgrade Rule

A stronger class must never be inferred from a weaker class.

Downgrade must occur immediately upon:
- coverage loss
- authority discontinuity
- invariant discontinuity
- identity discontinuity
- refusal failure
- timing failure
- alternate path exposure
- truth-boundary contradiction
- replay insufficiency
- claim-relevant crypto posture failure

---

## 8. Failure Mapping

Model 9 contributes a stricter failure taxonomy to DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

Each failure class must map to a concrete architectural meaning.

### 8.1 Coverage Failure

Meaning:
A claimed required boundary was not actually covered by active accompaniment.

Architectural implication:
The accompanied claim must terminate or downgrade at that boundary.

### 8.2 Refusal Failure

Meaning:
The accompaniment process existed, but refusal was not mechanically effective.

Architectural implication:
The segment cannot be classified as actively accompanied.

### 8.3 Identity Continuity Failure

Meaning:
The accompaniment process cannot be proven to remain bound to the same governed transition.

Architectural implication:
Continuity claim fails because the governed object is no longer stably identifiable.

### 8.4 Authority Continuity Failure

Meaning:
The authority basis changed, disappeared, or became unprovable.

Architectural implication:
The system must fail closed or downgrade because accompaniment without stable authority is not governance continuity.

### 8.5 Invariant Continuity Failure

Meaning:
The governing invariant changed, disappeared, or became unprovable without governed handling.

Architectural implication:
The accompanied claim fails for that segment because the system no longer proves what remained live.

### 8.6 Latency Failure

Meaning:
Refusal existed in principle but could not act before mutation completion.

Architectural implication:
This is advisory or observed behavior, not active accompaniment.

### 8.7 Alternate Path Failure

Meaning:
The mutation could complete through an uncontrolled or unaccompanied path.

Architectural implication:
The system cannot claim accompanied governance for the broader mutation scope.

### 8.8 Truth-Boundary Failure

Meaning:
The claimed covered boundary was not the true mutation authority.

Architectural implication:
The architecture claimed governance at the wrong place.

### 8.9 Replay Insufficiency Failure

Meaning:
Evidence is insufficient to independently verify the accompanied claim.

Architectural implication:
The claim must be downgraded to unverifiable.

### 8.10 Scope Inflation Failure

Meaning:
The architecture claimed end-to-end active accompaniment even though only a bounded segment was actually covered.

Architectural implication:
This is a classification and conformance failure, not merely a documentation issue.

### 8.11 Crypto Posture Failure

Meaning:
Relevant crypto posture was unsupported, mismatched, absent, or hidden while the stronger claim attempted to survive.

Architectural implication:
The stronger claim must fail closed or downgrade.

---

## 9. Replay Mapping

Model 9 only helps DTPE / IAL / SPECTRE / SPECTRE-SENTINEL if replay can test its claims.

The replay mapping must therefore answer exact architecture questions.

### 9.1 Replay must be able to determine

For each accompanied segment:
1. what transition was governed
2. what accompaniment instance was claimed
3. what authority basis governed it
4. what invariant basis governed it
5. what boundaries were claimed as covered
6. what irreversible primitive was claimed for the segment
7. whether refusal was live at each claimed covered boundary
8. whether refusal was timely relative to mutation completion
9. whether coverage remained continuous
10. whether any alternate mutation path escaped coverage
11. whether downgrade occurred when required
12. whether the final claim exceeded what the evidence supports
13. whether relevant crypto posture was surfaced and properly handled where claim-relevant

### 9.2 Replay must be deterministic at the claim level

Replay does not need to reproduce irrelevant runtime internals.

Replay does need to deterministically recompute whether the architecture had sufficient basis to classify the segment as:
- Actively Accompanied
- Segment-Accompanied
- Advisory-Accompanied
- Observed-Only
- Uncovered
- Unverifiable

### 9.3 Replay must fail closed

If replay cannot prove the accompanied claim from the surfaced evidence, the claim must not survive as a stronger class.

---

## 10. Mapping by Concern Area

### 10.1 Authority Continuity

Model 9 sharpens authority continuity by requiring that accompaniment remain bound to the same governing authority basis across the covered segment.

This strengthens the architecture by forcing explicit treatment of:
- authority persistence
- authority succession
- authority loss
- fail-closed authority drift

### 10.2 Execution-Bound Enforcement

Model 9 does not replace execution-bound enforcement.

Instead:
- execution-bound enforcement remains the initial admissibility gate
- Model 9 extends the architecture by asking whether refusal remains live beyond that first gate across later covered mutation-capable boundaries

This means Model 9 is an extension of continuity claim, not a substitute for first-boundary discipline.

### 10.3 Mutation-Bound Refusal

This is the strongest overlap.

Model 9 only matters if the architecture can maintain refusal at the actual mutation-capable boundaries that determine real state change.

This makes it directly relevant to mutation-bound truthfulness.

### 10.4 Deterministic Replay

Model 9 strengthens replay requirements by forcing the architecture to surface claim-level continuity evidence rather than mere boundary decision evidence.

This pushes the system to prove:
- accompaniment continuity
- refusal continuity
- correct downgrade
- correct termination of stronger claims
- correct crypto-posture handling where claim-relevant

### 10.5 Evidence Sufficiency

Model 9 increases the evidence burden in a useful way.

It requires the architecture to prove not only that governance evaluated once, but that governance stayed live where claimed.

This strengthens evidence sufficiency standards for any public or internal conformance claim.

### 10.6 Offline Verification

Model 9 materially benefits offline verification only if the evidence surface is rich enough to support replay of continuity claims.

Otherwise Model 9 remains a conceptual description with no independently verifiable force.

### 10.7 Failure Taxonomy

Model 9 strengthens the public and internal failure taxonomy by adding failure modes that matter specifically for continuity claims:
- coverage loss
- advisory masquerading as governance
- alternate path escape
- truth-boundary misidentification
- scope inflation
- crypto posture failure where relevant

### 10.8 Conformance Framing

Model 9 gives DTPE / IAL / SPECTRE / SPECTRE-SENTINEL a bounded public frame for claiming stronger continuity than a single execution-bound gate, while still remaining honest about coverage limits.

This is useful only if the architecture preserves downgrade discipline.

---

## 11. Non-Claim Boundary

Model 9 incorporation into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL must not be described as any of the following unless independently proven:
- universal end-to-end governance continuity
- governance of all downstream systems
- proof that observation alone equals refusal
- proof that persistent presence alone equals active governance
- proof that a confidential runtime alone closes the mutation-bound problem
- proof that accompaniment survives across handoff without surfaced continuity evidence
- proof that one accompanied path governs all possible mutation paths
- proof that PQC can remain out of scope without affecting claim validity where crypto posture is claim-relevant

The correct non-claim rule is:

Incorporation of Model 9 means only that the architecture can support bounded active accompaniment for explicitly covered segments, under strict downgrade and replay-verifiable evidence requirements.

---

## 12. Direct Incorporation Standard for SPECTRE-SENTINEL

If SPECTRE-SENTINEL is going to incorporate Model 9, then in architecture terms it must be able to express, at minimum:
- start of accompanied segment
- identity of accompanied transition
- authority basis in force
- invariant basis in force
- covered mutation-capable boundaries
- claimed irreversible primitive for the segment
- refusal path for each covered boundary
- continuity maintenance
- continuity loss
- downgrade state
- final accompanied classification
- claim-relevant crypto posture where applicable

If SPECTRE-SENTINEL cannot express those states, then it has not yet incorporated Model 9 in a meaningful way.

At that point, the honest claim is only:
- conceptual alignment
- partial support
- or future target

Not incorporation.

---

## 13. Direct Recommendation

The correct way to carry Model 9 into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL is this:
- treat it as a bounded accompaniment mode
- require explicit coverage claims
- require mechanically effective refusal
- require authority and invariant continuity
- require alternate-path accounting or explicit claim limitation
- require downgrade discipline
- require replay-verifiable evidence
- require PQC-ready crypto posture to remain active where claim-relevant

That is the strict incorporation rule.

---

## 14. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_CONFORMANCE_AND_CLASSIFICATION_RULES.md

This file should be committed before moving to the next split artifact.