# MODEL 9 SENTINEL EVIDENCE SCHEMA

## Status

This file is a canonical split artifact derived from:
- docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md
- docs/MODEL_9_TIGHTENING_SPEC.md
- docs/MODEL_9_SENTINEL_STATE_MODEL.md

It defines the evidence schema required for SPECTRE-SENTINEL to support Model 9 in a strict, bounded, replay-verifiable way.

It is architecture-facing only.

It does not assume repository layout beyond this file.
It does not authorize implementation by itself.
It does not broaden BBIS.
It does not collapse BBIS into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL.

---

## 1. Purpose

This artifact defines the evidence schema required for SPECTRE-SENTINEL to support Model 9 in a strict, bounded, replay-verifiable way.

It defines:
- exact evidence categories required per state
- exact mandatory versus optional evidence
- exact downgrade evidence requirements
- exact replay input requirements
- exact final classification evidence requirements
- exact evidence needed to distinguish:
  - active accompaniment
  - segment accompaniment
  - advisory accompaniment
  - observed-only
  - uncovered
  - unverifiable
- exact evidence treatment for claim-relevant crypto posture where applicable

---

## 2. Governing Evidence Rule

No Model 9 classification may exceed what the surfaced evidence can independently support.

If required evidence is absent, ambiguous, contradicted, or not replay-sufficient, the classification must be downgraded.

---

## 3. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 4. Standing Architectural Requirement

PQC must be on and always at the ready.

For the evidence schema, this means:
- evidence must not be structured in a way that assumes a structurally legacy-only crypto posture
- where crypto posture is relevant to the claim, evidence must surface it explicitly
- replay must be able to inspect claim-relevant crypto posture where it affects classification validity
- unsupported or mismatched claim-relevant crypto posture must not be hidden behind generic evidence labels

This file does not require a full PQC migration program by itself.

It does require that claim-relevant crypto posture remain expressible in the evidence model where applicable.

---

## 5. Schema Design Constraints

The evidence schema must preserve these constraints:
- evidence must be explicit rather than inferred
- evidence must distinguish declaration from proof
- evidence must distinguish persistence from refusal capability
- evidence must distinguish bounded segment support from end-to-end support
- evidence must distinguish observed state from governed state
- evidence must be sufficient for offline replay of the claim
- absence of evidence must not be repaired by narrative or assumption
- claim-relevant crypto posture must not be omitted where classification depends on it

---

## 6. Evidence Categories

Every evidence item must belong to one of these categories.

### 6.1 Declaration Evidence

Evidence that records what was claimed.

Examples:
- declared segment scope
- declared covered boundaries
- declared irreversible primitive
- declared authority basis
- declared invariant basis

Declaration evidence is necessary, but never sufficient by itself for a strong classification.

### 6.2 Binding Evidence

Evidence that records what was actually bound.

Examples:
- governed transition identity binding
- accompaniment instance binding
- authority binding
- invariant binding

### 6.3 Coverage Evidence

Evidence that records what boundaries and paths were actually within accompanied scope.

Examples:
- explicit covered boundary set
- covered path association
- scope limits
- excluded path statement

### 6.4 Refusal Evidence

Evidence that records whether refusal existed and whether it was mechanically effective.

Examples:
- refusal path identity
- refusal-capability status
- refusal-path-to-boundary association
- refusal result

### 6.5 Timing Evidence

Evidence that records whether refusal was live in time relative to mutation completion.

Examples:
- refusal-ready-before-mutation indicator
- ordering proof
- timing qualification state

### 6.6 Continuity Evidence

Evidence that records whether identity, authority, invariant, and accompaniment continuity remained intact.

Examples:
- continuity confirmation
- continuity-preserving successor relation
- continuity-loss event

### 6.7 Alternate-Path Evidence

Evidence that records whether the governed mutation could escape through uncovered relevant paths.

Examples:
- alternate path closure proof
- alternate path exposure event
- scope-limited exclusion statement

### 6.8 Truth-Boundary Evidence

Evidence that records the basis for claiming that the named boundary is the actual mutation authority for the claimed scope.

Examples:
- mutation-authority assertion basis
- contradiction event
- scope correction event

### 6.9 Crypto Posture Evidence

Where crypto posture is relevant to the claim, evidence that records the relevant crypto posture and its qualification status.

Examples:
- crypto posture identity
- crypto qualification result
- crypto mismatch event
- crypto absence event
- crypto visibility-to-replay confirmation

### 6.10 Downgrade Evidence

Evidence that records why a stronger class no longer applies.

Examples:
- refusal failure event
- coverage loss event
- evidence insufficiency event
- authority drift event
- scope inflation detection event
- crypto posture failure event

