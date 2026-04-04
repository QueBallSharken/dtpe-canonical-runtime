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
- Phase 4: execution boundary authorization
- Phase 5: state admissibility evaluation
- Phase 6: temporal invariant enforcement
- Phase 7: full governance kernel behavior

Each phase strengthens the execution boundary and increases the system's ability to prevent invalid state transitions.

## Execution-boundary evaluation

At the governance boundary, the runtime evaluates multiple constraints:

- authority validity
- state admissibility
- system stability
- temporal invariants

Execution decision:

ALLOW only if all constraints evaluate true.

Otherwise:

`REFUSED_NON_BINDING`

## Mutation authority and boundary integrity

DTPE's governance claim does not end at proving that a decision was evaluated or recorded.

The stronger question is whether the component that actually controls the irreversible primitive can still refuse under authoritative live conditions when the moment of mutation arrives.

This is why DTPE now distinguishes:

- authorization integrity
- execution evidence
- mutation authority
- boundary integrity

These are not interchangeable.

A system can validate authority, record a receipt, and replay a decision afterward, yet still fail governance if stale or invalid admissibility can survive to the mutation point.

For the integrated mutation-boundary governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Authority re-derivation model

Traditional distributed systems allow authority to propagate through delegation chains.

Example:

User → Agent A → Agent B → Agent C

Authority persists while scope narrows.

This creates windows where authority may continue executing after the conditions that justified it have changed.

DTPE uses a different model.

Authority does not propagate.

Authority must be re-derived at execution boundaries.

Execution model:

Execution Step N  
→ Authority Collapse  
→ Authority Re-Derivation  
→ Execution Step N+1

Authority therefore exists only during valid transitions.

## Authority collapse

Authority collapse prevents persistent authority inheritance.

At each execution boundary:

- authority collapses
- the system attempts recomputation
- recomputation uses canonical identity and policy state
- execution continues only if recomputation succeeds

If recomputation fails:

- execution stops

Authority cannot persist across boundaries.

## Execution-path collapse

Collapse must occur directly in the execution path.

Execution Request  
→ Authority Collapse  
→ Authority Re-Derivation  
→ Execution Gate  
→ Actuation

If re-derivation fails, execution becomes impossible.

This converts authority collapse into a runtime containment mechanism.

## Validation-actuation risk

In many architectures a gap exists between validation and execution.

Validation  
→ Authority confirmed  
→ Time passes  
→ Execution occurs

If system conditions change during this gap, authority may become invalid.

DTPE therefore treats admissibility as a gate on whether a transition may become real, not merely as a descriptive property of a recorded action.

## Runtime containment

Authority collapse functions as containment.

When recomputation fails:

- authority becomes invalid
- execution cannot proceed
- runtime halts the action

Invalid authority cannot propagate.

## Authority as derived runtime state

Authority is not a persistent permission.

Authority becomes a computed runtime property derived from:

- policy
- identity
- system state
- execution intent

Authority exists only during valid state transitions.

## Admissibility

Even when authority is valid, a transition must still be admissible.

Admissibility evaluates:

- current system state
- proposed transition
- policy constraints
- execution intent
- authority binding

Execution proceeds only if the transition is admissible.

## Governance kernel definition

A governance kernel is the smallest deterministic runtime component that evaluates whether system state transitions are permitted under defined policy constraints.

DTPE enforces this evaluation at the execution boundary and produces canonical receipts that allow independent verification without trusting the runtime.

## Enforceability posture

DTPE should distinguish honestly between mutation paths that are:

- strong
- bounded
- detectable-only

This prevents false equivalence between architectures that can fail closed at the true mutation boundary and architectures that can only explain or detect afterward.

## Architectural implication

The system no longer only records decisions.

It governs whether system evolution is permitted.

All future phases must preserve the core invariant:

verify without trusting the runtime that generated it
