# MODEL 9 SENTINEL FIRST TARGET TEST CASE CATALOG

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_PROOF_HARNESS_OUTLINE.md

It defines the repo-agnostic test case catalog for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It is verification-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the repo-agnostic test case catalog for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It turns the earlier acceptance rules and proof harness into explicit verification units.

It defines:
- exact test cases
- exact objective of each test
- exact setup shape
- exact evidence that must exist
- exact replay result expected
- exact final classification expected
- exact pass/fail rule
- exact claim-relevant crypto handling where applicable

---

## 2. Governing Test Rule

A first-target test passes only if the exact bounded claim under test is supported by:
- explicit state
- explicit evidence
- explicit downgrade behavior
- explicit replay validation
- claim-relevant crypto posture handling where applicable
- a crypto posture that does not place PQC outside the active architectural readiness set

No test may pass by narrative, implication, or future intent.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For this catalog, that means:
- the architecture under test must not model PQC as absent, disabled by default, structurally unsupported, or deferred to a later redesign
- where crypto posture is relevant to the claim, tests must confirm it is surfaced and replay-meaningful
- claim-relevant crypto mismatch must fail closed or downgrade
- acceptance must not depend on postponing PQC readiness

This file does not require proving full PQC migration or full multi-algorithm runtime behavior unless explicitly claimed.

It does require that the first-target architecture remain compatible with an active PQC-ready posture.

---

## 5. Test Scope

This catalog applies only to the first incorporation target:
- one explicitly bounded segment
- one explicitly covered mutation-capable boundary
- one governed transition identity
- one authority basis
- one invariant basis
- one refusal-capable surface
- one timing qualification surface
- one replay-verifiable bounded claim

No broader workflow continuity is in scope.

---

## 6. Catalog Structure

The catalog is divided into six groups:
1. core positive conformance
2. refusal and timing failure discipline
3. coverage and scope discipline
4. evidence and replay discipline
5. classification and downgrade discipline
6. PQC readiness discipline

---

## 7. Test Case Format

Each test case in this catalog uses this structure:
- Test ID
- Name
- Objective
- Scope under test
- Setup shape
- Required evidence to inspect
- Replay questions
- Expected result
- Pass rule
- Fail rule

---

## 8. Core Positive Conformance Tests

### T01 - Nominal bounded active segment

Objective:
Prove that one explicitly bounded segment with one covered mutation-capable boundary can satisfy the first target.

Scope under test:
- one segment
- one covered boundary
- one governed transition identity
- one authority basis
- one invariant basis
- one refusal-capable surface
- one timing-qualified refusal relation

Setup shape:
The system declares the segment, binds identity, binds authority and invariant, establishes coverage, activates refusal, qualifies timing, completes the segment, and emits final classification.

Required evidence to inspect:
- segment declaration
- segment scope statement
- governed transition identity binding
- authority binding
- invariant binding
- covered boundary identification
- claimed irreversible primitive
- refusal path identification
- refusal-live state
- timing qualification
- active accompaniment state
- completion record
- final classification
- evidence sufficiency result
- crypto posture record relevant to the bounded claim where applicable

Replay questions:
- What exact segment was claimed?
- What exact boundary was covered?
- What authority and invariant governed it?
- Was refusal mechanically effective?
- Was refusal timely?
- Does the evidence support only the bounded scope?
- Is the crypto posture compatible with PQC-on / PQC-ready architectural treatment where claim-relevant?

Expected result:
- Segment-Accompanied at minimum
- Actively Accompanied only if the exact segment is the full claim scope and every stronger condition is proven

Pass rule:
All required elements are explicit, replay-sufficient, scope-bounded, and not contradicted.

Fail rule:
Any required first-target element is missing, ambiguous, contradicted, or broader than the supported scope.

### T02 - Nominal bounded active segment with explicit claim limitation

Objective:
Prove that the successful first target remains explicitly bounded and does not silently inflate into workflow-wide continuity.

Scope under test:
Same as T01, but focused on claim language discipline.

Setup shape:
Run the nominal first-target path and emit explicit non-claim boundaries.

Required evidence to inspect:
- bounded scope statement
- non-claim statement
- classification ceiling statement
- final classification record

Replay questions:
- Does the evidence support only the bounded segment?
- Is broader scope explicitly excluded?
- Does the final class remain within the first-target ceiling?

Expected result:
Bounded claim survives; broader claim does not appear.

Pass rule:
Bounded support exists and broader support is not implied.

Fail rule:
Any broader language survives without proof.

---

## 9. Refusal and Timing Failure Discipline Tests

### T03 - Refusal path present but mechanically ineffective

Objective:
Prove that refusal presence alone does not qualify as active accompaniment.

Scope under test:
Single bounded first-target segment.

