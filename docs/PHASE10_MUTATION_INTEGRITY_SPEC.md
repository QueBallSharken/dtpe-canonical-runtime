# PHASE 10 - MUTATION INTEGRITY / EXECUTION HARDENING SPEC

## STATUS

- Design locked (documentation only)
- No runtime implementation authorized by this document

---

## PURPOSE

Define mutation integrity as the enforcement layer that ensures the component that changes reality is subordinate to the admissibility predicate at the mutation boundary.

This phase extends DTPE from:

- execution-bound admissibility
- replay integrity
- reconstruction integrity

to:

- mutation-bound enforcement

---

## CORE RULE

No irreversible mutation may occur unless mutation authority revalidates the admissibility predicate against the governing live state at the mutation boundary.

---

## MUTATION AUTHORITY

Mutation authority is the component that controls the state-changing primitive itself.

It is not identical to:

- the component that evaluated policy
- the component that issued a receipt
- the component that later attested or recorded what happened

---

## GUARDED PRIMITIVE

The guarded primitive is any operation that changes reality, including but not limited to:

- write
- send
- transfer
- publish
- queue irreversible downstream work
- invoke external side effects
- commit state transitions

If the guarded primitive is not explicitly identified, governance claims are incomplete.

---

## MUTATION-BOUND ADMISSIBILITY

Mutation authority must revalidate the admissibility predicate at the mutation boundary.

This predicate may include:

- policy state
- authority / delegation state
- capability constraints
- resource state
- temporal validity
- exclusivity / concurrency conditions
- override validity

The requirement is not to re-check policy in isolation, but to revalidate the admissibility-relevant live state scope that justified the transition.

---

## FAIL-CLOSED REQUIREMENT

If mutation authority cannot revalidate the admissibility predicate successfully:

- the mutation MUST NOT occur

If a side effect can occur before revalidation, the system is observational rather than governable.

---

## BOUNDARY INTEGRITY VS GATE INTEGRITY

Gate integrity:
- a receipt or authorization artifact exists

Boundary integrity:
- the side effect is structurally impossible unless admissibility still holds at mutation time

DTPE requires boundary integrity for full governance.

---

## DISTRIBUTED SYSTEMS CONSIDERATION

When policy state, authority state, resource state, and mutation are distributed:

- mutation authority scope must be explicit
- admissibility scope must be explicit
- atomic enforcement boundaries must be defined

If mutation authority cannot enforce across all relevant state:

- the system must explicitly acknowledge partial governance scope

---

## PROOF REQUIREMENT

A system must be able to demonstrate:

- which component owned mutation authority
- what admissibility scope was revalidated
- that the side effect could not occur if the predicate failed

---

## RELATION TO EARLIER PHASES

Phase 5–7:
- establish execution-bound admissibility

Phase 9:
- establish evaluator identity, rule identity, and reconstruction integrity

Phase 10:
- ensure that the component that changes reality is subordinate to those guarantees

---

## NON-GOALS

This phase does not:

- define a specific enforcement mechanism
- assume a single-process architecture
- require co-location of evaluator and mutation authority

---

## SUMMARY

DTPE is not fully governable unless:

- admissibility holds at execution
- admissibility can be replayed
- admissibility can be reconstructed
- AND mutation authority prevents reality from changing unless that admissibility still holds
