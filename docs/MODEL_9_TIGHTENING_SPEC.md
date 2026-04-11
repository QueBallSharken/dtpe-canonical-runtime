# MODEL 9 TIGHTENING SPEC
## Active Accompaniment for DTPE / IAL / SPECTRE / SPECTRE-SENTINEL

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md

It defines the tightened architectural meaning of Model 9.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact tightens Model 9 so it can be incorporated into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL without overclaim.

Its purpose is to define a narrow architecture claim for persistent accompaniment with live refusal, bounded by:
- explicit coverage
- explicit failure conditions
- explicit evidence requirements
- explicit downgrade rules
- replay-verifiable claim discipline

---

## 2. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture that can satisfy the lens

Do not merge them conceptually.

BBIS defines what must survive for governance closure to be real.

DTPE / IAL / SPECTRE / SPECTRE-SENTINEL defines what architecture can make that survival deterministically enforceable and independently verifiable.

---

## 3. Standing Architectural Requirement

PQC must be on and always at the ready.

For Model 9, this means:
- PQC readiness is not optional
- PQC readiness is not decorative
- PQC readiness is not deferred outside architecture posture
- crypto posture must not be treated as structurally legacy-only
- where crypto posture is relevant to the claim, unsupported or mismatched posture must fail closed
- evidence and replay surfaces must not make relevant crypto posture invisible

This file does not require a full PQC migration program by itself.

It does require that Model 9 incorporation remain compatible with an active PQC-ready posture.

---

## 4. Narrow Claim

Model 9 claims the following, and only the following:

A transition segment counts as actively accompanied only where a persistent, identity-bound, authority-bound, refusal-capable governance process remains mechanically effective across each explicitly covered mutation-capable boundary in that segment, and where evidence is sufficient to prove that refusal could have remained live until refusal or completion at the claimed irreversible primitive for that segment.

This claim is segment-bounded, not universal.

---

## 5. Non-Claim / Anti-Overclaim Clause

Model 9 does not claim:
- that all downstream systems are governed merely because accompaniment was initiated
- that observation equals governance
- that persistence equals refusal capability
- that a TEE, confidential runtime, sidecar, watcher, or monitor alone establishes accompaniment
- that accompaniment survives handoff unless survival is explicitly proven
- that end-to-end continuity exists where any segment is uncovered, advisory-only, or unverifiable
- that one covered path governs all mutation paths
- that PQC can be ignored and added later without architectural consequence

A transition or segment must not be described as governed under Model 9 if any of the following are true:
- the accompaniment process cannot execute at the relevant boundary
- the accompaniment process can observe but cannot prevent mutation
- the accompaniment process can emit warnings or revocations only after mutation
- the accompaniment process loses identity continuity
- the accompaniment process loses authority continuity
- the accompaniment process loses invariant continuity
- veto latency exceeds mutation latency
- the claimed covered boundary is not the true mutation authority
- the accompaniment path can be bypassed by an alternate mutation path
- evidence is insufficient for independent replay
- relevant crypto posture is unsupported or mismatched and the claim still survives

In such cases, the system must downgrade the claim rather than silently preserve a stronger one.

---

## 6. Core Terms

### 6.1 Accompaniment
A governance process that remains live during a transition segment rather than evaluating only at a single point.

### 6.2 Active Accompaniment
Accompaniment that is both:
- refusal-capable
- mechanically effective at the relevant covered mutation-capable boundary

### 6.3 Covered Boundary
A mutation-capable boundary for which the system can prove all of the following:
- the accompaniment process was live at that boundary
- the accompaniment process remained bound to the same governed transition
- the accompaniment process remained bound to the same authority and invariant basis
- the accompaniment process had a mechanically effective refusal path
- the refusal path could act before the governed mutation completed

### 6.4 Mutation-Capable Boundary
Any boundary at which a transition can cause, authorize, release, commit, promote, publish, forward, materialize, or otherwise enable a state change with irreversible or operationally binding effect.

### 6.5 True Mutation Authority
The actual boundary, mechanism, or primitive whose successful execution makes the relevant mutation operationally binding or irreversible for the scope being claimed.

### 6.6 Advisory Accompaniment
A process that remains present and may evaluate continuously, but lacks mechanically effective refusal power.

Advisory accompaniment is not governance continuity under Model 9.

### 6.7 Coverage Loss
Any point at which the accompaniment process ceases to satisfy the requirements for active accompaniment at a required boundary.

### 6.8 Segment
A bounded portion of a transition for which coverage is explicitly claimed.

---

## 7. Coverage Model

### 7.1 Coverage Rule
Model 9 applies only to explicitly claimed segments.

Coverage must never be assumed.

Each claimed segment must identify:
- segment start condition
- segment end condition
- claimed covered boundaries
- claimed irreversible primitive for that segment
- refusal mechanism for each covered boundary
- evidence surfaces for each covered boundary

