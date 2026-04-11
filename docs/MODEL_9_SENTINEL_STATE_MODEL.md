# MODEL 9 SENTINEL STATE MODEL

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_TIGHTENING_SPEC.md
- docs/MODEL_9_CONFORMANCE_AND_CLASSIFICATION_RULES.md

It defines the state model required for incorporating Model 9 into SPECTRE-SENTINEL in a strict, bounded, fail-closed way.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the state model required for incorporating Model 9 into SPECTRE-SENTINEL in a strict, bounded, fail-closed way.

It defines:
- required accompaniment states
- required transition events
- required downgrade events
- required evidence emissions per state
- required fail-closed transitions
- exact mapping between state loss and classification loss
- claim-relevant crypto posture handling where applicable

---

## 2. Governing State Rule

The state model must preserve this rule:

SPECTRE-SENTINEL may claim Model 9 support only for the strongest state-backed classification that can be proven from:
- explicit coverage
- live refusal capability
- continuity of identity, authority, and invariant
- correct mutation-boundary identification
- replay-sufficient evidence
- claim-relevant crypto posture satisfaction where applicable

The state model exists to prevent descriptive continuity from being mislabeled as enforced continuity.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For the state model, this means:
- no state model may assume a structurally legacy-only crypto posture
- where crypto posture is relevant to the claim, the state model must be able to represent crypto qualification and crypto failure
- unsupported or mismatched claim-relevant crypto posture must cause fail-closed transition or downgrade
- replay must not be unable to see crypto posture if it affects classification validity

This file does not require a full PQC migration program by itself.

It does require that claim-relevant crypto posture remain part of the bounded state model where applicable.

---

## 5. State Model Scope

This state model applies only to a claimed accompanied segment.

It does not automatically apply to an entire workflow or end-to-end system.

Each segment must be modeled separately unless a broader scope is explicitly claimed and all conditions are satisfied for that broader scope.

---

## 6. Core State Objects

The state model assumes the existence of these conceptual objects only.

### 6.1 Governed Transition
The transition whose accompanied status is being tracked.

### 6.2 Accompaniment Instance
The logical governance process claiming accompaniment for the segment.

### 6.3 Authority Basis
The governing authority bound to the accompanied segment.

### 6.4 Invariant Basis
The governing invariant bound to the accompanied segment.

### 6.5 Covered Boundary Set
The explicit set of mutation-capable boundaries claimed as covered for the segment.

### 6.6 Claimed Irreversible Primitive
The boundary or mechanism claimed as the mutation authority for the segment.

### 6.7 Claim-Relevant Crypto Posture
The crypto posture that is relevant to evaluating the accompanied claim where applicable.

These are conceptual requirements for state tracking.

They are not implementation prescriptions.

---

## 7. Required Sentinel States

Each accompanied segment must be in exactly one primary state at a time.

### 7.1 Uninitialized

Meaning:
- no valid accompaniment segment has been established yet
- no coverage claim is active
- no stronger classification is available

This is the default starting state.

Required properties:
- no active segment claim
- no active accompaniment claim
- no coverage continuity claim

### 7.2 Segment-Declared

Meaning:
- a segment claim has been declared
- intended coverage scope has been identified
- active accompaniment is not yet established

This is a declaration state only.

It does not justify any accompanied classification above descriptive intent.

Required properties:
- segment start candidate identified
- segment end candidate identified
- covered boundary set declared
- claimed irreversible primitive declared
- authority basis declared
- invariant basis declared
- claim scope declared

Not yet proven:
- identity continuity
- refusal effectiveness
- timing sufficiency
- alternate path closure
- replay sufficiency
- crypto qualification where claim-relevant

### 7.3 Identity-Bound

Meaning:
- the accompaniment instance is now bound to a stable governed transition identity for the claimed segment

This state establishes transition identity continuity as a live requirement.

Required properties:
- governed transition identity bound
- accompaniment instance identity bound
- successor rules, if any, are explicit

Not yet proven:
- authority continuity
- invariant continuity
- refusal effectiveness
- covered-boundary continuity

### 7.4 Authority-Bound

Meaning:
- the accompaniment instance is bound to the governing authority basis and invariant basis for the claimed segment

This state establishes governance-basis continuity as a live requirement.

Required properties:
- authority basis bound
- invariant basis bound
- any governed succession rule explicit

Not yet proven:
- refusal effectiveness
- coverage continuity
- timing sufficiency

