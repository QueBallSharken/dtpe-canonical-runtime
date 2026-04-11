# MODEL 9 SENTINEL REPLAY RULES

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_TIGHTENING_SPEC.md
- docs/MODEL_9_SENTINEL_EVIDENCE_SCHEMA.md

It defines the replay rules required for SPECTRE-SENTINEL to evaluate Model 9 claims in a strict, bounded, fail-closed, independently verifiable way.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the replay rules required for SPECTRE-SENTINEL to evaluate Model 9 claims in a strict, bounded, fail-closed, independently verifiable way.

It defines:
- replay inputs
- replay ordering rules
- replay sufficiency rules
- replay downgrade rules
- replay pass/fail criteria by classification
- replay handling of contradiction, ambiguity, and evidence loss
- replay handling of claim-relevant crypto posture where applicable

---

## 2. Governing Replay Rule

Replay may validate only the strongest Model 9 classification that can be deterministically reconstructed from:
- surfaced evidence
- explicit scope
- explicit ordering
- explicit downgrade logic
- claim-relevant crypto posture where applicable

Nothing stronger may survive replay.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For replay, this means:
- replay must not assume a structurally legacy-only crypto posture
- where crypto posture is relevant to the claim, replay must be able to inspect it
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- replay must not treat hidden crypto posture as acceptable when classification depends on it

This file does not require a full PQC migration program by itself.

It does require replay to preserve claim-relevant crypto posture as part of bounded claim validation where applicable.

---

## 5. Replay Scope

Replay applies only to a claimed accompanied segment and the exact scope surfaced for that segment.

Replay must not infer:
- broader workflow scope from narrower segment evidence
- active accompaniment from persistent presence
- timely refusal from mere refusal-path existence
- alternate-path closure from lack of evidence
- true mutation authority from naming alone
- crypto qualification from mere crypto presence

Replay evaluates only what the evidence explicitly supports.

---

## 6. Replay Inputs

Replay must receive explicit inputs sufficient to evaluate the claim.

### 6.1 Mandatory Replay Inputs

Replay must have access to:
- segment identifier
- claimed scope statement
- claimed classification
- governed transition identifier
- accompaniment instance identifier where relevant
- authority basis identifier
- invariant basis identifier
- covered boundary set
- claimed irreversible primitive
- evidence records relevant to the segment
- ordering markers sufficient to reconstruct event and state sequence
- downgrade events, if any
- final classification record
- evidence sufficiency record, if present
- claim-relevant crypto posture record where applicable

Without these, replay cannot validate a strong claim.

### 6.2 Optional Replay Inputs

Replay may use, but must not depend on unless required by the claim:
- explanatory metadata
- implementation diagnostics
- health status notes
- environment notes
- secondary observability records

Optional inputs may clarify, but cannot repair missing mandatory claim evidence.

---

## 7. Replay Ordering Rules

Replay must evaluate evidence in a deterministic order.

### 7.1 Ordering Rule

Replay must process evidence using surfaced ordering markers only.

Replay must not infer ordering from:
- narrative sequence
- display order
- assumption

### 7.2 Declaration Before Validation Rule

Replay must first determine what was claimed before evaluating whether the claim is supported.

That means replay must identify:
- claimed segment
- claimed scope
- claimed classification
- claimed covered boundaries
- claimed irreversible primitive
- claimed authority basis
- claimed invariant basis
- claim-relevant crypto posture where applicable

before attempting to validate them.

### 7.3 Binding Before Continuity Rule

Replay must validate:
- transition identity binding
- authority binding
- invariant binding

before evaluating continuity-dependent claims.

If binding is not established, stronger continuity claims cannot survive.

### 7.4 Coverage Before Refusal Rule

Replay must determine the claimed accompanied scope and covered boundaries before evaluating whether refusal was live.

A refusal path without established covered scope cannot support active accompaniment.

### 7.5 Refusal Before Timing Rule

Replay must determine that a refusal path existed and was mechanically relevant before evaluating whether it was timely.

A timely nonexistent refusal path is not meaningful.

### 7.6 Timing Before Active Classification Rule

Replay must determine timing sufficiency before validating Actively Accompanied.

If timing cannot be proven, the stronger class fails.

### 7.7 Crypto Qualification Before Stronger Classification Rule

Where crypto posture is claim-relevant, replay must determine crypto qualification before validating a stronger class that depends on it.

If crypto qualification cannot be proven, the stronger class fails.

