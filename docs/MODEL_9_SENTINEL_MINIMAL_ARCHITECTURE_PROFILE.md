# MODEL 9 SENTINEL MINIMAL ARCHITECTURE PROFILE

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_TIGHTENING_SPEC.md
- docs/MODEL_9_SENTINEL_REPLAY_RULES.md

It defines the smallest architecture capability set required for SPECTRE-SENTINEL to support Model 9 in a meaningful, bounded, honest way.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the smallest architecture capability set required for SPECTRE-SENTINEL to support Model 9 in a meaningful, bounded, honest way.

It defines:
- which capabilities are mandatory
- which capabilities are optional
- what minimum claim each capability set permits
- what classification ceiling applies when capabilities are missing
- what a minimal honest first incorporation target looks like
- how PQC-on / PQC-ready posture must remain preserved

---

## 2. Governing Architecture Rule

SPECTRE-SENTINEL may claim only the strongest Model 9 support level justified by the architecture capabilities it can actually sustain, surface, and replay.

Capabilities not present must not be assumed.

Capabilities present but not surfaced as evidence do not justify stronger claims.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For the minimal architecture profile, this means:
- no capability tier may assume a structurally legacy-only crypto posture
- claim-relevant crypto posture must remain available to evidence and replay where applicable
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- first-target architecture must not require redesign from scratch to remain PQC-ready

This file does not require a full PQC migration program by itself.

It does require that the architecture remain compatible with an active PQC-ready posture.

---

## 5. Design Objective

The objective is not to achieve universal active accompaniment immediately.

The objective is to define the minimum bounded architecture that allows SPECTRE-SENTINEL to begin incorporating Model 9 without overclaim.

That means the first target should aim for:
- explicit segment declaration
- stable transition identity
- authority and invariant binding
- explicit covered boundary scope
- at least one real refusal-capable boundary
- downgrade discipline
- replay-sufficient evidence for the bounded claim
- PQC-ready crypto posture preserved as an active requirement

Anything less is concept only.

---

## 6. Capability Categories

The minimal architecture profile is organized into capability categories.

### 6.1 Segment Capability
Ability to define a bounded accompanied segment explicitly.

### 6.2 Identity Capability
Ability to bind accompaniment to a stable governed transition identity.

### 6.3 Authority Capability
Ability to bind accompaniment to governing authority and invariant basis.

### 6.4 Coverage Capability
Ability to state which boundaries are covered and which are not.

### 6.5 Refusal Capability
Ability to mechanically prevent mutation at at least one claimed covered boundary.

### 6.6 Timing Capability
Ability to establish that refusal is live before mutation completion.

### 6.7 Downgrade Capability
Ability to terminate or lower stronger claims when conditions fail.

### 6.8 Evidence Capability
Ability to surface evidence sufficient for replay of the bounded claim.

### 6.9 Replay Capability
Ability to reconstruct and verify the bounded claim from surfaced evidence.

### 6.10 Alternate-Path Capability
Ability to detect or explicitly limit claims relative to uncovered mutation paths.

### 6.11 Truth-Boundary Capability
Ability to support the claim that the named covered boundary is the relevant mutation authority for the bounded scope.

### 6.12 Crypto Capability
Ability to surface and evaluate claim-relevant crypto posture where applicable.

---

## 7. Mandatory Minimum Capability Set

This is the smallest capability set that allows meaningful first incorporation beyond concept only.

### 7.1 Mandatory Capability M1 - Explicit Segment Declaration

The architecture must be able to declare:
- segment identifier
- segment scope
- segment start
- segment end
- claimed covered boundary or boundaries
- claimed irreversible primitive for the segment
- authority basis
- invariant basis

Without this, no bounded Model 9 claim exists.

Minimum claim enabled:
- bounded accompanied intent only

If missing, classification ceiling:
- Uncovered or Observed-Only only

### 7.2 Mandatory Capability M2 - Stable Transition Identity Binding

The architecture must be able to bind the accompaniment instance to a stable governed transition identity for the claimed segment.

Without this, accompaniment continuity cannot be claimed.

Minimum claim enabled:
- bounded accompanied tracking tied to a real governed transition

If missing, classification ceiling:
- Observed-Only only

### 7.3 Mandatory Capability M3 - Authority and Invariant Binding

The architecture must be able to bind the accompanied segment to:
- governing authority basis
- governing invariant basis

Without this, accompaniment is not governance continuity.

Minimum claim enabled:
- governance-relevant bounded accompaniment

If missing, classification ceiling:
- Observed-Only only

### 7.4 Mandatory Capability M4 - Explicit Coverage Surface

The architecture must be able to state exactly:
- what boundary is covered
- what scope is covered
- what scope is not covered

Without this, Model 9 cannot avoid scope inflation.

Minimum claim enabled:
- segment-bounded claim with explicit limits

If missing, classification ceiling:
- Observed-Only or Unverifiable

### 7.5 Mandatory Capability M5 - At Least One Mechanically Effective Refusal Surface

The architecture must support refusal that can actually prevent mutation at at least one covered boundary in the claimed segment.

Without this, Model 9 incorporation is advisory only.