### 7.5 Coverage-Established

Meaning:
- the claimed covered boundaries for the segment have been explicitly established as the intended accompaniment scope

This is a scope-establishment state, not yet full active accompaniment.

Required properties:
- covered boundary set explicit
- segment bounds explicit
- claimed irreversible primitive explicit
- required mutation path set explicit, to the extent claimed

Not yet proven:
- live refusal at each covered boundary
- alternate path closure
- true mutation-boundary correctness

### 7.6 Refusal-Live

Meaning:
- the system has established that refusal is mechanically available for the covered boundaries presently in scope

This is the first state that begins to approach active accompaniment, but it is not enough alone.

Required properties:
- refusal path identified
- refusal path mechanically connected to covered mutation path
- refusal path status live

Not yet proven:
- refusal timing sufficiency
- alternate path closure
- truth-boundary correctness
- continuity through segment completion

### 7.7 Crypto-Qualified

Meaning:
- where crypto posture is relevant to the claim, the system has established that the relevant crypto posture is surfaced, bound where required, and currently compatible with the accompanied claim

This state is required only where crypto posture is claim-relevant.

Required properties:
- claim-relevant crypto posture identified
- crypto posture visible to evidence and replay
- crypto posture qualification result explicit

Not yet proven:
- continuity through segment completion unless maintained later
- active accompaniment unless all other required conditions also hold

### 7.8 Actively-Accompanying

Meaning:
- active accompaniment is presently live for the claimed segment scope as currently proven

This is the strongest live state.

It requires all currently relevant conditions to hold at once.

Required properties:
- segment declared
- identity bound
- authority bound
- invariant bound
- coverage established
- refusal live
- refusal timely
- no relevant uncovered alternate path for claimed scope, or claim scope explicitly excludes such paths
- no current truth-boundary contradiction
- evidence emission active
- crypto qualified where claim-relevant

This is the state that can support Actively Accompanied or Segment-Accompanied, depending on scope.

### 7.9 Advisory-Only

Meaning:
- a persistent accompaniment process remains present, but refusal no longer qualifies as mechanically effective or timely

This is not active accompaniment.

Required properties:
- accompaniment presence still evidenced
- reason for advisory-only downgrade explicit

This state supports Advisory-Accompanied only.

### 7.10 Coverage-Lost

Meaning:
- accompaniment continuity no longer covers one or more required boundaries for the claimed scope

This state means the stronger accompanied claim has failed for the affected scope.

Required properties:
- point of coverage loss explicit
- affected boundary or path explicit
- affected scope explicit

This state forces downgrade.

### 7.11 Crypto-Failed

Meaning:
- where crypto posture is claim-relevant, the required crypto posture no longer qualifies, is unsupported, is mismatched, or is no longer visible to replay

Required properties:
- crypto failure reason explicit
- affected scope explicit
- resulting classification ceiling explicit

This state forces downgrade or fail-closed handling.

### 7.12 Unverifiable

Meaning:
- the state model can no longer support independent verification of the stronger accompaniment claim

This is an evidence-failure state.

Required properties:
- missing or insufficient evidence condition explicit
- affected claim scope explicit

This state supports Unverifiable only.

### 7.13 Completed

Meaning:
- the accompanied segment has ended and final classification can be issued for the claimed scope

This is a terminal evaluation state, not automatically a success state.

Required properties:
- segment end explicit
- final classification explicit
- downgrade history explicit
- final evidence sufficiency status explicit

### 7.14 Failed-Closed

Meaning:
- the state model encountered a condition under which stronger accompaniment claims could no longer continue and the system terminated or downgraded them without silent continuation

This is the mandatory safety state for strict incorporation.

Required properties:
- failure condition explicit
- stronger claim termination explicit
- resulting downgraded classification explicit

---

## 8. Allowed State Transitions

Only the following transition structure is valid.

### 8.1 Nominal Path without claim-relevant crypto qualification

- Uninitialized
- Segment-Declared
- Identity-Bound
- Authority-Bound
- Coverage-Established
- Refusal-Live
- Actively-Accompanying
- Completed

This path is valid only where crypto posture is not claim-relevant.

### 8.2 Nominal Path with claim-relevant crypto qualification

- Uninitialized
- Segment-Declared
- Identity-Bound
- Authority-Bound
- Coverage-Established
- Refusal-Live
- Crypto-Qualified
- Actively-Accompanying
- Completed