### 7.8 Downgrade Before Final Classification Rule

Replay must process downgrade events before accepting the final classification.

A final label cannot override surfaced downgrade evidence.

---

## 8. Replay Reconstruction Rules

Replay must reconstruct the claim state from evidence, not from intention.

### 8.1 Claim Reconstruction

Replay must reconstruct:
- what segment was claimed
- what scope was claimed
- what class was claimed
- what authority and invariant were claimed
- what boundaries were claimed as covered
- what irreversible primitive was claimed
- what claim-relevant crypto posture was claimed where applicable

If claim reconstruction fails, replay cannot validate a strong class.

### 8.2 State Reconstruction

Replay must reconstruct the strongest state path supported by evidence, including where applicable:
- Segment-Declared
- Identity-Bound
- Authority-Bound
- Coverage-Established
- Refusal-Live
- Crypto-Qualified
- Actively-Accompanying
- Advisory-Only
- Coverage-Lost
- Crypto-Failed
- Unverifiable
- Failed-Closed
- Completed

Replay must not assume intermediate states not supported by evidence.

### 8.3 Continuity Reconstruction

Replay must determine whether continuity held for:
- transition identity
- authority basis
- invariant basis
- accompaniment presence where relevant
- refusal-capability status where relevant
- crypto qualification status where claim-relevant

If continuity cannot be reconstructed, stronger continuity claims fail.

---

## 9. Replay Sufficiency Rules

Replay must explicitly test evidence sufficiency.

### 9.1 Sufficiency Rule

A classification survives replay only if every mandatory element required for that class is supported by surfaced evidence.

### 9.2 No Inference Rule

Replay must not fill missing mandatory elements through:
- narrative explanation
- probable intent
- architectural expectation
- unstated defaults
- "should have happened" logic

### 9.3 Explicit Gap Rule

If a required element is missing, replay must record that gap explicitly and downgrade accordingly.

### 9.4 Ambiguity Rule

If evidence is ambiguous between a stronger and weaker class, replay must select the weaker justified class.

### 9.5 Contradiction Rule

If evidence contradicts a stronger class, replay must reject the stronger class even if some supporting records exist.

### 9.6 Scope Sufficiency Rule

Replay must separately test whether evidence supports:
- the narrower segment only
- or the full claimed scope

Failure at broader scope does not automatically destroy a narrower valid segment claim, but the broader claim must fail.

### 9.7 Crypto Sufficiency Rule

Where crypto posture is claim-relevant, replay must separately test whether surfaced crypto evidence is sufficient to support the stronger class.

Mere crypto presence is not enough.

---

## 10. Replay Classification Evaluation Order

Replay must test classifications from strongest to weakest.

### 10.1 Step 1 - Test Actively Accompanied

Replay may validate Actively Accompanied only if it can establish all of the following:
- explicit segment and scope
- transition identity continuity
- authority continuity
- invariant continuity
- explicit covered boundaries
- refusal live at covered boundaries
- refusal mechanically effective
- refusal timely relative to mutation completion
- no relevant uncovered alternate mutation path for the claimed scope, or explicit narrower scope excluding them
- support for the claimed mutation authority
- no unresolved contradiction or insufficiency defeating the class
- final class consistent with downgrade chain
- crypto qualification where claim-relevant

If any required element fails, replay must reject this class.

### 10.2 Step 2 - Test Segment-Accompanied

Replay may validate Segment-Accompanied only if it can establish active accompaniment for a bounded narrower segment, but not for the broader surrounding workflow or path.

Replay must verify:
- narrower segment scope is explicit
- active criteria hold for that narrower segment
- no improper end-to-end claim survives
- crypto qualification holds where claim-relevant to that narrower claim

If narrower scope is not explicit, replay must not validate this class as a repair mechanism.

### 10.3 Step 3 - Test Advisory-Accompanied

Replay may validate Advisory-Accompanied only if it can establish:
- a persistent accompaniment process was present for the segment
- refusal did not qualify as mechanically effective or timely
- the weaker class is explicitly or necessarily supported by evidence

Without proof of persistent accompaniment presence, replay must reject this class.

### 10.4 Step 4 - Test Observed-Only

Replay may validate Observed-Only only if it can establish:
- visibility or observation evidence exists for the relevant segment or event
- no stronger accompanied class is supported

### 10.5 Step 5 - Test Uncovered

Replay may validate Uncovered only if it can establish:
- no accompaniment claim applied to the segment, or
- no supported covered scope existed