### 6.11 Completion Evidence

Evidence that records the final outcome for the segment.

Examples:
- final classification
- final scope
- final downgrade chain
- evidence sufficiency result

---

## 7. Common Evidence Fields

Every evidence record, regardless of category, should carry these common fields.

### 7.1 Evidence Type
Identifies what kind of evidence record this is.

### 7.2 Segment Identifier
Identifies the accompanied segment to which the record applies.

### 7.3 Transition Identifier
Identifies the governed transition to which the record applies.

### 7.4 Accompaniment Instance Identifier
Identifies the accompaniment instance to which the record applies, where relevant.

### 7.5 Event or State Identifier
Identifies the state or event represented by the record.

### 7.6 Sequence or Ordering Marker
Provides replay ordering sufficient to determine claim progression and timing relations.

### 7.7 Scope Statement
States the exact scope to which the record applies.

### 7.8 Evidence Status
States whether the record is:
- asserted
- bound
- confirmed
- downgraded
- contradicted
- insufficient

### 7.9 Source Class
States whether the evidence arises from:
- declaration
- binding
- runtime enforcement surface
- continuity surface
- downgrade surface
- completion surface

### 7.10 Integrity Basis
States what basis allows the record to be trusted as evidence for replay.

This is a schema requirement, not a prescription of trust mechanism.

---

## 8. Mandatory Evidence by State

This section defines the minimum mandatory evidence required for each state.

### 8.1 Uninitialized

Mandatory:
- explicit absence of active accompanied segment claim

Optional:
- visibility-only context

Without this, replay cannot determine whether accompaniment had not started or evidence is simply missing.

### 8.2 Segment-Declared

Mandatory:
- segment identifier
- segment scope statement
- declared start condition
- declared end condition
- declared covered boundary set
- declared irreversible primitive
- declared authority basis
- declared invariant basis

Optional:
- declared exclusions
- declared alternate path assumptions
- declared crypto posture expectation where claim-relevant

This evidence supports declaration only, not accompaniment conformance.

### 8.3 Identity-Bound

Mandatory:
- governed transition identifier
- accompaniment instance identifier
- identity binding event
- continuity rule or successor rule if identity can transfer

Optional:
- identity-basis metadata

Without this, no accompanied classification above Observed-Only can survive.

### 8.4 Authority-Bound

Mandatory:
- authority basis identifier
- invariant basis identifier
- authority binding event
- invariant binding event
- governed succession rule if authority or invariant can change

Optional:
- authority scope limitations
- invariant scope limitations

Without this, governance continuity cannot be claimed.

### 8.5 Coverage-Established

Mandatory:
- explicit covered boundary set
- path-scope statement
- segment scope statement
- claimed irreversible primitive
- included-path statement or equivalent scope boundary

Optional:
- excluded path statement
- conditional scope statement

Without this, active accompaniment scope cannot be verified.

### 8.6 Refusal-Live

Mandatory:
- refusal path identifier
- refusal-path-to-covered-boundary association
- refusal-capability status
- refusal activation event

Optional:
- refusal mechanism characterization
- refusal dependency conditions

Without this, active accompaniment cannot be claimed.

### 8.7 Crypto-Qualified

Where crypto posture is claim-relevant, mandatory:
- claim-relevant crypto posture identifier
- crypto qualification event
- crypto qualification status
- replay-visible crypto posture record

Optional:
- crypto posture scope limitations
- crypto policy notes that are explicitly surfaced as evidence

Without this, a crypto-dependent stronger claim cannot survive.

### 8.8 Actively-Accompanying

Mandatory:
- active continuity confirmation
- current identity continuity confirmation
- current authority continuity confirmation
- current invariant continuity confirmation
- current refusal-live confirmation
- timing qualification evidence
- alternate-path status evidence
- no-known truth-boundary contradiction status
- current classification ceiling statement
- crypto qualification status where claim-relevant

Optional:
- narrower scope limitation statement
- continuity health metadata

This is the minimum state evidence required to justify a live strong classification.

### 8.9 Advisory-Only

Mandatory:
- persistent accompaniment presence evidence
- reason refusal does not qualify
- resulting classification ceiling statement

Optional:
- residual visibility evidence
- residual continuity evidence

Without the reason field, replay cannot distinguish advisory accompaniment from missing evidence.

### 8.10 Coverage-Lost

Mandatory:
- lost boundary or path identifier
- loss event ordering marker
- affected scope statement
- resulting downgraded classification ceiling

Optional:
- surviving narrower scope statement

Without this, replay cannot justify why stronger classification ended.

### 8.11 Crypto-Failed

Where crypto posture is claim-relevant, mandatory:
- crypto failure reason
- affected scope
- resulting downgraded classification ceiling