This path is required where crypto posture is claim-relevant.

### 8.3 Advisory Path

- Uninitialized
- Segment-Declared
- Identity-Bound
- Authority-Bound
- Coverage-Established
- Advisory-Only
- Completed

or

- Actively-Accompanying
- Advisory-Only
- Completed

### 8.4 Coverage Failure Path

- Coverage-Established
- Coverage-Lost
- Failed-Closed
- Completed

or

- Actively-Accompanying
- Coverage-Lost
- Failed-Closed
- Completed

### 8.5 Crypto Failure Path

Where crypto posture is claim-relevant:

- Crypto-Qualified
- Crypto-Failed
- Failed-Closed
- Completed

or

- Actively-Accompanying
- Crypto-Failed
- Failed-Closed
- Completed

### 8.6 Evidence Failure Path

Any state that depends on proof may transition to:
- Unverifiable
- Failed-Closed
- Completed

### 8.7 Direct Fail-Closed Rule

If a required higher state cannot be established, the system must not silently skip forward.

It must either:
- remain in the strongest justified lower state, or
- move to Failed-Closed, Unverifiable, Coverage-Lost, or Crypto-Failed as appropriate

---

## 9. Required Transition Events

Each state transition must be caused by an explicit event.

### 9.1 Segment Declaration Event

Creates the accompanied segment claim.

Required emission:
- segment identifier
- declared scope
- declared boundaries
- declared irreversible primitive
- declared authority basis
- declared invariant basis

### 9.2 Identity Binding Event

Binds accompaniment instance to governed transition identity.

Required emission:
- governed transition identity
- accompaniment instance identity
- continuity rule or successor relation if relevant

### 9.3 Authority Binding Event

Binds accompaniment instance to authority basis and invariant basis.

Required emission:
- authority basis identity
- invariant basis identity
- any succession rule if relevant

### 9.4 Coverage Establishment Event

Establishes claimed covered boundaries and claimed scope.

Required emission:
- covered boundary set
- claimed segment start
- claimed segment end
- claimed irreversible primitive
- scope statement

### 9.5 Refusal Activation Event

Establishes that refusal is live for the relevant covered boundaries.

Required emission:
- refusal path identity
- refusal-capability status
- covered boundary association

### 9.6 Crypto Qualification Event

Where crypto posture is claim-relevant, establishes that relevant crypto posture is visible and currently compatible with the claim.

Required emission:
- claim-relevant crypto posture identity
- qualification status
- affected scope
- fail-closed consequence if qualification fails later

### 9.7 Active Continuity Event

Confirms that active accompaniment is presently live.

Required emission:
- current state confirmation
- continuity status
- timing-qualification status
- alternate-path status for claimed scope

### 9.8 Downgrade Event

Occurs when a higher state is no longer justified.

Required emission:
- prior state
- downgrade reason
- resulting state
- affected scope

### 9.9 Coverage Loss Event

Occurs when required coverage ceases.

Required emission:
- lost boundary or path
- scope affected
- resulting classification ceiling

### 9.10 Crypto Failure Event

Occurs when claim-relevant crypto posture becomes unsupported, mismatched, absent, contradicted, or hidden.

Required emission:
- crypto failure reason
- affected scope
- resulting classification ceiling

### 9.11 Evidence Failure Event

Occurs when state proof becomes insufficient.

Required emission:
- missing or insufficient evidence description
- affected state claim
- resulting classification ceiling

### 9.12 Completion Event

Ends the accompanied segment and issues final classification.

Required emission:
- final state
- final classification
- final scope
- downgrade history
- evidence sufficiency result

---

## 10. Required Downgrade Events

These are mandatory events, not optional annotations.

### 10.1 Identity Loss Event

Triggered when stable governed transition identity can no longer be proven.

Result:
- exit Actively-Accompanying or higher-preparatory state
- move to Failed-Closed or Unverifiable depending on proof state

### 10.2 Authority Drift Event

Triggered when authority continuity is broken, changed without governed handling, or becomes unprovable.

Result:
- stronger state ends immediately
- downgrade required

### 10.3 Invariant Drift Event

Triggered when invariant continuity is broken or unprovable.

Result:
- stronger state ends immediately
- downgrade required

### 10.4 Refusal Failure Event

Triggered when refusal is no longer mechanically effective.

Result:
- downgrade to Advisory-Only at best, or lower if even that cannot be proven

