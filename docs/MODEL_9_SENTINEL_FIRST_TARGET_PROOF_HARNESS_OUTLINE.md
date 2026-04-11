# MODEL 9 SENTINEL FIRST TARGET PROOF HARNESSS OUTLINE

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_ACCEPTANCE_RULES.md
- docs/MODEL_9_SENTINEL_FIRST_TARGET_IMPLEMENTATION_CHECKLIST.md

It defines the repo-agnostic proof harness outline for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It is verification-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the repo-agnostic proof harness outline for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It defines only:
- what scenarios must be exercised
- what failures must be forced
- what replay must confirm
- what evidence must be inspected
- what constitutes proof of first-target acceptance
- what claim-relevant crypto handling must be proven where applicable

---

## 2. Governing Proof Rule

The first target is proven only if the harness can exercise one explicitly bounded accompanied segment with one explicitly covered mutation-capable boundary and demonstrate, through surfaced evidence and replay, that the strongest accepted class is justified for that exact scope and is downgraded when required.

A build artifact existing is not proof.

A descriptive demo is not proof.

A successful proof harness must show both:
- positive validation
- negative discipline

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For the proof harness, this means:
- the harness must not assume a structurally legacy-only crypto posture
- where crypto posture is relevant to the claim, the harness must test it
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- acceptance must not silently ignore claim-relevant crypto posture

This file does not require a full PQC migration program by itself.

It does require that the bounded first-target proof preserve PQC-ready posture as an active architectural requirement.

---

## 5. Proof Harness Scope

The proof harness applies only to the first target:
- one explicit segment
- one covered boundary
- one governed transition identity
- one authority basis
- one invariant basis
- one refusal-capable surface
- one timing-qualified refusal relation
- one bounded claim ceiling
- claim-relevant crypto handling where applicable

It must not treat broader claims as in scope.

---

## 6. Required Harness Goals

The harness must prove all of the following.

### 6.1 Positive Goal G1 - Bounded Active Segment Support

The harness must prove that the first target can reach its strongest justified bounded classification for the exact segment scope.

### 6.2 Negative Goal G2 - Refusal Qualification Matters

The harness must prove that if refusal is not mechanically effective or not timely, the stronger class does not survive.

### 6.3 Negative Goal G3 - Replay Discipline Exists

The harness must prove that missing or insufficient evidence downgrades the claim rather than being ignored.

### 6.4 Negative Goal G4 - Coverage Discipline Exists

The harness must prove that if coverage is lost or ambiguous, the stronger claim fails closed.

### 6.5 Negative Goal G5 - Scope Discipline Exists

The harness must prove that broader claim language is rejected when only the bounded first target is supported.

### 6.6 Negative Goal G6 - Crypto Discipline Exists

Where crypto posture is claim-relevant, the harness must prove that unsupported or mismatched crypto posture defeats the stronger claim.

These are all mandatory.

---

## 7. Required Harness Structure

The harness should be organized into six sections.

### 7.1 Setup Section
Defines:
- first target segment under test
- covered boundary under test
- authority basis under test
- invariant basis under test
- expected classification ceiling
- expected non-claim boundary
- claim-relevant crypto posture where applicable

### 7.2 Success Scenario Section
Exercises the nominal path and expected successful bounded classification.

### 7.3 Failure Scenario Section
Exercises required downgrade paths and failure conditions.

### 7.4 Replay Verification Section
Reconstructs the claim from surfaced evidence and confirms the strongest justified classification.

### 7.5 Crypto Verification Section
Where crypto posture is claim-relevant, reconstructs and validates crypto qualification or crypto failure handling.

### 7.6 Acceptance Decision Section
Determines whether first-target acceptance conditions are satisfied.

---

## 8. Mandatory Success Scenario

The harness must include exactly one core success scenario for the first target.

### 8.1 Success Scenario S1 - Nominal Bounded Active Segment

Scenario objective:
Demonstrate that one explicitly bounded segment with one covered mutation-capable boundary can satisfy the first target.

Scenario setup must include:
- explicit segment declaration
- explicit covered boundary
- explicit claimed irreversible primitive for the segment
- one governed transition identity
- one authority basis
- one invariant basis
- one real refusal surface
- timing-qualified refusal path
- claim-relevant crypto posture where applicable

Expected state path:
- Uninitialized
- Segment-Declared
- Identity-Bound
- Authority-Bound
- Coverage-Established
- Refusal-Live
- Crypto-Qualified where claim-relevant
- Actively-Accompanying
- Completed

Evidence that must be inspected:
- segment declaration record
- identity binding record
- authority binding record
- invariant binding record
- covered boundary record
- claimed irreversible primitive record
- refusal path record
- refusal-live record
- timing qualification record
- active-state record
- completion record
- final classification record
- evidence sufficiency record
- claim-relevant crypto qualification record where applicable