Setup shape:
A refusal path exists, but it only alerts, annotates, or recommends and cannot actually stop the mutation.

Required evidence to inspect:
- refusal path record
- refusal capability state
- evidence showing lack of mechanical effectiveness
- downgrade record
- final classification

Replay questions:
- Did refusal exist?
- Was it mechanically effective?
- What is the strongest remaining justified class?

Expected result:
- Advisory-Accompanied at best

Pass rule:
Replay rejects active accompaniment and preserves only the strongest lower justified class.

Fail rule:
Active accompaniment survives merely because a refusal surface exists.

### T04 - Refusal mechanically effective but untimely

Objective:
Prove that untimely refusal does not qualify as active accompaniment.

Setup shape:
A real refusal path exists, but timing evidence shows it could not act before mutation completion.

Required evidence to inspect:
- refusal-live record
- timing ordering basis
- timing qualification failure
- downgrade record
- final classification

Replay questions:
- Was refusal live?
- Was refusal timely?
- Does untimely refusal ceiling the classification?

Expected result:
- Advisory-Accompanied at best

Pass rule:
Replay downgrades below active accompaniment because timing failed.

Fail rule:
Active accompaniment survives despite timing failure.

### T05 - Refusal failure after initial active state

Objective:
Prove that a previously stronger state does not survive after refusal effectiveness is lost.

Setup shape:
The segment reaches active accompaniment, then refusal effectiveness is lost before completion.

Required evidence to inspect:
- active accompaniment state
- refusal failure event
- downgrade event
- final classification

Replay questions:
- Did the stronger state exist?
- When was refusal lost?
- Did the stronger classification terminate immediately?

Expected result:
The stronger class ends at the failure point and only the strongest lower justified class survives.

Pass rule:
No silent persistence of the defeated stronger class.

Fail rule:
Earlier active status continues to be treated as if uninterrupted.

---

## 10. Coverage and Scope Discipline Tests

### T06 - Coverage loss at the covered boundary

Objective:
Prove that coverage loss ends the stronger claim fail closed.

Setup shape:
The covered boundary is initially established, then coverage is lost before valid completion.

Required evidence to inspect:
- coverage establishment
- coverage loss record
- affected scope
- downgrade or fail-closed record
- final classification

Replay questions:
- Was coverage established?
- Was coverage lost?
- Did the stronger claim terminate?
- Did any lower class survive legitimately?

Expected result:
Stronger active claim fails closed.

Pass rule:
Coverage loss is explicit and the stronger claim does not survive by inertia.

Fail rule:
Coverage loss occurs but no downgrade or ceiling is enforced.

### T07 - Ambiguous covered boundary

Objective:
Prove that ambiguous boundary definition fails the first target.

Setup shape:
The segment claims one covered boundary, but evidence leaves room for multiple plausible mutation-capable boundaries without explicit bounded handling.

Required evidence to inspect:
- covered boundary declaration
- mutation-boundary evidence
- ambiguity record or insufficiency record
- final classification

Replay questions:
- Is the covered boundary explicit?
- Is the claim single-boundary and bounded?
- Can replay determine which boundary is actually covered?

Expected result:
- Unverifiable or rejection of the stronger class

Pass rule:
Replay refuses to preserve the stronger class under boundary ambiguity.

Fail rule:
The stronger class survives despite ambiguous covered-boundary scope.

### T08 - Scope inflation attempt

Objective:
Prove that workflow-wide or downstream wording is rejected when only one bounded segment is proven.

Setup shape:
Only the first-target bounded segment is supported, but a broader label or public conclusion is attempted.

Required evidence to inspect:
- supported segment scope
- attempted broader scope wording
- rejection/downgrade record
- final accepted scope statement

Replay questions:
- What exact scope is actually supported?
- Did broader claim language exceed the evidence?
- Was broader scope rejected?

Expected result:
Only the bounded scope survives.

Pass rule:
Scope inflation is detected and blocked.

Fail rule:
Broader unsupported claim remains.

---

## 11. Evidence and Replay Discipline Tests

### T09 - Missing mandatory evidence for stronger class

Objective:
Prove that missing mandatory evidence defeats the stronger claim.

Setup shape:
A stronger class is claimed, but one mandatory evidence link is absent.

Required evidence to inspect:
- missing evidence indication
- affected stronger claim
- downgrade record
- final classification

Replay questions:
- What evidence is missing?
- Is that evidence mandatory for the stronger class?
- What lower class, if any, survives?

Expected result:
- Unverifiable or a weaker lower class if separately supported

Pass rule:
Replay rejects the unsupported stronger class.

Fail rule:
Narrative or assumption repairs the missing evidence.

### T10 - Contradictory evidence on a required stronger-class element

Objective:
Prove that contradiction defeats the stronger class unless resolved by a lower justified class.