### 10.5 Timing Failure Event

Triggered when refusal exists but can no longer act before mutation completion.

Result:
- downgrade to Advisory-Only at best

### 10.6 Coverage Loss Event

Triggered when any required covered boundary for the claimed scope is no longer covered.

Result:
- downgrade to Segment-Accompanied for narrower surviving scope if justified
- otherwise Failed-Closed or Uncovered

### 10.7 Alternate Path Exposure Event

Triggered when mutation can occur through an uncovered relevant path for claimed scope.

Result:
- broader active claim ends immediately
- narrower scope may survive only if explicitly separable

### 10.8 Truth-Boundary Contradiction Event

Triggered when claimed irreversible primitive or claimed covered boundary is shown not to be the actual mutation authority.

Result:
- stronger claim fails
- downgrade required
- prior classification must not survive by inertia

### 10.9 Crypto Failure Event

Triggered when claim-relevant crypto posture becomes unsupported, mismatched, absent, contradicted, or hidden from replay.

Result:
- stronger claim ends immediately
- downgrade or fail-closed handling required

### 10.10 Evidence Insufficiency Event

Triggered when evidence needed for independent replay is missing, ambiguous, corrupted, or no longer sufficient.

Result:
- move to Unverifiable at best

### 10.11 Scope Inflation Detection Event

Triggered when a bounded accompanied fact is presented as a broader accompanied claim without proof.

Result:
- broader claim invalid
- retained classification limited to strongest justified narrower scope only

---

## 11. Required Evidence Emissions Per State

Each state requires its own minimum evidence emission.

### 11.1 Uninitialized

Minimum:
- no active claim marker

### 11.2 Segment-Declared

Minimum:
- segment identifier
- declared boundaries
- declared start
- declared end
- declared irreversible primitive
- declared authority basis
- declared invariant basis
- declared scope

### 11.3 Identity-Bound

Minimum:
- governed transition identity
- accompaniment instance identity
- binding event record

### 11.4 Authority-Bound

Minimum:
- authority basis identity
- invariant basis identity
- binding continuity record

### 11.5 Coverage-Established

Minimum:
- explicit covered boundary set
- claimed scope statement
- claimed irreversible primitive
- path-scope statement

### 11.6 Refusal-Live

Minimum:
- refusal path identity
- refusal-capability status
- covered-boundary linkage

### 11.7 Crypto-Qualified

Where crypto posture is claim-relevant, minimum:
- crypto posture identity
- qualification status
- claim-relevance statement
- affected scope

### 11.8 Actively-Accompanying

Minimum:
- continuity confirmation
- refusal live status
- timing qualification
- alternate-path status
- no known truth-boundary contradiction for claimed scope
- current classification ceiling
- crypto qualification status where claim-relevant

### 11.9 Advisory-Only

Minimum:
- accompaniment presence evidence
- reason refusal does not qualify
- resulting classification ceiling

### 11.10 Coverage-Lost

Minimum:
- lost boundary or path
- loss ordering marker
- affected claim scope
- resulting downgrade ceiling

### 11.11 Crypto-Failed

Minimum:
- crypto failure reason
- affected scope
- resulting downgraded ceiling

### 11.12 Unverifiable

Minimum:
- evidence insufficiency statement
- affected higher claim
- resulting downgraded ceiling

### 11.13 Completed

Minimum:
- final classification
- final scope
- full downgrade chain
- final evidence sufficiency determination

### 11.14 Failed-Closed

Minimum:
- triggering failure event
- terminated stronger claim
- resulting lower state or classification ceiling

---

## 12. Required Fail-Closed Transitions

The state model must fail closed under these conditions.

### 12.1 Missing Binding Rule

If identity binding, authority binding, or invariant binding cannot be established, the model must not enter Actively-Accompanying.

### 12.2 Missing Refusal Rule

If refusal is not proven mechanically effective, the model must not enter Actively-Accompanying.

### 12.3 Missing Timing Rule

If timing sufficiency is not proven, the model must not enter Actively-Accompanying.

### 12.4 Missing Coverage Rule

If required covered boundaries are not explicit, the model must not enter Actively-Accompanying.

### 12.5 Alternate Path Rule

If relevant alternate path closure is not proven for the claimed scope and the path is not explicitly outside claim scope, the model must not maintain a broader accompanied claim.

### 12.6 Truth-Boundary Rule