This class must not be used when the real issue is insufficient evidence for a stronger attempted claim.

### 10.6 Step 6 - Test Unverifiable

Replay must assign Unverifiable when:
- a stronger claim was made or implied
- but required evidence is insufficient, ambiguous, or contradictory beyond replay resolution

This class is mandatory when proof failure, not true lack of accompaniment, is the reason a stronger class cannot stand.

---

## 11. Replay Downgrade Rules

Replay must apply downgrade rules deterministically.

### 11.1 Downgrade Trigger Rule

Replay must downgrade immediately when surfaced evidence shows any of the following:
- identity discontinuity
- authority discontinuity
- invariant discontinuity
- coverage loss
- refusal failure
- timing failure
- alternate path exposure
- truth-boundary contradiction
- evidence insufficiency
- scope inflation
- claim-relevant crypto posture failure

### 11.2 Strongest Lower Justified Class Rule

Replay must downgrade only to the strongest lower class explicitly supported by evidence.

### 11.3 No Silent Persistence Rule

A previously stronger class must not remain valid merely because no downgrade label was emitted at runtime.

If replay evidence defeats the stronger class, replay must downgrade it.

### 11.4 Narrower Survival Rule

If a broader scope fails but a narrower bounded segment still satisfies a lower or equal class, replay may preserve that narrower class only if the narrower scope is explicit and supported.

### 11.5 Downgrade Ceiling Rule

If evidence defeats an element required for a class, replay must enforce the resulting classification ceiling.

Example:
- failure of mechanical refusal ceilings the result below Actively Accompanied
- evidence insufficiency ceilings the result at Unverifiable for the defeated claim
- crypto qualification failure ceilings the result below any crypto-dependent stronger class

---

## 12. Replay Pass / Fail Criteria by Classification

### 12.1 Replay Pass for Actively Accompanied

Replay passes for Actively Accompanied only if all mandatory evidence required for the class is present, ordered, coherent, and sufficient, with no unresolved contradiction defeating the class.

### 12.2 Replay Fail for Actively Accompanied

Replay fails this class if any required element is missing, ambiguous, contradicted, mistimed, or unsupported for the claimed scope.

Failure here does not end replay. Replay must continue to lower classes.

### 12.3 Replay Pass for Segment-Accompanied

Replay passes for Segment-Accompanied only if active accompaniment is fully supported for the explicit narrower segment and the broader unsupported claim is not preserved.

### 12.4 Replay Fail for Segment-Accompanied

Replay fails this class if the narrower segment is not explicit, or if even the narrower segment lacks support for active accompaniment.

### 12.5 Replay Pass for Advisory-Accompanied

Replay passes for Advisory-Accompanied only if accompaniment presence is supported but refusal fails qualification.

### 12.6 Replay Fail for Advisory-Accompanied

Replay fails this class if persistent accompaniment itself cannot be proven.

### 12.7 Replay Pass for Observed-Only

Replay passes for Observed-Only only if observation evidence exists and no stronger accompanied class survives.

### 12.8 Replay Fail for Observed-Only

Replay fails this class if there is no evidence even of visibility or observation.

### 12.9 Replay Pass for Uncovered

Replay passes for Uncovered only if the segment genuinely had no supported accompaniment claim.

### 12.10 Replay Pass for Unverifiable

Replay passes for Unverifiable when replay can prove that a stronger claim was attempted or relevant, but the evidence chain is insufficient to validate it.

---

## 13. Replay Handling of Contradiction

Replay must explicitly handle contradictory evidence.

### 13.1 Contradiction Detection Rule

Replay must detect contradiction where evidence simultaneously asserts and defeats a required claim element.

Examples:
- refusal path asserted, but downgrade evidence shows refusal could not block mutation
- claimed irreversible primitive asserted, but truth-boundary evidence shows mutation authority existed elsewhere
- active continuity asserted, but continuity-loss event is surfaced earlier or within the same claimed scope
- crypto-qualified status asserted, but crypto-failure evidence shows claim-relevant crypto posture was unsupported or hidden

### 13.2 Contradiction Resolution Rule

Replay must resolve contradiction by selecting the strongest lower class not defeated by the contradiction.

Replay must not average contradictory records into a stronger surviving class.

### 13.3 Unresolved Contradiction Rule

If contradiction cannot be resolved deterministically from surfaced evidence, replay must downgrade to Unverifiable or lower.

---

## 14. Replay Handling of Ambiguity

Replay must explicitly handle ambiguity.

