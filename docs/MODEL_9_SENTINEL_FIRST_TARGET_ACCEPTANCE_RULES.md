# MODEL 9 SENTINEL FIRST TARGET ACCEPTANCE RULES

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_SENTINEL_FIRST_INCORPORATION_TARGET.md

It defines the exact acceptance rules for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the exact acceptance rules for the first Model 9 incorporation target in SPECTRE-SENTINEL.

It defines only:
- exact pass/fail conditions
- exact evidence required for acceptance
- exact downgrade conditions that fail acceptance
- exact permitted public wording on acceptance
- exact rejection reasons if the target is incomplete
- exact PQC-ready requirement treatment where claim-relevant

---

## 2. Governing Acceptance Rule

The first target is accepted only if SPECTRE-SENTINEL can prove one explicitly bounded accompanied segment with one explicitly covered mutation-capable boundary, using:
- one governed transition identity
- one authority basis
- one invariant basis
- one mechanically effective and timely refusal surface
- fail-closed downgrade behavior
- replay-sufficient evidence for that exact scope
- claim-relevant crypto posture handling where applicable
- PQC-ready posture preserved as an active requirement

Anything less fails acceptance.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For acceptance, this means:
- the first target must not depend on a structurally legacy-only crypto posture
- where crypto posture is relevant to the claim, it must be surfaced and evaluated
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- acceptance must not rely on postponing PQC readiness outside the bounded architecture posture

This file does not require a full PQC migration program by itself.

It does require that acceptance preserve PQC-ready architecture posture as active, not decorative.

---

## 5. Acceptance Scope

Acceptance applies only to the first target defined as:
- one segment
- one covered boundary
- one governed transition identity
- one authority basis
- one invariant basis
- one refusal-capable surface
- one replay-verifiable evidence chain
- one bounded claim ceiling
- claim-relevant crypto posture handling where applicable

Acceptance of this first target does not imply acceptance of:
- multi-boundary accompaniment
- end-to-end accompaniment
- downstream continuity
- alternate-path closure beyond explicitly supported scope
- full Model 9 incorporation
- full BBIS closure
- full PQC migration completion
- full crypto-agility completion

No broader acceptance may be inferred.

---

## 6. Exact Pass Conditions

The first target passes only if all pass conditions below are satisfied.

### 6.1 Pass Condition P1 - Explicit Segment Definition

The target must define one explicit segment with:
- segment identifier
- segment start condition
- segment end condition
- segment scope statement
- covered boundary identifier
- claimed irreversible primitive for that segment

If any element is missing, fail.

### 6.2 Pass Condition P2 - Stable Governed Transition Identity

The target must prove one stable governed transition identity bound to the accompanied segment.

Required proof:
- governed transition identifier
- accompaniment instance identifier
- binding relation between them

If identity continuity cannot be proven for the segment, fail.

### 6.3 Pass Condition P3 - Bound Authority Basis

The target must prove one authority basis bound to the accompanied segment.

Required proof:
- authority basis identifier
- authority binding record

If authority basis is declared only but not bound, fail.

### 6.4 Pass Condition P4 - Bound Invariant Basis

The target must prove one invariant basis bound to the accompanied segment.

Required proof:
- invariant basis identifier
- invariant binding record

If invariant basis is declared only but not bound, fail.

### 6.5 Pass Condition P5 - Explicit Covered Boundary

The target must prove that exactly one mutation-capable boundary is the covered boundary for the first-target scope.

Required proof:
- covered boundary identifier
- scope statement tying the claim to that boundary
- statement that broader boundary coverage is not being claimed

If coverage is implicit or ambiguous, fail.

### 6.6 Pass Condition P6 - Real Mechanically Effective Refusal

The target must prove one refusal surface that can actually prevent the mutation at the covered boundary.

Required proof:
- refusal path identifier
- refusal-path-to-covered-boundary association
- evidence that refusal is mechanically effective, not merely advisory

If refusal is only observational, recommendatory, revocatory after commit, or punitive after commit, fail.

### 6.7 Pass Condition P7 - Timely Refusal

The target must prove that refusal is live in time to act before mutation completion at the covered boundary.

Required proof:
- timing qualification evidence
- ordering basis sufficient to show refusal was timely relative to mutation completion

If refusal exists but timeliness is not proven, fail.

### 6.8 Pass Condition P8 - Required State Path Support

The target must support the minimum success path:
- Uninitialized
- Segment-Declared
- Identity-Bound
- Authority-Bound
- Coverage-Established
- Refusal-Live
- Actively-Accompanying
- Completed

