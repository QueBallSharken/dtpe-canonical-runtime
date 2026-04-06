# DTPE Governance Kernel Positioning

## Summary

DTPE is evolving from a provenance and verification runtime into a deterministic governance kernel for automated and autonomous systems.

Earlier phases focused on proving that automated decisions were authorized and reproducible.

Later phases expand the execution boundary so that the system evaluates whether state transitions are permitted before mutation is allowed.

## Core invariant

verify without trusting the runtime that generated it

A binding governance decision is valid only if an independent verifier can reconstruct the canonical inputs, replay the boundary evaluation, and confirm the recorded outcome without relying on hidden runtime state.

## Phase stack

The DTPE architecture evolves through a layered governance model.

- Phase 1: identity integrity
- Phase 2: authority and signature verification
- Phase 3: ledger evidence and offline verification
- later phases: expanded mutation-boundary governance, continuity constraints, and stronger bounded execution semantics

## Execution-boundary evaluation

At the governance boundary, the runtime evaluates multiple constraints:

- authority validity
- state admissibility
- system stability
- temporal invariants
- continuity-oriented invariants where the bounded runtime surface requires them

Execution decision:

ALLOW only if all governing constraints evaluate true.

Otherwise:

`REFUSED_NON_BINDING`

## Mutation authority and boundary integrity

DTPE's governance claim does not end at proving that a decision was evaluated or recorded.

The stronger question is whether the component that actually controls the irreversible primitive can still refuse under authoritative live conditions when the moment of mutation arrives.

This is why DTPE distinguishes:

- authorization integrity
- execution evidence
- mutation authority
- boundary integrity

These are not interchangeable.

A system can validate authority, record a receipt, and replay a decision afterward, yet still fail governance if stale or invalid admissibility can survive to the mutation point.

For the integrated mutation-boundary governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Portable continuity direction

DTPE's portable-invariant / boundary-to-boundary continuity direction extends the existing execution-boundary model.

It does not replace authority validity, state admissibility, temporal validity, receipts, ledger evidence, or offline replay.

It strengthens the governance claim by requiring the governing basis to survive mutation-capable boundaries as a live refusal condition rather than treating prior authorization or later evidence as sufficient by itself.

For the continuity model, see:

- `PORTABLE_BOUNDARY_INVARIANT.md`
- `PORTABLE_INVARIANT_MAPPING_TO_DTPE.md`

## Authority re-derivation model

Traditional distributed systems allow authority to propagate through delegation chains.

Authority persists while scope narrows.

This creates windows where authority may continue executing after the conditions that justified it have changed.

DTPE uses a different model.

Authority does not propagate as a permanently trusted runtime fact.

Authority must be re-derived at execution boundaries under canonical governing inputs.

## Authority collapse

Authority collapse prevents persistent authority inheritance.

At each execution boundary:

- authority collapses
- the system attempts recomputation
- recomputation uses canonical identity and policy state
- execution continues only if recomputation succeeds

If recomputation fails:

- execution stops

Authority cannot persist across boundaries as a binding fact without renewed validity.

## Validation-actuation risk

In many architectures a gap exists between validation and execution.

If system conditions change during this gap, authority may become invalid.

DTPE therefore treats admissibility as a gate on whether a transition may become real, not merely as a descriptive property of a recorded action.

## Governance kernel definition

A governance kernel is the smallest deterministic runtime component that evaluates whether system state transitions are permitted under defined policy constraints.

DTPE enforces this evaluation at the execution boundary and produces canonical receipts that allow independent verification without trusting the runtime.

## Enforceability posture

DTPE should distinguish honestly between mutation paths that are:

- strong
- bounded
- detectable-only

This prevents false equivalence between architectures that can fail closed at the true mutation boundary and architectures that can only explain or detect afterward.

## PQC / crypto-agility posture

Portable-invariant / boundary-to-boundary continuity must remain crypto-profile explicit, policy-governed, and replay-reconstructable across profile transitions.

Nothing in this positioning authorizes:

- implicit cryptographic behavior
- silent profile substitution
- hard-coded permanent algorithm assumptions
- weakening replayability across profile transitions

This positioning must remain compatible with post-quantum readiness.

## Architectural implication

The system no longer only records decisions.

It governs whether system evolution is permitted.

All future phases must preserve the core invariant:

verify without trusting the runtime that generated it