### 14.1 Ambiguity Detection Rule

Replay must detect ambiguity when evidence could support more than one classification and the distinguishing element is missing or unclear.

### 14.2 Ambiguity Resolution Rule

Replay must choose the weaker justified class.

Example:
- if refusal presence is clear but mechanical effectiveness is unclear, replay must not validate active accompaniment
- if segment support is clear but broader scope sufficiency is unclear, replay must not validate end-to-end active accompaniment
- if crypto posture is present but qualification is unclear, replay must not validate a stronger crypto-dependent class

### 14.3 Ambiguity Ceiling Rule

Ambiguity regarding a required stronger-class element creates a ceiling below that stronger class.

---

## 15. Replay Handling of Evidence Loss

Replay must explicitly handle missing, corrupted, late, or insufficient evidence.

### 15.1 Missing Evidence Rule

If mandatory evidence is missing for the claimed class, replay must reject that class.

### 15.2 Corrupted Evidence Rule

If evidence is surfaced but unusable for deterministic reconstruction, replay must treat it as insufficient for the affected claim.

### 15.3 Late Evidence Rule

Evidence appearing later may support a claim only if surfaced ordering and schema rules make that support valid.

Replay must not let late explanation retroactively repair a defeated stronger claim unless the claim model explicitly permits that evidence relation.

### 15.4 Evidence Loss Downgrade Rule

When evidence loss defeats a stronger class and no lower descriptive class can be safely established, replay must assign Unverifiable.

---

## 16. Replay Output Rules

Replay must produce a strict output, not a narrative only.

### 16.1 Mandatory Replay Output Fields

Replay output must include:
- segment identifier
- claimed classification
- replay-supported final classification
- claimed scope
- replay-supported scope
- classification ceiling reached
- pass/fail result for each tested stronger class
- reasons for each failure or downgrade
- evidence insufficiency findings
- contradiction findings, if any
- ambiguity findings, if any
- downgrade chain
- final replay judgment
- crypto qualification result where claim-relevant

### 16.2 Final Replay Judgment Rule

The final replay judgment must state only the strongest supported class and scope.

It must not preserve stronger claim language once replay has downgraded the claim.

---

## 17. Replay Non-Claim Rules

Replay must reject these invalid outcomes.

### 17.1 Forbidden Replay Outcome: Stronger by Narrative

Replay must not preserve a strong class because the overall story sounds governed.

### 17.2 Forbidden Replay Outcome: Stronger by Architecture Reputation

Replay must not preserve a strong class because the system is generally expected to be rigorous.

### 17.3 Forbidden Replay Outcome: Stronger by Missing Downgrade Event

Replay must not preserve a strong class merely because runtime did not emit a downgrade label.

### 17.4 Forbidden Replay Outcome: Stronger by Partial Evidence

Replay must not preserve a strong class when only some required elements are proven.

### 17.5 Forbidden Replay Outcome: Stronger by Boundary Naming Alone

Replay must not accept a named boundary as the true mutation authority without support.

### 17.6 Forbidden Replay Outcome: Stronger by Hidden Crypto Assumption

Replay must not preserve a stronger class by assuming claim-relevant crypto posture was acceptable when it was absent, hidden, unsupported, or mismatched.

---

## 18. Minimal Replay Chain for Strong Model 9 Support

For SPECTRE-SENTINEL to claim meaningful replay-verifiable Model 9 support beyond concept, replay must be able to reconstruct this minimal chain:

1. segment declared
2. transition identity bound
3. authority and invariant bound
4. covered boundaries established
5. refusal live
6. refusal timely
7. continuity maintained across claimed scope
8. alternate-path status determined
9. truth-boundary support determined
10. crypto posture determined where claim-relevant
11. final class downgraded if needed
12. strongest supported class emitted

If replay cannot reconstruct this chain, strong Model 9 support is not yet established.

---

## 19. Direct Incorporation Rule

SPECTRE-SENTINEL can only claim replay-verifiable Model 9 incorporation to the extent that replay can deterministically distinguish and validate:
- Actively Accompanied
- Segment-Accompanied
- Advisory-Accompanied
- Observed-Only
- Uncovered
- Unverifiable

under:
- explicit scope
- explicit ordering
- explicit downgrade
- explicit evidence sufficiency rules
- claim-relevant crypto posture handling where applicable

---

## 20. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_MINIMAL_ARCHITECTURE_PROFILE.md

This file should be committed before moving to the next split artifact.