Where crypto posture is claim-relevant, it must also support:
- Crypto-Qualified

before Actively-Accompanying.

Required proof:
- evidence sufficient to reconstruct this path for the exact segment

If this path cannot be reconstructed, fail.

### 6.9 Pass Condition P9 - Required Downgrade Support

The target must prove fail-closed downgrade behavior for at least:
- refusal failure
- evidence insufficiency
- coverage loss
- crypto failure where claim-relevant

Required proof:
- downgrade event structure or equivalent evidence
- resulting lower state or classification ceiling

If stronger claims can silently survive failure, fail.

### 6.10 Pass Condition P10 - Replay Sufficiency

The target must prove that replay can determine, for the exact bounded scope:
- what was claimed
- what was bound
- what boundary was covered
- whether refusal was live
- whether refusal was timely
- whether downgrade occurred
- what final class is actually supported
- whether claim-relevant crypto posture qualified where applicable

If replay cannot independently determine these, fail.

### 6.11 Pass Condition P11 - Classification Ceiling Discipline

The target must keep its final claim at the bounded first-target ceiling.

Required proof:
- final classification record
- claim-limitation statement
- no broader public or architectural wording exceeding supported scope

If broader claim language is used, fail.

### 6.12 Pass Condition P12 - Claim-Relevant Crypto Qualification

Where crypto posture is relevant to the claim, the target must prove that the relevant crypto posture is surfaced, evaluated, and either:
- qualified for the stronger claim, or
- correctly caused downgrade or fail-closed outcome

If claim-relevant crypto posture is hidden, ignored, unsupported, mismatched, or allowed to pass silently, fail.

---

## 7. Exact Evidence Required for Acceptance

Acceptance requires at minimum the following evidence chain.

### 7.1 Mandatory Evidence Chain

1. segment declaration record
2. governed transition identity binding record
3. authority binding record
4. invariant binding record
5. coverage establishment record
6. claimed irreversible primitive record for the segment
7. refusal path record
8. refusal-live record
9. timing qualification record
10. active accompaniment state record
11. downgrade record structure for failure cases
12. completion record
13. final classification record
14. evidence sufficiency record
15. claim-relevant crypto qualification record where applicable

If any mandatory link is missing, acceptance fails.

### 7.2 Evidence Quality Rule

Acceptance evidence must be:
- explicit
- ordered
- scope-bound
- replay-usable
- non-contradictory for the accepted class

Narrative explanation alone is insufficient.

---

## 8. Exact Downgrade Conditions That Fail Acceptance

The following conditions require first-target rejection if present unresolved within the claimed accepted target.

### 8.1 Failure Condition F1 - Identity Discontinuity

Reject if:
- governed transition identity continuity cannot be proven for the segment

Reason:
- accompaniment continuity collapses without stable governed identity

### 8.2 Failure Condition F2 - Authority Discontinuity

Reject if:
- authority basis is missing, unbound, changed without governed handling, or unprovable

Reason:
- governance continuity cannot be claimed without stable authority basis

### 8.3 Failure Condition F3 - Invariant Discontinuity

Reject if:
- invariant basis is missing, unbound, changed without governed handling, or unprovable

Reason:
- the system cannot prove what remained live

### 8.4 Failure Condition F4 - Coverage Ambiguity or Loss

Reject if:
- the covered boundary is not explicit
- multiple boundaries are effectively implicated without bounded handling
- coverage loss occurs without fail-closed treatment

Reason:
- the first target must remain single-boundary and explicit

### 8.5 Failure Condition F5 - Refusal Ineffectiveness

Reject if:
- refusal cannot actually stop the mutation at the covered boundary

Reason:
- the first target requires real refusal, not advisory accompaniment

### 8.6 Failure Condition F6 - Timing Failure

Reject if:
- refusal timeliness cannot be proven relative to mutation completion

Reason:
- untimely refusal does not qualify for active accompaniment

### 8.7 Failure Condition F7 - Replay Insufficiency

Reject if:
- replay cannot reconstruct the claim and validate the bounded class independently

Reason:
- the first target must be replay-verifiable

### 8.8 Failure Condition F8 - Silent Stronger-Claim Survival

Reject if:
- failure can occur without downgrade
- stronger classification remains by inertia after defeat of required conditions

Reason:
- the first target must fail closed

### 8.9 Failure Condition F9 - Scope Inflation

