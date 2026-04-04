# Boundary Integrity and Mutation Authority

## Purpose

This document defines the mutation-boundary governance model used by DTPE.

It integrates the architectural role of:

- mutation authority
- boundary integrity
- admissibility
- continuity and anti-interleaving
- session invalidation
- boundary evidence
- enforceability class

It does not replace the state admissibility specification, temporal invariants, or receipt schema.
It defines how those subordinate components fit together at the point where a system decides whether an irreversible transition may become real.

## Core claim

No irreversible mutation may occur except through explicit mutation authority that evaluates a closed, still-governing admissibility predicate against authoritative boundary state under a declared continuity mechanism and refuses otherwise.

A valid receipt is evidence of that boundary decision.
It is not a substitute for enforcing it.

## Non-substitution method

A path cannot claim strong governance unless it:

1. identifies the true irreversible primitive
2. identifies the component that can still refuse before that primitive occurs
3. identifies every load-bearing invalidation input that may change between authorization and effect
4. shows whether those inputs are held constant or re-derived at that boundary
5. only then classifies the path as strong, bounded, or detectable-only

This method exists to prevent substitution.

Without it, architectures can still overclaim governance by substituting:

- source of authority for mutation authority
- policy evaluation for mutation control
- token issuance for live admissibility
- anti-replay for anti-staleness
- local forwarding control for control of the true effect boundary
- evidence quality for fail-closed enforcement

## True irreversible primitive

The true irreversible primitive is the concrete state-changing operation after which the governed system can no longer prevent the side effect from becoming real by local refusal alone.

Examples include:

- write
- send
- publish
- transfer
- queue irreversible downstream work
- invoke an external side effect
- commit a state transition

A governed path must identify the true irreversible primitive it claims to control.

## Mutation authority

Mutation authority is the component that can still refuse before the true irreversible primitive occurs.

This role is not automatically identical to:

- the root source of authority
- the delegating principal
- the policy evaluator
- the registry
- the token issuer
- the last visible local checkpoint

Those may all contribute to legitimacy, but none of them count as mutation authority unless they actually control whether the side effect becomes real.

If a component evaluates policy but cannot still refuse before the primitive occurs, it is not the mutation authority for that path.

## Boundary integrity

Boundary integrity is the requirement that the admissibility predicate both holds and remains authoritative through the validation-to-mutation boundary.

This is stricter than:

- authorization validity
- execution evidence
- transport integrity
- faithful forwarding
- post-hoc replay

A system can satisfy all of those and still fail governance if stale or invalid admissibility can survive to the mutation point.

## Admissibility as gate, not property

Admissibility is not a descriptive property of an action record.

Admissibility is a gating condition on whether the transition may become real.

A system that records failed admissibility but still permits the irreversible primitive has not governed the mutation boundary.

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

## Load-bearing invalidation inputs

A load-bearing invalidation input is any input whose change between authorization and effect can make the transition no longer legitimate.

Typical categories include:

- authority or revocation state
- temporal validity
- resource state
- exclusivity or concurrency state
- cumulative or session state
- override state
- behavioral trust, only when explicitly declared as governing for that mutation class

If such an input can change between authorization and effect, the architecture must state whether it is held constant or re-derived at the true mutation boundary.

## Held constant

An input is held constant only if the architecture prevents that input from changing in any way that would affect admissibility before the true irreversible primitive occurs.

Examples may include:

- exclusivity lock
- version-checked reservation
- immutable snapshot with enforced commit coupling
- equivalent mechanism that makes stale evaluation unusable

A mere earlier read, cache, or advisory snapshot does not count as held constant.

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

## Claim-time and commit-time admissibility

Claim-time admissibility is not equivalent to commit-time admissibility.

A frozen admissibility snapshot is sufficient only if the architecture can show either:

- that no load-bearing invalidation input can change before the effect occurs
- or that all such inputs are re-derived at the true mutation boundary before mutation is allowed

Otherwise anti-replay, anti-transfer, and scoped authorization are doing different work than live admissibility and must not be treated as equivalent.

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

The true mutation boundary can fail closed before the irreversible primitive occurs, and all load-bearing invalidation inputs that may change before effect are held constant or re-derived there.

### Bounded

The system can constrain, bind, or re-check important inputs and reduce drift, but cannot fully guarantee fail-closed control at the true irreversible primitive.

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

Together, these components support mutation-boundary governance.
This document defines the architectural method that prevents substitution and overclaiming across that model.