Setup shape:
Some evidence supports active accompaniment while another surfaced record defeats a required element such as timing or refusal effectiveness.

Required evidence to inspect:
- supporting record
- contradicting record
- contradiction handling
- downgrade record
- final classification

Replay questions:
- Is contradiction present?
- Does it defeat a required stronger-class element?
- Was a lower justified class selected?

Expected result:
Stronger class rejected; lower class or Unverifiable survives.

Pass rule:
Replay does not average contradictory records into a stronger pass.

Fail rule:
The stronger claim survives despite unresolved contradiction.

### T11 - Late explanation without valid evidentiary support

Objective:
Prove that late narrative explanation cannot retroactively repair a defeated stronger claim.

Setup shape:
Initial surfaced evidence is insufficient for the stronger claim; later explanatory material attempts to restore it without valid evidence-chain support.

Required evidence to inspect:
- original evidence set
- late explanation
- ordering markers
- replay decision

Replay questions:
- Was the stronger class already defeated by missing evidence?
- Does the later material qualify as valid evidence under the schema and ordering rules?
- Can the claim be lawfully repaired?

Expected result:
The stronger claim remains defeated unless the late evidence is valid under the explicit replay model.

Pass rule:
Replay refuses improper retroactive repair.

Fail rule:
Narrative arrives late and rescues a class that should have failed.

### T12 - Final classification exceeds evidentiary ceiling

Objective:
Prove that the final output cannot exceed the strongest class actually supported.

Setup shape:
The emitted final classification is stronger than what replay can justify from the evidence chain.

Required evidence to inspect:
- full evidence chain
- final classification record
- replay-supported classification
- discrepancy finding

Replay questions:
- What is the strongest justified class?
- Does the final label exceed it?
- Was the final label corrected or rejected?

Expected result:
Final classification is downgraded to the strongest replay-supported class.

Pass rule:
Replay enforces the evidentiary ceiling.

Fail rule:
The emitted label wins over the evidence.

---

## 12. Classification and Downgrade Discipline Tests

### T13 - Advisory presence correctly distinguished from observed-only

Objective:
Prove that persistent accompaniment presence is distinguished from mere observation.

Setup shape:
A persistent accompaniment process exists, but no effective refusal exists.

Required evidence to inspect:
- accompaniment presence evidence
- lack of refusal qualification
- final classification

Replay questions:
- Is there real persistent accompaniment presence?
- Is it more than observed-only?
- Is it less than active accompaniment?

Expected result:
- Advisory-Accompanied

Pass rule:
Replay correctly assigns advisory rather than observed-only or active.

Fail rule:
The system collapses advisory into active, or advisory into mere observation without basis.

### T14 - Observed-only correctly distinguished from uncovered

Objective:
Prove that visibility without accompaniment is classified as observed-only, not uncovered.

Setup shape:
The segment is visible, but no accompanied claim applies.

Required evidence to inspect:
- visibility evidence
- absence of accompanied proof
- final classification

Replay questions:
- Is the segment visible?
- Is there any valid accompanied claim?
- What is the correct lower class?

Expected result:
- Observed-Only

Pass rule:
Replay preserves the visibility distinction.

Fail rule:
The system collapses visible-but-ungoverned into uncovered without basis.

### T15 - Stronger claim terminated by omission failure

Objective:
Prove that the system cannot preserve a stronger class merely because no downgrade label was emitted during runtime.

Setup shape:
A required active condition fails, but no explicit runtime downgrade record is emitted.

Required evidence to inspect:
- evidence defeating the stronger class
- absence of runtime downgrade label
- replay classification result

Replay questions:
- Did a stronger-class requirement fail?
- Did runtime omit downgrade?
- Does replay still enforce downgrade?

Expected result:
Replay downgrades anyway.

Pass rule:
Replay defeats silent stronger-claim persistence.

Fail rule:
Missing runtime downgrade lets the stronger class survive.

---

## 13. PQC Readiness Discipline Tests

### T16 - Crypto posture is not legacy-only by structural assumption

Objective:
Prove that the first target does not depend on a structurally legacy-only crypto assumption.

Setup shape:
Inspect the bounded first-target claim surfaces and evidence posture to verify that crypto identity/profile handling is not hard-coded as legacy only forever.

Required evidence to inspect:
- crypto profile or equivalent crypto posture record
- authority/evidence binding relation to crypto posture
- fail-closed behavior when required crypto posture is not satisfied
- replay visibility of crypto posture relevant to the claim

Replay questions:
- Is crypto posture surfaced at all?
- Is the first target claim compatible with a PQC-ready architecture?
- Would unsupported or wrong crypto posture fail closed rather than pass silently?

Expected result:
The bounded target remains compatible with PQC-on / PQC-ready architectural treatment.

Pass rule:
The architecture does not require postponing PQC readiness in order for the first target to function honestly.