Reject if:
- the target is described as broader than one bounded segment and one covered boundary
- wording implies workflow-wide, end-to-end, or downstream continuity

Reason:
- first-target acceptance is strictly bounded

### 8.10 Failure Condition F10 - Contradictory Evidence

Reject if:
- evidence simultaneously supports and defeats required elements of the accepted class, and the contradiction is not resolved by downgrade to a lower class

Reason:
- first-target acceptance cannot rest on unresolved contradiction

### 8.11 Failure Condition F11 - Crypto Posture Failure

Reject if:
- claim-relevant crypto posture is unsupported, mismatched, absent, hidden from replay, or otherwise unresolved while the stronger accepted class attempts to survive

Reason:
- claim-relevant crypto posture must not be silently bypassed

---

## 9. Acceptance Output Rule

If the first target passes, the acceptance output must state only:
- accepted target scope
- accepted classification ceiling
- accepted evidence basis
- accepted downgrade discipline
- accepted replay basis
- accepted crypto qualification basis where applicable
- non-claim boundary

It must not imply broader incorporation.

---

## 10. Exact Permitted Public Wording on Acceptance

The strongest permitted public wording is:

SPECTRE-SENTINEL supports replay-verifiable bounded Model 9 segment accompaniment for one explicitly declared segment with one covered mutation-capable boundary, where governed transition identity, authority basis, invariant basis, mechanically effective refusal, timing qualification, downgrade behavior, and evidence sufficiency are supported for that exact scope, with claim-relevant crypto posture handled where applicable.

A shorter permitted version is:

SPECTRE-SENTINEL supports bounded replay-verifiable active accompaniment for a single explicitly scoped segment and covered boundary.

A weaker permitted version, if the stronger class is not achieved, is:

SPECTRE-SENTINEL supports governance-bound advisory accompaniment for a bounded segment.

Only the strongest actually supported version may be used.

---

## 11. Exact Forbidden Public Wording on Acceptance

Even after acceptance, the following remain forbidden:
- "SPECTRE-SENTINEL implements Model 9"
- "SPECTRE-SENTINEL provides end-to-end active accompaniment"
- "SPECTRE-SENTINEL governs downstream continuity"
- "SPECTRE-SENTINEL proves full continuous governance"
- "SPECTRE-SENTINEL closes BBIS"
- "SPECTRE-SENTINEL governs all mutation paths"
- "SPECTRE-SENTINEL solves mutation-bound continuity"
- "SPECTRE-SENTINEL provides universal live refusal"
- "SPECTRE-SENTINEL completes PQC migration"
- "SPECTRE-SENTINEL fully solves crypto agility"

These exceed first-target acceptance.

---

## 12. Exact Rejection Reasons

If the first target fails, rejection must identify the exact reason.

Allowed rejection reasons:
- segment not explicitly bounded
- governed transition identity not stably bound
- authority basis not bound
- invariant basis not bound
- covered boundary not explicit
- refusal not mechanically effective
- refusal timing not proven
- required state path not reconstructable
- required downgrade behavior missing
- replay insufficiency
- scope inflation
- contradictory evidence unresolved
- claim-relevant crypto posture failure
- accepted claim exceeds evidence-supported ceiling

Rejection must be specific.

Generic rejection such as "not ready" is insufficient.

---

## 13. Acceptance Ceiling

Even when accepted, the first target's honest ceiling is:

bounded segment accompaniment only

Program-level wording should keep that ceiling.

The target may internally validate Actively Accompanied for the exact segment scope if the full exact segment claim is supported.

But public and architecture-level framing for the first target should remain:
- bounded
- single-segment
- single-boundary
- non-universal
- first-step only

---

## 14. Final Acceptance Test

The final acceptance question is:

For one explicitly bounded segment and one explicitly covered mutation-capable boundary, can SPECTRE-SENTINEL independently prove identity-bound, authority-bound, invariant-bound, mechanically effective, timely, downgrade-disciplined, replay-verifiable active accompaniment for that exact scope only, with claim-relevant crypto posture handled where applicable, without broader overclaim?

If yes, accept.

If no, reject.

---

## 15. Direct Recommendation

The first target should not be accepted early.

Acceptance should be withheld unless all pass conditions are satisfied and all rejection conditions are cleared for the exact bounded scope.

That is the correct strict acceptance rule.

---

## 16. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_FIRST_TARGET_IMPLEMENTATION_CHECKLIST.md

This file should be committed before moving to the next split artifact.