### 7.2 Coverage Establishment
Coverage is established only when the system can show that:
- accompaniment was instantiated before the first claimed covered boundary in the segment
- accompaniment identity is bound to the transition identity
- accompaniment authority is bound to the governing basis
- accompaniment invariant is bound to the governed transition
- refusal capability exists at each claimed covered boundary
- the covered path is the only path by which the governed mutation can occur, or all alternate mutation paths are also covered and refusal-capable, or the claim scope explicitly excludes those paths

### 7.3 Coverage Maintenance
Coverage remains valid only while all of the following remain true:
- identity continuity remains intact
- authority continuity remains intact
- invariant continuity remains intact
- refusal capability remains live
- veto latency remains within the required bound
- no ungoverned alternate mutation path becomes available for the claimed scope
- the accompaniment process remains attached to each claimed covered boundary
- the claimed irreversible primitive remains the true mutation authority for the segment
- relevant crypto posture remains compatible with the claim where crypto posture is claim-relevant

### 7.4 Coverage Loss
Coverage is lost when any required condition no longer holds.

Once coverage is lost:
- the stronger accompaniment claim must end immediately
- subsequent state must be classified under downgrade semantics
- replay evidence must show where and how coverage was lost

---

## 8. Refusal Effectiveness Requirements

This is the center of Model 9.

A segment counts as actively accompanied only if refusal is mechanically effective.

### 8.1 Refusal is mechanically effective only if it can:
- block mutation before completion
- prevent release or promotion before operational binding effect
- halt or invalidate the governed transition before the claimed irreversible primitive completes

### 8.2 Refusal is not mechanically effective if it can only:
- log
- alert
- recommend
- flag
- score
- quarantine after commit
- revoke after commit
- impose cost after commit
- trigger incident response after commit

### 8.3 Refusal must be bound to timing reality
If the refusal path exists in principle but cannot act before mutation completes, refusal is not live for that boundary.

### 8.4 Refusal must be bound to the actual mutation path
If the system can refuse one path but the mutation can still occur through another unrefused path, the segment is not actively accompanied for that mutation claim.

---

## 9. Identity and Authority Continuity

### 9.1 Identity Continuity
The accompaniment process must remain bound to the same governed transition identity throughout the claimed segment.

It must be possible to prove:
- which transition is being accompanied
- that the accompaniment instance attached to later boundaries is the same logical accompaniment instance or a valid continuity-preserving successor
- that no unrelated transition identity was substituted

### 9.2 Authority Continuity
The accompaniment process must remain bound to the same governing authority basis or to a valid explicitly governed succession of authority.

It must be possible to prove:
- which authority basis governed the segment
- which invariant basis was in force
- whether any authority or invariant change occurred
- whether such change was itself governed and replay-verifiable

### 9.3 Continuity Failure
If identity continuity, authority continuity, or invariant continuity cannot be proven, accompaniment continuity fails for the affected segment.

---

## 10. Evidence Sufficiency Requirements

Model 9 is not satisfied by architecture description alone.

It requires evidence sufficient for independent verification.

For each claimed covered segment, evidence must be sufficient to show:
- transition identity
- accompaniment instance identity
- governing authority identity
- governing invariant identity
- segment start marker
- segment end marker
- claimed covered boundaries
- claimed irreversible primitive
- refusal path identity
- refusal capability state at each covered boundary
- timing relation between refusal capability and mutation event
- pass/refuse result at each covered boundary
- coverage continuity events
- coverage loss events
- downgrade events
- final segment classification
- crypto posture relevant to the claim where applicable

If these cannot be shown, the segment is not replay-verifiable as actively accompanied.

---

## 11. Replay Requirements

Model 9 must support deterministic replay at the level of claimed accompaniment facts.

Replay must be able to test, at minimum:
1. what segment was claimed
2. what boundaries were claimed as covered
3. what irreversible primitive was claimed
4. what authority and invariant governed the segment
5. whether accompaniment remained continuously bound to the governed transition
6. whether refusal capability remained live at each covered boundary
7. whether refusal was timely
8. whether any alternate mutation path escaped accompaniment
9. whether coverage was lost
10. whether downgrade classification was applied correctly
11. whether the final claim exceeded what the evidence supports
12. whether relevant crypto posture was surfaced and properly handled where claim-relevant

Replay does not need hidden runtime internals unless those internals are required to prove the governance claim.

If they are required, sufficient evidence for them must be surfaced.

---

## 12. Failure Taxonomy

Model 9 requires explicit failure classes.

### 12.1 Coverage Failure
A required boundary was not actually covered.

### 12.2 Refusal Failure
The accompaniment process was present, but refusal was not mechanically effective.

### 12.3 Identity Continuity Failure
The accompaniment process cannot be proven to remain bound to the same transition identity.

### 12.4 Authority Continuity Failure
The governing authority or invariant basis changed, disappeared, or became unprovable.

### 12.5 Latency Failure
The refusal path existed but could not act before mutation completion.

### 12.6 Alternate Path Failure
An uncontrolled or unaccompanied path allowed the mutation to occur.

### 12.7 Truth-Boundary Failure
The claimed covered boundary was not the true mutation authority.

### 12.8 Advisory-Only Failure
The accompaniment process remained present but only in observational or recommendatory form.