Minimum claim enabled:
- Segment-Accompanied for a narrow bounded segment, if all other required conditions also hold

If missing, classification ceiling:
- Advisory-Accompanied at best

### 7.6 Mandatory Capability M6 - Timing Qualification for Refusal

The architecture must be able to show that refusal is live before mutation completion at the covered boundary.

Without this, refusal may exist but not qualify.

Minimum claim enabled:
- active bounded accompaniment at the covered boundary

If missing, classification ceiling:
- Advisory-Accompanied at best

### 7.7 Mandatory Capability M7 - Downgrade and Fail-Closed Handling

The architecture must be able to:
- detect loss of stronger conditions
- emit downgrade state or equivalent evidence
- stop preserving stronger claims after failure

Without this, incorporation is unsafe.

Minimum claim enabled:
- honest bounded accompaniment with classification discipline

If missing, classification ceiling:
- Unverifiable for stronger claims

### 7.8 Mandatory Capability M8 - Replay-Sufficient Evidence Emission

The architecture must surface enough evidence to replay:
- what was claimed
- what was bound
- what boundary was covered
- whether refusal existed
- whether refusal was timely
- whether downgrade occurred
- what final class is justified

Without this, incorporation is not independently verifiable.

Minimum claim enabled:
- replay-verifiable Segment-Accompanied or stronger, depending on other capabilities

If missing, classification ceiling:
- Unverifiable

### 7.9 Mandatory Capability M9 - Deterministic Claim-Level Replay

The architecture must support replay sufficient to determine the strongest justified classification for the segment.

Without replay, Model 9 remains descriptive only.

Minimum claim enabled:
- replay-validated bounded accompaniment

If missing, classification ceiling:
- Unverifiable

### 7.10 Mandatory Capability M10 - Claim-Relevant Crypto Surface

Where crypto posture is relevant to the claim, the architecture must be able to:
- surface the relevant crypto posture
- bind it to the claim where required
- fail closed or downgrade if unsupported or mismatched
- expose it to replay

Without this, a crypto-dependent stronger claim cannot stand honestly.

Minimum claim enabled:
- bounded claim with claim-relevant crypto posture discipline preserved

If missing when claim-relevant, classification ceiling:
- Unverifiable or lower for the affected stronger claim

---

## 8. Optional but Important Capability Set

These capabilities are not strictly required for first bounded incorporation, but they materially strengthen Model 9 support.

### 8.1 Optional Capability O1 - Alternate-Path Detection or Explicit Scope Exclusion

The architecture can either:
- prove there is no relevant uncovered alternate mutation path for the claimed scope, or
- explicitly narrow the claim to exclude paths not covered

Benefit:
Prevents one accompanied path from being overstated as broader governance.

If absent:
Broader claims must not be made.

### 8.2 Optional Capability O2 - Truth-Boundary Support

The architecture can support the claim that the named covered boundary is the relevant mutation authority for the bounded scope.

Benefit:
Prevents accompaniment at the wrong boundary from being mislabeled as closure.

If absent:
Only weaker bounded claims should survive.

### 8.3 Optional Capability O3 - Continuity-Preserving Successor Support

The architecture can prove that a later accompaniment instance is a valid continuity-preserving successor to an earlier one.

Benefit:
Supports multi-step or transferred accompaniment without identity collapse.

If absent:
Model 9 support may be limited to simpler single-instance segments.

### 8.4 Optional Capability O4 - Fine-Grained Coverage Loss Reporting

The architecture can state precisely:
- where coverage ended
- which narrower scope, if any, still survives

Benefit:
Supports cleaner downgrade and more precise retained claims.

If absent:
Replay may have to drop to a weaker lower class more often.

### 8.5 Optional Capability O5 - Explicit Advisory-State Support

The architecture can positively distinguish:
- active refusal-capable accompaniment
- persistent but non-refusal accompaniment

Benefit:
Improves classification quality and avoids conflating missing proof with advisory presence.

### 8.6 Optional Capability O6 - Expanded Crypto Agility Support

The architecture can support multiple claim-relevant crypto postures without structural redesign.

Benefit:
Improves long-term PQC-ready posture and claim portability.

If absent:
The first target may still succeed, but broader future crypto transitions may require additional architecture work.

---

## 9. Capability Tiers

To keep incorporation honest, the minimal architecture profile should use capability tiers.

### 9.1 Tier 0 - Concept Only

Capabilities present:
- none, or descriptive discussion only

Permitted claim:
- conceptual alignment with Model 9 only

Forbidden claim:
- any actual accompanied classification support

Classification ceiling:
- none

### 9.2 Tier 1 - Observability Foundation

Capabilities present:
- M1 explicit segment declaration
- some visibility into segment events

Permitted claim:
- observed bounded segment only

Forbidden claim:
- accompaniment continuity
- governance continuity
- active refusal

Classification ceiling:
- Observed-Only

### 9.3 Tier 2 - Governance-Bound Advisory Accompaniment

Capabilities present:
- M1 segment declaration
- M2 transition identity binding
- M3 authority and invariant binding
- M4 explicit coverage
- evidence of persistent accompaniment presence
- no proven mechanically effective refusal or no proven timing qualification

