# MODEL 9 CONFORMANCE AND CLASSIFICATION RULES

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_TIGHTENING_SPEC.md
- docs/MODEL_9_TO_DTPE_IAL_SPECTRE_MAPPING.md

It defines the conformance and classification rules required to evaluate Model 9 claims in a strict, bounded, replay-verifiable way.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the conformance and classification rules required to evaluate Model 9 claims in a strict, bounded, replay-verifiable way.

It exists to prevent overclaim.

It defines:
- what must be true for a Model 9 claim to conform
- how accompanied segments must be classified
- what events force downgrade
- what evidence is minimally sufficient
- what replay must be able to prove
- what claims must not be made
- how claim-relevant crypto posture affects classification and downgrade

---

## 2. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

BBIS defines what must be true.

DTPE / IAL / SPECTRE / SPECTRE-SENTINEL provides architecture that may satisfy that truth in bounded form.

Do not merge them conceptually.

---

## 3. Standing Architectural Requirement

PQC must be on and always at the ready.

For conformance and classification, this means:
- crypto posture must not be treated as structurally legacy-only
- where crypto posture is relevant to the claim, it must be surfaced and evaluable
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- replay must not hide claim-relevant crypto posture if it affects classification validity

This file does not require a full PQC migration program by itself.

It does require that claim-relevant crypto posture be part of the bounded conformance model where applicable.

---

## 4. Scope

These rules apply only to claimed accompanied segments.

They do not automatically apply to an entire system, workflow, transaction, or end-to-end path unless that broader scope is explicitly claimed and the conformance conditions are satisfied for that broader scope.

No broader scope may be inferred from a narrower one.

---

## 5. Core Conformance Question

A claimed Model 9 segment conforms only if the following question can be answered yes:

Did a persistent, identity-bound, authority-bound, invariant-bound, refusal-capable governance process remain mechanically effective across each explicitly claimed covered mutation-capable boundary in the segment, with evidence sufficient for independent replay of that claim?

If the answer is not yes, the segment does not conform as Actively Accompanied.

---

## 6. Conformance Conditions

A claimed segment conforms as Actively Accompanied only if all conditions below are satisfied.

### 6.1 Segment Explicitness Condition

The claim must explicitly identify:
- segment start
- segment end
- covered boundaries
- claimed irreversible primitive for the segment
- governing authority basis
- governing invariant basis
- claim scope
- claim limitation where broader scope is excluded

If any of these are missing, the segment cannot conform as Actively Accompanied.

### 6.2 Transition Identity Condition

The accompanied process must remain bound to a stable governed transition identity across the claimed segment.

If continuity of transition identity cannot be proven, active conformance fails.

### 6.3 Authority Continuity Condition

The accompanied process must remain bound to the governing authority basis across the claimed segment, or to an explicitly governed successor basis.

If authority continuity cannot be proven, active conformance fails.

### 6.4 Invariant Continuity Condition

The accompanied process must remain bound to the governing invariant basis across the claimed segment, or to an explicitly governed successor basis.

If invariant continuity cannot be proven, active conformance fails.

### 6.5 Coverage Condition

Every mutation-capable boundary required by the claimed segment scope must be explicitly covered.

If a required boundary is uncovered, active conformance fails for that scope.

### 6.6 Refusal Capability Condition

At every claimed covered boundary, refusal must be mechanically effective.

If the process can observe, recommend, warn, revoke later, impose cost later, or log only, this condition is not satisfied.

### 6.7 Timing Condition

Refusal capability must be live in time to prevent mutation before completion at the claimed covered boundary.

If refusal exists only after mutation becomes operationally binding, active conformance fails.

### 6.8 Alternate Path Closure Condition

No relevant alternate mutation path may bypass accompaniment for the claimed scope, unless the claim explicitly excludes those paths.

If such a path exists and is not covered or explicitly excluded from the claim scope, active conformance fails for that broader scope.

### 6.9 Truth-Boundary Condition

The claimed covered boundary must correspond to the actual mutation authority for the scope being claimed.

If the claimed boundary is not the true mutation authority, active conformance fails.

### 6.10 Evidence Sufficiency Condition

Evidence must be sufficient for independent replay of the claim-level facts.

If evidence is insufficient, active conformance fails and the segment must be downgraded.

### 6.11 Crypto Posture Condition

Where crypto posture is relevant to the claim, the relevant crypto posture must be surfaced, compatible with the claim, and not contradicted by the evidence.

If claim-relevant crypto posture is unsupported, mismatched, absent, or hidden from replay, active conformance fails and the segment must downgrade or fail closed.

---

## 7. Classification States

Each claimed segment must be classified into exactly one state.

### 7.1 Actively Accompanied

Use only if all conformance conditions in Section 6 are satisfied.

This is the strongest valid Model 9 classification.

It means:
- explicit segment
- stable transition identity
- stable authority basis
- stable invariant basis
- covered required boundaries
- mechanically effective refusal
- timely refusal
- no relevant uncovered alternate mutation path for claimed scope, unless explicitly outside claim scope
- correct mutation-boundary identification
- replay-sufficient evidence
- claim-relevant crypto posture satisfied where applicable