If the claimed mutation authority is contradicted or ungrounded, the stronger state must end.

### 12.7 Crypto Qualification Rule

Where crypto posture is claim-relevant, if crypto qualification is not proven, the model must not enter or maintain Actively-Accompanying.

### 12.8 Evidence Rule

If replay-sufficient evidence is absent, the model must not preserve a stronger classification.

---

## 13. Mapping Between State Loss and Classification Loss

This section is the heart of the model.

### 13.1 If Segment-Declared is lost

Classification impact:
- no accompanied classification survives
- result becomes Uncovered or Observed-Only depending on visibility

### 13.2 If Identity-Bound is lost

Classification impact:
- Actively Accompanied cannot survive
- Segment-Accompanied cannot survive
- result becomes Unverifiable or lower

### 13.3 If Authority-Bound is lost

Classification impact:
- governance continuity cannot survive
- result becomes Unverifiable or lower

### 13.4 If Coverage-Established is lost

Classification impact:
- broader accompanied claim cannot survive
- narrower scope may survive only if separately established
- otherwise Uncovered or Failed-Closed

### 13.5 If Refusal-Live is lost

Classification impact:
- Actively Accompanied cannot survive
- highest remaining class is Advisory-Accompanied at best

### 13.6 If Crypto-Qualified is lost where claim-relevant

Classification impact:
- the stronger claim cannot survive
- result becomes Unverifiable, Segment-Accompanied, or lower only if remaining evidence still supports a lower class without that stronger crypto-dependent claim
- otherwise Failed-Closed

### 13.7 If Actively-Accompanying is lost through timing failure

Classification impact:
- downgrade to Advisory-Accompanied at best

### 13.8 If Actively-Accompanying is lost through alternate path exposure

Classification impact:
- broader accompanied claim fails immediately
- narrower bounded claim may survive only if explicitly separable and still covered

### 13.9 If Actively-Accompanying is lost through truth-boundary contradiction

Classification impact:
- stronger classification fails
- any surviving lower class must not imply governance at the real mutation authority

### 13.10 If evidence for any higher state becomes insufficient

Classification impact:
- downgrade to Unverifiable at best for that higher claim

### 13.11 If Completed is reached without sufficient evidence

Classification impact:
- final classification must reflect strongest replay-supported lower class only

---

## 14. Classification Ceilings by State

Each state imposes a maximum possible classification.

| State | Maximum Classification |
|---|---|
| Uninitialized | Uncovered |
| Segment-Declared | Uncovered or Observed-Only |
| Identity-Bound | Observed-Only |
| Authority-Bound | Observed-Only |
| Coverage-Established | Segment-Accompanied at most, only if other requirements are later satisfied |
| Refusal-Live | Segment-Accompanied at most, unless full active conditions are proven |
| Crypto-Qualified | Segment-Accompanied at most, unless all active conditions are proven |
| Actively-Accompanying | Actively Accompanied or Segment-Accompanied depending on scope |
| Advisory-Only | Advisory-Accompanied |
| Coverage-Lost | Segment-Accompanied for narrower surviving scope at most; otherwise Uncovered |
| Crypto-Failed | strongest justified downgraded class only |
| Unverifiable | Unverifiable |
| Failed-Closed | strongest justified downgraded class only |
| Completed | strongest replay-supported final class only |

---

## 15. Non-Claim Boundary for Sentinel

SPECTRE-SENTINEL must not claim Model 9 incorporation merely because it can:
- spawn a monitor
- attach a sidecar
- run in a TEE
- emit alerts
- log events
- carry policy identity
- observe a transition over time
- surface crypto posture without making it classification-relevant where claim-relevant

Those are insufficient by themselves.

The minimum honest claim is only what the state model can actually support through:
- explicit accompanied segment state
- refusal-live state
- active continuity state
- downgrade events
- replay-sufficient evidence
- crypto qualification where claim-relevant

---

## 16. Direct Incorporation Rule

SPECTRE-SENTINEL can be said to support Model 9 only to the degree that it can represent and verify:
- segment declaration
- identity binding
- authority binding
- invariant binding
- coverage establishment
- refusal-live status
- crypto-qualified status where claim-relevant
- active accompaniment status
- downgrade on loss
- fail-closed termination of stronger claims
- final replay-supported classification

Nothing broader should be claimed.

---

## 17. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_EVIDENCE_SCHEMA.md

This file should be committed before moving to the next split artifact.