Replay must confirm:
- exact segment claimed
- exact scope claimed
- exact covered boundary
- exact authority and invariant basis
- exact governed transition identity
- refusal live
- refusal timely
- strongest supported classification for that exact scope
- crypto qualification where claim-relevant

Acceptance expectation:
This scenario must support Segment-Accompanied at minimum, and may support Actively Accompanied only for that exact segment scope if all criteria hold.

---

## 9. Mandatory Failure Scenarios

The harness must include at least the following failure scenarios.

### 9.1 Failure Scenario F1 - Refusal Ineffective

Scenario objective:
Prove that a refusal path which exists but is not mechanically effective cannot support active accompaniment.

Scenario setup:
Use the first target shape, but make refusal advisory only.

Expected result:
- stronger active claim rejected
- classification ceiling at Advisory-Accompanied at best

Evidence that must be inspected:
- refusal path present
- evidence showing refusal does not actually block mutation
- downgrade record
- final classification record

Replay must confirm:
- refusal presence does not equal active accompaniment
- active claim fails
- lower justified class only survives

### 9.2 Failure Scenario F2 - Refusal Untimely

Scenario objective:
Prove that refusal existence without timing qualification is insufficient.

Scenario setup:
Use a real refusal path, but make the refusal too late relative to mutation completion.

Expected result:
- active claim rejected
- classification ceiling at Advisory-Accompanied at best

Evidence that must be inspected:
- refusal-live record
- timing qualification failure record or equivalent ordering evidence
- downgrade record
- final classification record

Replay must confirm:
- live refusal is not enough
- timing failure defeats active accompaniment

### 9.3 Failure Scenario F3 - Coverage Loss

Scenario objective:
Prove that stronger claims fail closed when covered-boundary continuity is lost.

Scenario setup:
Start with the nominal path, then introduce loss of coverage for the claimed boundary or make covered scope no longer valid.

Expected state path:
- Coverage-Established or Actively-Accompanying
- Coverage-Lost
- Failed-Closed
- Completed

Expected result:
- stronger active claim ends
- only the strongest lower justified class survives

Evidence that must be inspected:
- coverage establishment record
- coverage loss record
- affected scope record
- downgrade record
- final classification record

Replay must confirm:
- stronger claim did not survive coverage loss
- fail-closed downgrade occurred

### 9.4 Failure Scenario F4 - Evidence Insufficiency

Scenario objective:
Prove that missing required evidence causes downgrade to Unverifiable or lower.

Scenario setup:
Use the first target shape, but omit or corrupt mandatory evidence for the stronger class.

Expected result:
- stronger claim rejected
- final class becomes Unverifiable or a weaker lower class

Evidence that must be inspected:
- missing or insufficient evidence record
- affected claim scope
- downgrade record
- final classification record

Replay must confirm:
- stronger class cannot stand without mandatory evidence
- no narrative repair occurred

### 9.5 Failure Scenario F5 - Scope Inflation Attempt

Scenario objective:
Prove that broader claim language is rejected when only the bounded first target is supported.

Scenario setup:
Support only the single first-target segment, but attempt broader wording or broader classification output.

Expected result:
- broader claim rejected
- retained class limited to exact bounded segment scope only

Evidence that must be inspected:
- supported segment scope
- attempted broader scope statement
- downgrade or rejection record
- final accepted scope statement

Replay must confirm:
- bounded support did not expand into workflow-wide support by wording alone

### 9.6 Failure Scenario F6 - Claim-Relevant Crypto Failure

Where crypto posture is claim-relevant:

Scenario objective:
Prove that unsupported, mismatched, absent, or hidden claim-relevant crypto posture defeats the stronger claim.

Scenario setup:
Use the first target shape, but make the claim-relevant crypto posture fail qualification.

Expected result:
- stronger crypto-dependent claim rejected
- final class downgraded or fail-closed as appropriate

Evidence that must be inspected:
- crypto posture record
- crypto qualification or crypto failure record
- affected scope
- downgrade record
- final classification record

Replay must confirm:
- crypto presence alone is not enough
- claim-relevant crypto failure defeats the stronger claim

---

## 10. Optional but Valuable Failure Scenarios

These are not mandatory for first acceptance, but they strengthen confidence.

### 10.1 Optional F7 - Authority Binding Failure
Proves that declared-but-unbound authority is insufficient.

### 10.2 Optional F8 - Invariant Binding Failure
Proves that declared-but-unbound invariant is insufficient.

### 10.3 Optional F9 - Identity Discontinuity
Proves that transition identity loss collapses stronger continuity claims.