### 7.2 Segment-Accompanied

Use when active accompaniment is proven only for a narrower bounded segment than the surrounding workflow.

This means:
- the accompanied claim is valid, but only for the explicitly bounded segment
- no broader end-to-end claim is valid from that fact alone

This is a conforming but scope-limited class.

### 7.3 Advisory-Accompanied

Use when a persistent accompaniment process exists, but refusal is not mechanically effective or not timely.

Examples include:
- continuous observation
- live scoring
- warning generation
- recommendation emission
- revocation after commit
- post-event interruption only

This is not active accompaniment.

### 7.4 Observed-Only

Use when the system has visibility into the segment but no valid accompaniment claim exists.

This means the system can see, log, or reconstruct events, but not claim persistent refusal-capable continuity.

### 7.5 Uncovered

Use when no accompaniment claim applies to the segment.

This includes cases where:
- accompaniment was never established
- covered boundaries were not defined
- the segment lies outside accompaniment scope

### 7.6 Unverifiable

Use when a stronger claim was made or implied, but the evidence is insufficient to verify it independently.

This class is mandatory whenever proof is missing or contradiction cannot be resolved into a stronger supported lower class.

---

## 8. Classification Decision Rules

Apply the following rules in order.

### Rule 1
If no accompanied segment was explicitly claimed, classify as:
- Observed-Only, or
- Uncovered

depending on whether visibility exists.

### Rule 2
If a segment was claimed but evidence is insufficient to verify the claim, classify as:
- Unverifiable

### Rule 3
If the process was persistent but lacked mechanically effective refusal, classify as:
- Advisory-Accompanied

### Rule 4
If refusal existed but was not timely relative to mutation completion, classify as:
- Advisory-Accompanied

### Rule 5
If accompaniment covered only a bounded sub-segment and no broader scope is proven, classify as:
- Segment-Accompanied

### Rule 6
If all conformance conditions are satisfied for the claimed segment, classify as:
- Actively Accompanied

### Rule 7
If no valid accompanied claim applies at all, classify as:
- Uncovered

### Rule 8
If claim-relevant crypto posture defeats a stronger class, enforce the resulting lower classification ceiling immediately.

---

## 9. Downgrade Triggers

A stronger classification must be downgraded immediately when any trigger below occurs.

### 9.1 Identity Discontinuity Trigger
Downgrade when continuity of governed transition identity can no longer be proven.

### 9.2 Authority Drift Trigger
Downgrade when authority continuity is broken, ambiguous, or no longer replay-verifiable.

### 9.3 Invariant Drift Trigger
Downgrade when invariant continuity is broken, ambiguous, or no longer replay-verifiable.

### 9.4 Coverage Loss Trigger
Downgrade when a claimed required covered boundary is no longer covered.

### 9.5 Refusal Failure Trigger
Downgrade when refusal is no longer mechanically effective.

### 9.6 Timing Failure Trigger
Downgrade when refusal exists but can no longer act before mutation completion.

### 9.7 Alternate Path Exposure Trigger
Downgrade when an uncontrolled mutation path becomes available for the claimed scope, unless the claim explicitly excludes that path.

### 9.8 Truth-Boundary Failure Trigger
Downgrade when the claimed boundary is found not to be the actual mutation authority.

### 9.9 Evidence Loss Trigger
Downgrade when evidence required for replay is missing, corrupted, ambiguous, or insufficient.

### 9.10 Scope Inflation Trigger
Downgrade when a bounded accompanied fact is presented as an end-to-end accompanied claim without proof.

### 9.11 Crypto Posture Trigger
Downgrade when claim-relevant crypto posture is unsupported, mismatched, absent, contradicted, or hidden from replay.

---

## 10. Downgrade Rules

Downgrade must follow the strongest justified lower class only.

### 10.1 From Actively Accompanied

Downgrade to:
- Segment-Accompanied, if narrower bounded conformance still holds
- Advisory-Accompanied, if persistence remains but refusal no longer qualifies
- Unverifiable, if proof is insufficient or contradiction defeats the stronger class
- Uncovered, if no valid accompanied claim remains

### 10.2 From Segment-Accompanied

Downgrade to:
- Advisory-Accompanied
- Unverifiable
- Uncovered

depending on what remains provable.

### 10.3 From Advisory-Accompanied

Downgrade to:
- Observed-Only, if persistence cannot be proven but observation remains
- Unverifiable, if even observation cannot be proven sufficiently
- Uncovered, if no claim remains

### 10.4 No Upward Inference Rule

No stronger class may be inferred from a weaker one without fresh proof satisfying the higher class.

---

## 11. Minimum Evidence Thresholds

A classification above Observed-Only requires explicit evidence.

### 11.1 Minimum Evidence for Segment-Accompanied

At minimum, evidence must show:
- segment identity
- segment start and end
- governed transition identity
- accompaniment instance identity
- authority basis
- invariant basis
- claimed covered boundaries within the segment
- final bounded classification

### 11.2 Minimum Evidence for Actively Accompanied