Optional:
- retained lower class rationale if any survives

### 8.12 Unverifiable

Mandatory:
- evidence insufficiency statement
- affected higher claim
- affected scope
- resulting downgraded classification ceiling

Optional:
- insufficiency subtype
- recovery possibility indicator

### 8.13 Failed-Closed

Mandatory:
- triggering failure event
- terminated stronger state or claim
- resulting lower classification ceiling or lower state
- affected scope

Optional:
- retained narrower valid scope statement

### 8.14 Completed

Mandatory:
- final classification
- final scope statement
- final evidence sufficiency determination
- downgrade chain
- final classification justification summary at evidence level

Optional:
- residual unresolved ambiguity statement

---

## 9. Mandatory Evidence by Classification

This section defines what evidence is mandatory to support each final classification.

### 9.1 Actively Accompanied

Mandatory:
- explicit segment declaration evidence
- identity binding evidence
- authority binding evidence
- invariant binding evidence
- explicit coverage evidence
- refusal-live evidence
- timing qualification evidence
- alternate-path status evidence
- truth-boundary support evidence
- continuity evidence across the claimed segment
- completion evidence with final class
- no unresolved evidence insufficiency for required elements
- crypto qualification evidence where claim-relevant

If any mandatory element is missing, this classification must not be issued.

### 9.2 Segment-Accompanied

Mandatory:
- all evidence needed for active accompaniment within the narrower segment
- explicit narrower segment scope statement
- explicit non-claim of broader end-to-end continuity, or equivalent scope-limiting evidence
- crypto qualification evidence where claim-relevant to that narrower claim

Without the narrower scope statement, this class risks scope inflation.

### 9.3 Advisory-Accompanied

Mandatory:
- segment declaration evidence or equivalent bounded scope evidence
- evidence of persistent accompaniment presence
- evidence showing refusal did not qualify as mechanically effective or timely
- completion evidence with final class

Without proof of persistent accompaniment presence, the class must drop lower.

### 9.4 Observed-Only

Mandatory:
- evidence of observation or visibility over the relevant segment or event
- absence of valid accompanied proof, or explicit lower ceiling

This class requires less evidence, but still requires positive support for observation.

### 9.5 Uncovered

Mandatory:
- evidence that no accompaniment claim applied, or no covered boundary scope existed for the segment

This class must not be used as a placeholder for unknown evidence status where a stronger claim was attempted.

### 9.6 Unverifiable

Mandatory:
- explicit evidence insufficiency record
- identification of the stronger claim that could not be supported
- affected scope
- resulting downgraded class

This class is required whenever proof failure, not true lack of accompaniment, is the reason a stronger class cannot stand.

---

## 10. Optional Evidence

Optional evidence may refine understanding, but may never substitute for mandatory evidence.

Examples of optional evidence:
- implementation notes
- environmental capability notes
- health metrics
- diagnostic commentary
- secondary observability records
- derived explanatory summaries

Optional evidence must never be used to fill mandatory gaps.

---

## 11. Downgrade Evidence Requirements

Every downgrade must be backed by explicit downgrade evidence.

### 11.1 Mandatory Downgrade Fields

Each downgrade record must include:
- prior claimed state or classification
- downgrade trigger type
- affected scope
- ordering marker
- resulting state or classification ceiling
- evidence basis for downgrade

### 11.2 Mandatory Downgrade Triggers Requiring Evidence

Evidence must exist for each of these when applicable:
- identity discontinuity
- authority drift
- invariant drift
- refusal failure
- timing failure
- coverage loss
- alternate path exposure
- truth-boundary contradiction
- evidence insufficiency
- scope inflation detection
- crypto posture failure where claim-relevant

### 11.3 Downgrade Sufficiency Rule

If a stronger class ended, replay must be able to see why it ended.

Silent degradation is non-conforming.

---

## 12. Replay Inputs

The evidence schema must support replay with explicit inputs.

Replay inputs must be sufficient to determine:
- what segment was claimed
- what classification was claimed
- what scope was claimed
- what transition identity was governed
- what accompaniment instance was used
- what authority basis was in force
- what invariant basis was in force
- what covered boundaries were claimed
- what irreversible primitive was claimed
- whether refusal was live
- whether refusal was timely
- whether continuity held
- whether alternate path closure held for the claimed scope, or whether broader paths were explicitly outside claim scope
- whether truth-boundary support existed
- whether downgrade occurred when required
- whether claim-relevant crypto posture existed and qualified where applicable
- what final class is actually supported

If the schema cannot supply these replay inputs, it cannot support strong Model 9 incorporation.

---

## 13. Final Classification Evidence Requirements

