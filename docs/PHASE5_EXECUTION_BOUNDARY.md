# Phase 5 Execution Boundary

## Purpose

This document defines the Phase 5 execution boundary behavior in DTPE.

Phase 5 extends the boundary beyond authority validation alone. A proposed transition may become real only if the boundary determines that authority is valid, state is admissible, and the system is stable.

## Boundary rule

At the Phase 5 execution boundary:

ALLOW iff:

- authority is valid
- state is admissible
- system is stable

Otherwise:

- refuse
- emit a non-binding refusal result
- preserve enough canonical evidence for replay and verification

## Mutation authority and gating semantics

The execution boundary is the mutation authority for a path only when it actually controls whether the irreversible primitive may occur.

This role is not identical to:

- the component that evaluated policy
- the component that issued an authorization artifact
- the component that later records a receipt

The relevant authority is the component that can still refuse before the transition becomes real.

Accordingly, admissibility at the boundary is a gate, not a descriptive property.

A system that records failed admissibility but still permits the irreversible primitive has not governed the mutation boundary.

In DTPE terms, a failed boundary decision must result in refusal rather than a valid mutation outcome.

For the integrated governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Phase 5 decision inputs

The Phase 5 boundary evaluates canonical inputs sufficient to determine:

- authority validity
- state admissibility
- system stability

These inputs must be reproducible, verifiable offline, and independent of hidden runtime context.

## Phase 5 outputs

The boundary produces a decision result that is sufficient to support:

- canonical receipt generation
- ledger append
- offline replay verification

A refusal outcome is part of the governed boundary behavior. It is not an undefined or advisory side path.

## Relationship to other specifications

Phase 5 boundary behavior depends on subordinate specifications including:

- `STATE_ADMISSIBILITY_SPEC.md`
- receipt schema documentation
- verifier tooling

Later phases may extend the boundary with additional invariants, but they do not reduce the Phase 5 requirement that invalid boundary conditions must refuse rather than mutate.