Fail rule:
The first target only works by assuming a legacy-only crypto posture or by hiding crypto posture from replay.

### T17 - Evidence and replay can carry crypto posture relevant to the claim

Objective:
Prove that replay can inspect crypto posture as part of claim validation where relevant.

Setup shape:
Run the nominal bounded segment with surfaced crypto posture information relevant to authority/evidence support.

Required evidence to inspect:
- crypto posture record
- evidence-integrity basis tied to the claim
- replay input carrying crypto posture
- final classification ceiling behavior if crypto posture is invalid or unsupported

Replay questions:
- Can replay see the crypto posture relevant to the bounded claim?
- Is it possible to validate or fail the claim based on surfaced crypto posture?
- Is fail-closed behavior preserved?

Expected result:
Replay can incorporate crypto posture into its bounded evaluation when relevant.

Pass rule:
Crypto posture is surfaced enough to be replay-meaningful.

Fail rule:
Crypto posture is hidden, ignored, or treated as non-binding.

### T18 - Wrong or unsupported crypto posture fails closed

Objective:
Prove that if the bounded claim depends on a required crypto posture, unsupported posture does not silently pass.

Setup shape:
Run a bounded first-target scenario where the required crypto posture is mismatched, absent, or unsupported.

Required evidence to inspect:
- required crypto posture record
- actual crypto posture record
- mismatch or unsupported indication
- downgrade or failure record
- final classification

Replay questions:
- Was required crypto posture satisfied?
- If not, did the stronger claim fail closed?
- Did replay preserve only the strongest lower justified class?

Expected result:
The stronger claim fails or downgrades appropriately.

Pass rule:
Unsupported crypto posture cannot ride through on optimism.

Fail rule:
The claim survives despite crypto-posture mismatch when that posture is relevant to the claim.

### T19 - PQC readiness not deferred outside the architecture claim boundary

Objective:
Prove that PQC readiness is treated as an active architecture posture, not a later policy note.

Setup shape:
Inspect the first-target claim package and verify that PQC readiness is explicitly preserved within the architecture posture rather than postponed outside it.

Required evidence to inspect:
- architecture claim limitation statement
- crypto posture statement
- non-claim boundaries
- fail-closed behavior related to crypto posture

Replay questions:
- Is PQC readiness acknowledged inside the architecture posture?
- Is the bounded first-target claim honest about what is implemented versus what remains broader?
- Is PQC treated as on/ready rather than off/later?

Expected result:
First-target architecture posture remains explicitly PQC-ready even though first-target scope is narrow.

Pass rule:
PQC is preserved as an active requirement.

Fail rule:
The first target is framed as if PQC can be ignored until much later.

---

## 14. Acceptance Matrix

The first target should be considered proven only if the following mandatory tests pass:

- T01
- T02
- T03
- T04
- T06
- T08
- T09
- T12
- T15
- T16
- T17
- T18
- T19

Recommended additional confidence tests:
- T05
- T07
- T10
- T11
- T13
- T14

---

## 15. Acceptance Rule

The first target is accepted only if:
1. the nominal bounded target passes
2. refusal ineffectiveness is rejected
3. refusal untimeliness is rejected
4. coverage loss fails closed
5. missing mandatory evidence defeats the stronger class
6. evidentiary ceiling is enforced
7. silent stronger-claim persistence is defeated by replay
8. broader unsupported scope is rejected
9. PQC-on / PQC-ready architecture posture is preserved
10. relevant crypto posture can be surfaced and replayed
11. unsupported relevant crypto posture fails closed

---

## 16. Rejection Rule

The first target must be rejected if any of the following occur:
- the nominal bounded target cannot be replay-validated
- active accompaniment survives without mechanical refusal
- active accompaniment survives without timely refusal
- stronger class survives coverage loss
- stronger class survives missing mandatory evidence
- stronger class exceeds evidentiary ceiling
- scope inflation survives
- replay depends on hidden assumptions
- PQC posture is structurally absent, deferred, or hidden when relevant
- crypto posture mismatch does not fail closed when relevant

---

## 17. Strongest Permitted Conclusion from This Catalog

If the mandatory tests pass, the strongest permitted conclusion is:

SPECTRE-SENTINEL satisfies the first bounded Model 9 incorporation target for one explicitly scoped segment and one covered mutation-capable boundary, with replay-verifiable classification discipline, fail-closed downgrade behavior, and PQC-ready cryptographic posture preserved as an active architectural requirement.

That conclusion still does not permit claims of:
- full Model 9 implementation
- end-to-end accompaniment
- universal mutation-bound continuity
- full BBIS closure

---

## 18. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_FIRST_TARGET_PHASED_IMPLEMENTATION_PLAN.md

This file should be committed before moving to the next split artifact.