The final classification record must not be standalone.

It must be supported by prior evidence.

### 13.1 Mandatory Final Classification Fields

Every final classification record must include:
- segment identifier
- final classification
- final scope
- strongest supported classification ceiling
- evidence sufficiency result
- downgrade chain or explicit statement that none occurred
- claim-limitation statement where relevant
- crypto qualification result where claim-relevant

### 13.2 Final Classification Rule

The final class must equal the strongest class supported by the evidence chain.

No final class may be justified by declaration alone.

---

## 14. Evidence Distinction Rules

The schema must make these distinctions explicit.

### 14.1 Declared vs Bound
Declared authority, invariant, or scope is not the same as bound authority, invariant, or scope.

### 14.2 Bound vs Live
A bound refusal path is not the same as a live refusal path.

### 14.3 Live vs Timely
A live refusal path is not the same as a timely refusal path.

### 14.4 Present vs Effective
A present accompaniment process is not the same as a mechanically effective accompaniment process.

### 14.5 Covered vs Closed
A covered path is not the same as alternate-path closure for the broader scope.

### 14.6 Asserted Boundary vs True Mutation Authority
A named boundary is not the same as a proven true mutation authority.

### 14.7 Described Classification vs Evidence-Supported Classification
A recorded label is not the same as a replay-supported final class.

### 14.8 Crypto Present vs Crypto Qualifying
A surfaced crypto posture is not the same as a crypto posture that satisfies the claim-relevant classification requirement.

---

## 15. Evidence Needed to Distinguish Final Classes

### 15.1 Active Accompaniment vs Segment Accompaniment

To distinguish these, evidence must show whether the active claim covers the full claimed scope or only a narrower bounded segment.

Mandatory distinguisher:
- explicit scope sufficiency evidence

### 15.2 Segment Accompaniment vs Advisory Accompaniment

To distinguish these, evidence must show whether refusal was mechanically effective and timely.

Mandatory distinguisher:
- refusal qualification evidence

### 15.3 Advisory Accompaniment vs Observed-Only

To distinguish these, evidence must show whether a persistent accompaniment process existed.

Mandatory distinguisher:
- persistent accompaniment presence evidence

### 15.4 Observed-Only vs Uncovered

To distinguish these, evidence must show whether visibility existed for the relevant segment.

Mandatory distinguisher:
- visibility evidence

### 15.5 Any Stronger Class vs Unverifiable

To distinguish these, evidence must show whether the required proof chain exists.

Mandatory distinguisher:
- evidence sufficiency determination

### 15.6 Crypto-Satisfied vs Crypto-Defeated Stronger Claim

Where crypto posture is claim-relevant, evidence must show whether the relevant crypto posture actually qualifies the stronger claim.

Mandatory distinguisher:
- crypto qualification evidence

---

## 16. Evidence Failure Rules

The schema must support explicit handling of evidence failure.

### 16.1 Missing Mandatory Evidence

If mandatory evidence for a claimed class is missing, the class must be downgraded.

### 16.2 Ambiguous Evidence

If evidence exists but does not uniquely support the claimed class, the stronger class must not stand.

### 16.3 Contradictory Evidence

If contradictory evidence exists, replay must resolve to the strongest lower justified class or to Unverifiable.

### 16.4 Late Evidence Rule

Evidence appearing after the claimed state may only support the claim if the schema and ordering markers make that support valid.

Otherwise it must not retroactively repair the claim.

---

## 17. Minimal Evidence Chain for Strong Incorporation

For SPECTRE-SENTINEL to claim meaningful Model 9 support beyond concept, the minimal evidence chain must show:

1. segment declared
2. transition identity bound
3. authority and invariant bound
4. covered boundaries established
5. refusal live
6. timing qualified
7. continuity maintained across claimed scope
8. alternate-path status determined or broader paths explicitly excluded from claim scope
9. truth-boundary support determined
10. crypto posture determined where claim-relevant
11. final classification issued with evidence sufficiency result

If this chain cannot be produced, strong incorporation is not yet established.

---

## 18. Direct Incorporation Rule

SPECTRE-SENTINEL can only claim Model 9 support to the extent that its evidence schema can distinguish and prove:
- active accompaniment
- segment accompaniment
- advisory accompaniment
- observed-only
- uncovered
- unverifiable

without inference, collapse, or silent overclaim.

Where crypto posture is claim-relevant, the schema must also be able to distinguish:
- crypto-qualified stronger claim
- crypto-defeated stronger claim

---

## 19. Immediate Follow-On

The next canonical split file after this one is:

- docs/MODEL_9_SENTINEL_REPLAY_RULES.md

This file should be committed before moving to the next split artifact.