### 10.4 Optional F10 - Contradictory Evidence
Proves that contradiction forces downgrade rather than optimistic interpretation.

### 10.5 Optional F11 - Observed-Only Fallback
Proves that visibility may remain after stronger accompanied claims fail.

These are valuable, but not required for the first acceptance decision if the mandatory scenarios already prove the acceptance rule.

---

## 11. Replay Verification Requirements

Every mandatory scenario must include replay verification.

### 11.1 Replay must inspect
- claim declaration
- scope statement
- identity binding
- authority binding
- invariant binding
- covered boundary
- refusal state
- timing state
- downgrade events where applicable
- final class
- evidence sufficiency result
- claim-relevant crypto posture where applicable

### 11.2 Replay must determine
- what class was claimed
- what class is actually supported
- what scope is actually supported
- why stronger classes failed where they failed
- whether claim-relevant crypto posture qualified where applicable

### 11.3 Replay must not assume
- missing evidence
- unstated ordering
- implied broader scope
- architectural intention
- runtime reputation
- acceptable crypto posture without surfaced support where claim-relevant

---

## 12. Required Evidence Inspection Matrix

The harness should inspect evidence by scenario using this matrix.

| Scenario | Must Inspect |
|---|---|
| S1 Nominal bounded active segment | all mandatory first-target records |
| F1 Refusal ineffective | refusal path, mechanical ineffectiveness basis, downgrade, final class |
| F2 Refusal untimely | refusal-live, timing failure basis, downgrade, final class |
| F3 Coverage loss | coverage established, coverage loss, affected scope, downgrade, final class |
| F4 Evidence insufficiency | missing/insufficient evidence basis, downgrade, final class |
| F5 Scope inflation attempt | exact supported scope, attempted broader scope, rejection/downgrade, final accepted scope |
| F6 Claim-relevant crypto failure | crypto posture, crypto failure basis, downgrade, final class |

This matrix is mandatory for the core harness.

---

## 13. Acceptance Decision Logic

The harness must make an explicit acceptance decision at the end.

### 13.1 Accept only if all of the following are true
- S1 passes with the bounded first-target scope
- F1 proves refusal ineffectiveness downgrades the claim
- F2 proves untimely refusal downgrades the claim
- F3 proves coverage loss downgrades the claim fail closed
- F4 proves evidence insufficiency defeats the stronger class
- F5 proves broader wording does not survive beyond supported bounded scope
- F6 proves claim-relevant crypto failure defeats the stronger class where applicable
- replay confirms the strongest justified class in all mandatory scenarios

### 13.2 Reject if any of the following are true
- S1 fails to reach the intended bounded active claim
- any mandatory failure scenario preserves a stronger defeated claim
- replay cannot independently validate the claim-level result
- scope inflation survives
- stronger claims remain by omission rather than proof
- final classification exceeds the supported ceiling
- claim-relevant crypto failure survives without downgrade where applicable

---

## 14. Exact Proof of First-Target Acceptance

First-target acceptance is proven only if the harness demonstrates:

1. one explicitly bounded segment can satisfy the first target
2. the claim survives replay only for that exact scope
3. mechanically ineffective refusal does not pass as active accompaniment
4. untimely refusal does not pass as active accompaniment
5. coverage loss terminates stronger claims
6. missing evidence terminates stronger claims
7. broader unsupported wording is rejected
8. claim-relevant crypto failure defeats stronger claims where applicable
9. final acceptance language remains within the first-target ceiling

That is the full proof burden.

---

## 15. Exact Permitted Acceptance Conclusion

If the harness passes, the strongest permitted conclusion is:

The first Model 9 incorporation target is proven for one explicitly bounded segment and one explicitly covered mutation-capable boundary, with replay-verifiable support for the strongest justified bounded classification, fail-closed downgrade under required failure conditions, and claim-relevant crypto handling where applicable.

A shorter permitted conclusion is:

The bounded first target is proven.

No broader conclusion should be issued from this harness alone.

---

## 16. Exact Forbidden Acceptance Conclusion

Even if the harness passes, it must not conclude:
- full Model 9 implementation
- end-to-end accompaniment
- downstream continuity governance
- universal active accompaniment
- full BBIS closure
- governance of all mutation paths
- continuous governance solved
- full PQC migration completion
- full crypto-agility completion

Those are outside first-target proof scope.

---

## 17. Direct Recommendation

This proof harness should be treated as the minimum acceptance harness, not an aspirational demo.

It should prove two things at once:
- the bounded claim is real
- the system refuses to overclaim when the bounded claim fails

That is the correct standard.

---

## 18. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_FIRST_TARGET_TEST_CASE_CATALOG.md

This file should be committed before moving to the next split artifact.