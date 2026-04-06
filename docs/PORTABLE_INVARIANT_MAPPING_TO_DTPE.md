---

## File 2 — `docs/PORTABLE_INVARIANT_MAPPING_TO_DTPE.md`

```md id="portable-invariant-mapping-dtpe-doc"
# Portable Invariant Mapping to DTPE

## Purpose

This section maps the portable boundary invariant model into DTPE / IAL / SPECTRE.

The goal is to show how DTPE’s existing architecture already aligns with the core invariant logic, and how the portable invariant extends DTPE from single-boundary enforcement into boundary-to-boundary continuity.

## Core mapping

The portable invariant model says that a governed transition is valid only if the same governing condition survives each mutation-capable boundary as a live refusal condition and still holds at the true irreversible primitive.

DTPE already strongly supports this direction.

DTPE’s core invariant:

> verify without trusting the runtime that generated it

becomes stronger when paired with a continuity claim:

> a transition remains valid only if the governing basis survives each mutation-capable boundary without widening and is re-derived under live state at the true irreversible primitive

## Why this fits DTPE

DTPE already contains the architectural components most of this model requires:

- canonical transition handling
- authority validation
- state admissibility evaluation
- system stability evaluation
- temporal invariant enforcement
- canonical receipts
- append-only ledger evidence
- offline replay verification
- refusal semantics at the execution boundary

What the portable invariant adds is not a replacement for those pieces.
It adds a continuity model for carrying the same governing basis across multiple mutation-capable boundaries.

## Mapping the portable invariant components into DTPE

### 1. Canonical transition identity

Portable invariant model:
- the exact governed transition must survive boundary-to-boundary in canonical form

DTPE mapping:
- canonical transition identity maps naturally to DTPE’s canonical execution inputs and execution intent
- DTPE already rejects hidden runtime context and requires deterministic inputs
- this means DTPE is already structurally aligned with canonical transition identity as a first-class object

Implication:
- DTPE should treat the governed transition not merely as an input to a single decision, but as a carried canonical identity that must remain stable or narrow across boundaries

### 2. Authorization basis

Portable invariant model:
- the authorization basis must survive each boundary without widening

DTPE mapping:
- authority snapshots
- authority hash
- identity/accountability binding
- authority validity checks

Implication:
- DTPE already has a strong authority basis
- the portable invariant model extends this by requiring that authority remain a live carried condition, not just a fact checked once and recorded historically

### 3. Admissibility basis

Portable invariant model:
- the admissibility predicate must be re-derived against live state at each mutation-capable boundary

DTPE mapping:
- canonical current state
- canonical transition
- policy state hash
- authority hash
- execution intent
- crypto profile
- temporal invariant result

Phase fit:
- Phase 5 maps directly to state admissibility
- Phase 6 maps directly to temporal validity
- future session invalidation work would map to later invalidation conditions

Implication:
- DTPE already treats admissibility as a deterministic function of canonical inputs
- the portable invariant model requires that this admissibility basis remain governing wherever mutation-capable progress occurs

### 4. Invalidation rules

Portable invariant model:
- replay
- supersession
- authority change
- policy change
- session invalidation
- state mismatch
- expiration
- resource-state change

DTPE mapping:
- refusal semantics already exist when authority, state admissibility, stability, or temporal validity fail
- DTPE naturally supports treating these as invalidation conditions within the carried invariant
- later session invalidation work would extend this more fully

Implication:
- DTPE can treat invalidation not only as local recomputation logic but as part of the portable governing package carried across boundaries

### 5. Native refusal

Portable invariant model:
- every mutation-capable boundary must refuse if the invariant no longer holds
- logging without refusal is insufficient

DTPE mapping:
- SPECTRE’s execution-boundary model already aligns with this requirement
- `ALLOW` only if the governing predicate holds
- otherwise `REFUSED_NON_BINDING`

Implication:
- DTPE already contains the right refusal semantics
- the portable invariant model extends them to chained mutation-capable boundaries rather than a single abstract boundary alone

### 6. Final-boundary enforcement

Portable invariant model:
- the decisive test is whether the same invariant still holds at the true irreversible primitive

DTPE mapping:
- this aligns directly with mutation authority and boundary integrity
- DTPE’s strongest architectural requirement is that the governing predicate must still control whether the side effect becomes real

Implication:
- DTPE becomes more complete when the final irreversible primitive is explicitly required to honor the same carried invariant as a live refusal condition

## Mapping to DTPE’s six-part frame

### Authorization integrity

Portable invariant meaning:
- canonical authorization basis survives each boundary without widening

DTPE meaning:
- authority snapshots and authority hashes remain governing, not merely historical

### Execution evidence

Portable invariant meaning:
- each boundary emits evidence showing preservation, narrowing, refusal, or failure of the invariant

DTPE meaning:
- canonical receipt + ledger + offline verification remain essential
- but a stronger DTPE continuity model would also preserve boundary-by-boundary evidence where needed

### Mutation authority

Portable invariant meaning:
- each mutation-capable boundary must refuse locally if the invariant no longer holds
- the final decisive authority remains the true irreversible primitive

DTPE meaning:
- mutation authority is the component that can still refuse before the side effect becomes real
- the portable invariant clarifies how this condition should survive across multiple boundaries

### Boundary integrity

Portable invariant meaning:
- the same governing condition survives transit and is re-derived without weakening

DTPE meaning:
- no stale admissibility should survive to mutation
- validation-to-mutation continuity becomes stronger when the same invariant is carried and re-derived across boundaries

### Session invalidation

Portable invariant meaning:
- prior events can revoke, narrow, supersede, or invalidate the carried invariant

DTPE meaning:
- this is the natural extension path for future DTPE work
- once session invalidation is made explicit, it becomes part of the carried live validity of the transition

### Enforceability class

Portable invariant meaning:
- honest disclosure of whether the invariant truly survives every meaningful boundary

DTPE meaning:
- strong if the invariant survives every relevant boundary and is enforced at the true irreversible primitive
- bounded if some boundaries preserve it but final closure still depends on weaker assumptions
- detectable-only if the invariant is mostly reconstructed or attested after the fact

## What the portable invariant adds to DTPE

### 1. Boundary-to-boundary continuity

DTPE already defines a strong execution boundary.
The portable invariant extends that model by asking how the same governing basis survives chained boundaries rather than a single decision point alone.

### 2. Distributed DTPE applicability

If DTPE governs:
- proxies
- delegated services
- downstream tools
- external systems
- payment rails
- multi-stage execution paths

then the portable invariant provides a cleaner answer to:

- what is carried forward
- what must be re-derived
- what invalidates downstream execution
- what must still refuse locally

### 3. Stronger distinction between evidence and governance

Portable invariant framing makes one DTPE distinction explicit:

- receipt = evidence of what was decided and what occurred
- portable invariant = carried live refusal condition that determines whether the transition may still become real

This distinction is already implicit in DTPE.
The portable invariant makes it architectural.

## Candidate DTPE-shaped invariant contents

A DTPE-compatible portable invariant would naturally bind things like:

- `transition_hash`
- `authority_hash`
- `policy_state_hash`
- `admissibility_digest` or canonical state basis
- `execution_intent`
- `crypto_profile`
- `execution_time` or temporal validity basis
- replay-prevention material
- invalidation generation / epoch
- refusal semantics binding

This list is illustrative, not a claim that all such fields are already fully implemented in DTPE today.

## Stress tests for DTPE continuity

A DTPE portable invariant claim should survive at least these tests:

1. authority valid at initial check, invalid at downstream boundary
2. state admissible at initial check, stale at commit boundary
3. payload altered after authorization
4. replay of a once-valid transition artifact
5. delayed execution after temporal validity changed
6. downstream path bypassing the original boundary assumption
7. queue/retry logic after invalidation
8. multi-step or multi-agent composition where no single local action captures the full irreversible result
9. degraded-mode / unavailable-boundary conditions
10. final mutation surface no longer enforcing the same invariant

If a transition can still proceed under those conditions, then DTPE has evidence continuity without full boundary continuity.

## Architectural implication

The portable invariant maps to DTPE as:

- a carried canonical transition + authority + admissibility + invalidation package
- re-derived at each mutation-capable boundary
- narrowed but never widened
- evidenced at each hop where required
- and still enforced at the true irreversible primitive as a live refusal condition

That is a natural extension of DTPE from deterministic boundary decision into deterministic boundary continuity.

## Open hard problem

The hardest remaining frontier is still compositional:

how to preserve the invariant when the true irreversible effect is not one local mutation, but an emergent composition across multiple agents, services, or systems.

This does not invalidate the DTPE mapping.
It defines the hardest future pressure surface for making boundary continuity complete.