### 12.9 Replay Insufficiency Failure
Evidence is insufficient to independently verify the accompaniment claim.

### 12.10 Scope Inflation Failure
The system claimed end-to-end active accompaniment even though only bounded segments were covered.

### 12.11 Crypto Posture Failure
Relevant crypto posture was unsupported, mismatched, absent, or hidden from replay while the stronger claim still attempted to survive.

---

## 13. Downgrade Semantics

Model 9 must fail closed by downgrading claims.

Each segment must be classified as exactly one of the following:

### 13.1 Actively Accompanied
All requirements for active accompaniment are satisfied.

### 13.2 Segment-Accompanied
Active accompaniment is established only for the explicitly bounded segment, without end-to-end claim.

### 13.3 Advisory-Accompanied
A persistent process remained present, but refusal was not mechanically effective.

### 13.4 Observed-Only
The system had visibility into the segment but no accompaniment claim is valid.

### 13.5 Uncovered
No valid accompaniment claim exists for the segment.

### 13.6 Unverifiable
A claim was made, but evidence is insufficient to verify it.

No stronger class may be inferred from a weaker one.

---

## 14. Relationship to BBIS

BBIS remains the conformance lens.

Model 9 does not replace BBIS.

Model 9 is one bounded architectural answer to the BBIS question.

BBIS asks:
- what must survive
- what continuity means
- what counts as survival
- what counts as failure
- what evidence is sufficient
- what replay must prove

Model 9 supplies one possible bounded answer:
- continuity by persistent accompaniment
- survival only across covered boundaries
- failure when accompaniment loses refusal-capable continuity
- evidence by continuity and refusal surfaces
- replay by segment-bounded verification of accompaniment claims

Model 9 therefore fits BBIS only where it satisfies BBIS requirements for the claimed scope.

---

## 15. Mapping into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL

This section is architecture-facing, not repo-facing.

### 15.1 Authority Continuity
Model 9 strengthens DTPE / IAL / SPECTRE by requiring accompaniment to remain bound to the same governing authority basis across the claimed segment.

### 15.2 Execution-Bound Enforcement
Model 9 does not replace execution-bound enforcement.

It extends it from a point claim to a bounded continuity claim:
- execution-bound enforcement remains necessary at the initial governed boundary
- Model 9 adds the requirement that refusal remain live across later covered boundaries in the same governed segment

### 15.3 Mutation-Bound Refusal
Model 9 matters only if it preserves refusal as a real condition at the actual mutation-capable boundaries that matter.

That directly strengthens mutation-bound truthfulness.

### 15.4 Deterministic Replay
Model 9 forces the system to expose enough structure to replay:
- accompaniment continuity
- refusal-capability continuity
- coverage loss
- downgrade correctness
- relevant crypto posture where claim-relevant

### 15.5 Evidence Sufficiency
Model 9 sharpens the requirement that evidence must not merely show that a process existed.

It must show that the process was:
- bound to the right transition
- bound to the right authority
- bound to the right invariant
- present at the right boundary
- able to refuse in time
- compatible with claim-relevant crypto posture where applicable

### 15.6 Offline Verification
Model 9 strengthens offline verification only if accompaniment claims are surfaced in receipts or equivalent evidence artifacts sufficient to verify:
- what was claimed
- what was covered
- whether refusal stayed live
- where continuity stopped
- how crypto posture affected the claim where relevant

### 15.7 Failure Taxonomy
Model 9 contributes a sharper public and internal failure taxonomy, especially around:
- coverage loss
- advisory-only masquerading as governance
- latency failure
- truth-boundary misidentification
- scope inflation
- crypto posture failure where relevant

### 15.8 Conformance Framing
Model 9 helps position DTPE / IAL / SPECTRE / SPECTRE-SENTINEL as architecture that can satisfy a harder BBIS-style continuity lens in bounded form without overclaiming universal closure.

---

## 16. Incorporation Rule for SPECTRE-SENTINEL

If Model 9 is incorporated into SPECTRE-SENTINEL, it should be incorporated as a bounded accompaniment mode, not as a blanket continuity claim.

SPECTRE-SENTINEL should be able to express:
- when accompaniment starts
- what segment is claimed
- which boundaries are covered
- what refusal path exists
- when accompaniment degrades
- when accompaniment ends
- what downgrade classification applies
- what crypto posture is relevant to the claim where applicable

If SPECTRE-SENTINEL cannot express those things, it should not claim Model 9 incorporation beyond concept or partial support.

---

## 17. Direct Recommendation

The correct tightened form of Model 9 is:

- not universal continuous governance
- not observation with better branding
- not persistent presence without mechanical refusal

It is:

bounded, identity-bound, authority-bound, refusal-capable active accompaniment across explicitly covered mutation-capable boundaries, with evidence sufficient to replay where continuity held, where it failed, and where claims must be downgraded, while preserving PQC-ready architecture posture as an active requirement.

That is the version safe to begin mapping into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 18. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_TO_DTPE_IAL_SPECTRE_MAPPING.md

This file should be committed before moving to the next split artifact.