At minimum, evidence must show all of the above plus:
- mechanically effective refusal path identity
- refusal-capability state at each claimed covered boundary
- timing sufficiency relative to mutation completion
- absence of relevant uncovered alternate mutation path for claimed scope, or explicit proof that scope excludes them
- claimed irreversible primitive
- final pass/refuse outcome at covered boundaries
- continuity maintenance or continuity-preserving successor relation if successors are in scope
- any downgrade events, if present
- claim-relevant crypto posture where applicable

### 11.3 Minimum Evidence for Advisory-Accompanied

At minimum, evidence must show:
- persistent accompaniment process identity
- governed transition identity
- segment bounds
- reason refusal did not qualify as mechanically effective or timely

### 11.4 Evidence Rule

If the evidence cannot support the class claimed, the classification must be downgraded.

---

## 12. Replay Pass / Fail Rules

Replay must test whether the claimed classification is supported by surfaced evidence.

### 12.1 Replay Pass for Actively Accompanied

Replay passes only if it can determine all of the following from surfaced evidence:
- what segment was claimed
- what transition was governed
- what authority basis governed it
- what invariant basis governed it
- what boundaries were claimed as covered
- what irreversible primitive was claimed
- that refusal remained mechanically effective at each covered boundary
- that refusal was timely
- that no relevant alternate mutation path escaped for claimed scope, unless explicitly excluded
- that identity continuity held
- that authority continuity held
- that invariant continuity held
- that claim-relevant crypto posture was properly surfaced and satisfied where applicable
- that the final class did not exceed the evidence

If replay cannot establish any required element, replay fails for this class.

### 12.2 Replay Pass for Segment-Accompanied

Replay passes only if it can establish bounded active accompaniment for the narrower claimed segment, even if no broader workflow claim is justified.

### 12.3 Replay Pass for Advisory-Accompanied

Replay passes only if it can establish persistent accompaniment presence but also establish that refusal did not qualify as mechanically effective or timely.

### 12.4 Replay Fail Rule

If replay cannot verify the claimed classification, the result must be downgraded to Unverifiable or lower.

---

## 13. Non-Claim Rules

The following claims are forbidden unless separately proven.

### 13.1 Forbidden Claim: Universal End-to-End Continuity
A bounded accompanied segment must not be described as end-to-end governance continuity without proof covering the full claimed path.

### 13.2 Forbidden Claim: Observation Equals Governance
Observation alone must not be described as active accompaniment.

### 13.3 Forbidden Claim: Persistent Presence Equals Refusal
A persistent agent, sidecar, enclave, monitor, or watcher must not be described as active accompaniment unless mechanically effective refusal is proven.

### 13.4 Forbidden Claim: One Path Governs All Paths
Coverage of one mutation path must not be described as governance of all paths unless alternate path closure is proven or broader paths are explicitly outside claim scope.

### 13.5 Forbidden Claim: Claimed Boundary Equals True Boundary by Assertion
A claimed boundary must not be treated as the true mutation authority without proof or grounded architectural basis.

### 13.6 Forbidden Claim: Missing Evidence Can Be Inferred
Missing continuity, authority, invariant, timing, refusal, scope, or crypto-posture evidence must not be inferred.

### 13.7 Forbidden Claim: PQC Can Be Ignored Without Claim Impact
Where crypto posture is relevant to the claim, it must not be treated as irrelevant or deferrable without architectural consequence.

---

## 14. Exact Distinctions That Must Be Preserved

The classification system must preserve these distinctions without collapse.

### 14.1 Declared vs Enforced
A declared accompaniment claim is not the same as an enforced accompaniment state.

### 14.2 Attested vs Mechanically Effective
An attested refusal path is not the same as a mechanically effective refusal path.

### 14.3 Observed vs Refusal-Capable
Observation is not refusal capability.

### 14.4 Persistent vs Active
Persistent accompaniment is not active accompaniment unless refusal remains live and effective.

### 14.5 Bounded Segment vs End-to-End Path
A segment-conforming claim is not an end-to-end conforming claim.

### 14.6 Replay-Described vs Replay-Verified
A replay narrative is not replay verification unless the evidence suffices to prove the claimed class.

### 14.7 Crypto Present vs Crypto Claim-Satisfying
A crypto posture being present is not the same as it satisfying the claim-relevant classification requirement.

---

## 15. Conformance Output Format

A valid conformance result for any claimed segment should state, at minimum:
- claimed segment
- claimed classification
- governing authority basis
- governing invariant basis
- covered boundaries
- claimed irreversible primitive
- whether refusal qualified
- whether timing qualified
- whether alternate path closure qualified or claim scope explicitly excluded such paths
- whether evidence sufficed
- whether claim-relevant crypto posture qualified where applicable
- final classification
- reason for any downgrade

---

## 16. Direct Final Rule

The governing rule is:

A Model 9 claim is only as strong as the strongest classification that can be independently supported by explicit coverage, mechanically effective refusal, continuity of identity, authority, and invariant, correct mutation-boundary identification, replay-sufficient evidence, and claim-relevant crypto posture where applicable.

Nothing stronger may be claimed.

---

## 17. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_STATE_MODEL.md

This file should be committed before moving to the next split artifact.