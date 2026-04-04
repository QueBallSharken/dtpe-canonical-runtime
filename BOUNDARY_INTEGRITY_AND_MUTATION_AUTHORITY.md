# Boundary Integrity and Mutation Authority

## Purpose

This document integrates the mutation-boundary governance model across DTPE.

It does not replace the state admissibility specification, temporal invariants, or receipt schema. It defines how those components fit together at the point where a system decides whether an irreversible transition may become real.

The core concern is not only whether a system can evaluate policy, record evidence, or replay a decision afterward.

The core concern is whether the component that controls the irreversible primitive can still refuse under authoritative live conditions when the moment of mutation arrives.

## Core claim

No irreversible mutation may occur except through explicit mutation authority that evaluates a closed, still-governing admissibility predicate against the authoritative boundary state, under a declared continuity mechanism, and refuses otherwise.

A valid receipt is evidence of that boundary decision. It is not a substitute for enforcing it.

## Irreversible primitive

An irreversible primitive is the concrete state-changing operation that makes a transition real.

Examples include:

- write
- send
- publish
- transfer
- queue irreversible downstream work
- invoke an external side effect
- commit a state transition

A governed path must identify the irreversible primitive it controls.

If the primitive is not explicitly identified, the system cannot honestly claim that it governs the mutation boundary.

## Mutation authority

Mutation authority is the component that actually controls whether the irreversible primitive may occur.

This role is not automatically identical to:

- the policy engine
- the component that issued an authorization artifact
- the component that records a receipt afterward
- the agent that requested the action

The relevant authority is the component that can still refuse before the irreversible primitive becomes real.

If a component evaluates policy but cannot prevent the primitive from occurring, it is not the mutation authority for that path.

## Boundary integrity

Boundary integrity is the requirement that the admissibility predicate both holds and remains authoritative through the validation-to-mutation boundary.

This is stricter than:

- authorization validity
- execution evidence
- post-hoc replay
- transport integrity
- faithful forwarding

A system can satisfy all of those and still fail governance if stale or invalid admissibility can survive to the mutation point.

## Admissibility as gate, not property

Admissibility is not a descriptive property of an action record.

Admissibility is a gating condition on whether the transition may become real.

A system that records that admissibility failed but still permits the irreversible primitive has not governed the mutation boundary.

In DTPE terms, a failed boundary decision must result in refusal rather than a valid mutation outcome.

## Admissibility scope

The admissibility predicate must be evaluated against a closed input surface.

Depending on the mutation class, admissibility inputs may include:

- policy state
- authority state
- revocation state
- resource state
- temporal validity
- exclusivity or concurrency constraints
- cumulative or session state
- override validity
- other explicitly declared governance inputs

If a governing input is omitted, the architecture can appear rigorous while only enforcing against a partial slice of the real state.

A governed mutation path must declare its admissibility-relevant input surface explicitly.

## Continuity and anti-interleaving

Revalidating before mutation is not the same thing as governing mutation.

If validation and mutation can be interleaved, stale admissibility can survive across the boundary even if the validation logic is correct.

A governed mutation path must declare the mechanism that prevents stale authority or stale admissibility from surviving to the irreversible primitive.

Examples include:

- non-interruptible validate-to-mutate critical section
- compare-and-swap or version-checked mutation
- single-use state-locked mutation token
- equivalent primitive that makes stale authority unusable at the boundary

Sequencing alone is insufficient.

## Session invalidation

Admissibility is not purely per-action.

Prior events may invalidate future mutation rights before the next side effect occurs.

Examples include:

- revocation landing between actions
- cumulative quota exhaustion
- delegation narrowing
- prior mutation changing the admissibility space
- concurrent or branching activity invalidating a later step
- a sequence that is individually admissible step-by-step but invalid in composition

DTPE therefore distinguishes action-local validity from session-level invalidation effects.

## Boundary artifact

A governed mutation path must emit verifiable boundary evidence sufficient to reconstruct what governed the decision.

This artifact exists to make the boundary decision externally auditable.

It does not replace the runtime requirement to refuse invalid mutation inline.

At minimum, the boundary artifact should bind enough information to determine:

- what transition was attempted
- what authority or policy basis governed evaluation
- what admissibility-relevant state was used
- what execution-time binding applied
- whether the result was refusal or success

The exact field requirements are defined by subordinate receipt and verification specifications.

## Local and cross-boundary mutation

Not all mutation paths support the same governance strength.

If the true irreversible primitive is controlled locally by the enforcing boundary, strong inline governance may be possible.

If the final effect depends on an external opaque system or third-party authority, the local system may only be able to:

- strongly govern the outbound request
- bound staleness or divergence
- attest what was sent
- detect inconsistency afterward
- trigger rollback, dispute, or containment procedures

Strong local control over an outbound request is not automatically strong governance over the final external mutation.

DTPE therefore distinguishes local mutation atomicity from cross-boundary mutation limits.

## Enforceability class

Each mutation-capable path should be classified honestly.

### Strong

The true mutation boundary can refuse inline under still-governing admissibility before the irreversible primitive occurs.

### Bounded

The system can constrain or re-check important inputs and reduce drift, but cannot fully guarantee inline control of the true effect boundary.

### Detectable-only

The strongest available guarantee is tightly bound post-hoc falsifiability, attestation, or divergence detection after the side-effect path has proceeded.

This classification prevents false equivalence between architectures that can fail closed at the true mutation boundary and architectures that can only explain or detect afterward.

## Relationship to subordinate specifications

This document integrates, but does not replace, the following DTPE components:

- `STATE_ADMISSIBILITY_SPEC.md` defines admissibility inputs and reproducibility requirements
- `PHASE5_EXECUTION_BOUNDARY.md` defines boundary decision behavior and refusal semantics
- `PHASE6_TEMPORAL_INVARIANTS.md` defines temporal validity as a canonical input to boundary evaluation
- `RECEIPT_SCHEMA_V2.md` defines receipt-level evidence structures
- verifier tooling checks replay consistency against recorded canonical artifacts

Together, these components support mutation-boundary governance. This document defines the architectural role they play in that larger model.