Permitted claim:
- governance-bound advisory accompaniment for a bounded segment

Forbidden claim:
- active accompaniment
- real refusal-capable continuity

Classification ceiling:
- Advisory-Accompanied

### 9.4 Tier 3 - Minimal Active Segment Accompaniment

Capabilities present:
- M1 through M9
- at least one covered refusal-capable boundary
- timing qualification for that boundary
- replay-sufficient evidence for the narrow segment
- M10 where crypto posture is claim-relevant

Permitted claim:
- replay-verifiable active accompaniment for an explicitly bounded segment

Forbidden claim:
- end-to-end continuity unless separately proven
- multi-boundary closure unless covered and evidenced

Classification ceiling:
- Segment-Accompanied, and in some tightly bounded cases Actively Accompanied for that exact segment scope

This is the minimum honest first incorporation target.

### 9.5 Tier 4 - Stronger Multi-Boundary Bounded Accompaniment

Capabilities present:
- Tier 3
- O1 alternate-path detection or explicit exclusion
- O2 truth-boundary support
- O3 continuity-preserving successor support where needed
- O4 fine-grained coverage loss reporting
- O6 expanded crypto agility support where relevant

Permitted claim:
- stronger bounded accompaniment across more than one covered boundary with more precise replay and downgrade

Forbidden claim:
- universal end-to-end governance continuity without full proof

Classification ceiling:
- Actively Accompanied for the exact bounded scope actually proven

---

## 10. Capability-to-Classification Mapping

| Capability Condition | Maximum Honest Classification |
|---|---|
| Segment declaration only | Observed-Only at best |
| Identity + authority binding but no refusal | Advisory-Accompanied at best |
| Refusal exists but timing unproven | Advisory-Accompanied at best |
| Refusal timely at one covered boundary, replay-sufficient, narrow explicit scope | Segment-Accompanied |
| Refusal timely across full exact claimed bounded scope, no defeated required element | Actively Accompanied |
| Evidence missing for a stronger claim | Unverifiable |
| No accompanied claim or no covered scope | Uncovered |
| Claim-relevant crypto posture missing or unsupported | Unverifiable or lower for the affected stronger claim |

---

## 11. Minimal Honest First Incorporation Target

The correct first target for SPECTRE-SENTINEL is:

one explicitly bounded accompanied segment with one real refusal-capable covered boundary, full identity and authority binding, explicit scope limits, downgrade handling, replay-sufficient evidence, and PQC-ready crypto posture preserved as an active requirement.

That is the minimum target that is both:
- meaningful
- honest
- compatible with Model 9

This first target should not attempt:
- end-to-end workflow accompaniment
- broad multi-system continuity
- universal downstream governance
- unstated alternate-path closure
- truth-boundary claims beyond the exact bounded scope that can be supported
- broad crypto-agility claims beyond the bounded target

---

## 12. What the First Target Must Be Able to Say

At minimum, the first incorporation target should be able to say:
- this exact segment was declared
- this exact governed transition was accompanied
- this exact authority and invariant basis governed it
- this exact boundary was covered
- refusal was mechanically effective here
- refusal was timely here
- this is the exact scope of the claim
- stronger broader claims are not being made
- downgrade occurs if these conditions fail
- replay can independently validate the claim
- claim-relevant crypto posture is surfaced and handled where applicable
- PQC-ready posture is preserved as active architecture posture

If it cannot say those things, the first target is not ready.

---

## 13. What the First Target Must Not Say

The first target must not say:
- the whole workflow was accompanied
- all downstream mutation points were governed
- a persistent sidecar or enclave alone established governance continuity
- observation alone counted as accompaniment
- one covered path governed all paths
- the named boundary was the true mutation authority unless that was explicitly supported
- the system has implemented Model 9 in full
- PQC can be ignored until later without affecting the claim

The honest claim is narrower.

---

## 14. Direct Recommendation for SPECTRE-SENTINEL

The immediate architecture goal should be:

Build Tier 3, not Tier 4 first.

Reason:
- Tier 3 is the first level that yields real, replay-verifiable, non-advisory Model 9 value
- Tier 4 adds important strength, but Tier 3 is the first level that materially proves bounded active accompaniment instead of describing it

That means the first incorporation target should optimize for:
- one bounded segment
- one covered refusal-capable boundary
- one stable transition identity
- one stable authority/invariant basis
- one explicit downgrade model
- one replay-verifiable evidence chain
- one PQC-ready crypto posture that stays active where claim-relevant

---

## 15. Final Rule

The final rule is:

SPECTRE-SENTINEL should claim only Tier 3 bounded active segment accompaniment first, and only after it can prove that the exact claimed segment had:
- explicit scope
- bound identity
- bound authority
- bound invariant
- mechanically effective refusal
- timely refusal
- downgrade discipline
- replay-sufficient evidence
- claim-relevant crypto posture handling where applicable

That is the minimal honest architecture profile.

---

## 16. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_FIRST_INCORPORATION_TARGET.md

This file should be committed before moving to the next split artifact.