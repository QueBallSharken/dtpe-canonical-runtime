# Governance Note — Mutation Authority

Date context: authored before posting related public thread comment.

## Core claim

The missing architectural role is **mutation authority**.

Current governance discussions often separate:

- authorization
- decision artifact / receipt
- execution evidence / attestation
- mutation-time admissibility

But they still leave implicit the component that actually has the authority to let the irreversible side effect occur.

That role is not identical to:

- the component that evaluated policy
- the component that issued the receipt
- the component that later records what happened

It is the component that controls the **state-changing primitive itself**.

## Why this matters

A system can prove all of the following:

- the intent was declared
- the policy decision was valid
- the receipt was signed at evaluation time
- the execution was attested afterward

and still fail governance if the side effect was able to cross the mutation boundary without the same admissibility predicate being revalidated by the authority that actually controls mutation.

So the missing separation is not just:

- decision-time validity
- execution-time evidence
- mutation-time admissibility

It is also:

- **mutation authority** — the fail-closed control point that decides whether the state-changing primitive may become real at all

## Boundary rule

No irreversible mutation may occur unless mutation authority revalidates the bound admissibility predicate against the governing live state at the mutation boundary.

## What is being guarded

Not “execution” in the abstract.

The guarded primitive is the thing that actually changes reality, for example:

- write
- send
- transfer
- publish
- queue irreversible downstream work
- invoke an external side effect
- commit a state transition

If that primitive is not identified, systems can claim enforcement while still allowing real side effects to happen before the supposed gate.

## What must still hold

The admissibility predicate may include:

- policy state
- authority / delegation state
- tool or capability constraints
- resource state
- temporal validity
- exclusivity / concurrency constraints
- override validity
- any other live condition that determines whether the transition may still become real

So the requirement is not merely “re-check policy.”

It is “revalidate the admissibility-relevant state scope that justified the transition.”

## Governance versus attestation

If the system can mutate first and explain later, it is still observational.

If mutation is structurally impossible unless the live predicate passes, it is governable.

This is why better logging, better receipts, better replay, and better post-hoc drift detection are all useful but still insufficient by themselves.

They do not answer whether the system was still allowed to change reality when it actually did.

## Receipt-as-precondition is not enough

A receipt being required is necessary.

But it is still only a gate artifact unless the state-changing primitive is subordinate to it.

A receipt that says:

> these constraints were true at evaluation time

is mainly an evidence object.

A receipt that functions as:

> this mutation may occur only if this same admissibility predicate still holds now

is participating in governance.

That is the difference between **gate integrity** and **boundary integrity**.

## Distributed systems consequence

When policy state, authority state, resource state, and side effects are split across different services, the question is no longer “did we sign the right thing?”

It becomes:

- which authorities are actually in scope for atomic enforcement?
- which are out of scope and therefore only auditable after the fact?
- which component owns mutation authority?
- can that component fail closed before the irreversible step?

If those boundaries are not explicit, the architecture can look governed while only enforcing against a partial slice of the live state.

## Proposed decomposition

1. **Authorization integrity**  
   proves the action was approved under a declared state scope

2. **Execution evidence**  
   proves what actually ran

3. **Mutation authority**  
   is the component that controls the state-changing primitive

4. **Mutation-time admissibility / boundary integrity**  
   requires mutation authority to revalidate the bound admissibility predicate against the governing live state at the mutation boundary and refuse if it no longer holds

## Audit question

What component owns mutation authority, what exact admissibility scope does it revalidate, and can an irreversible side effect occur if that revalidation fails?

## Summary

The missing layer is not another receipt, and not another attestation.

It is the explicit recognition that **mutation authority** must be governed separately from authorization and separately from evidence.

Without that, a system may be able to prove what it decided and what it did, while still being unable to prove it was allowed to do it at the exact moment reality changed.
