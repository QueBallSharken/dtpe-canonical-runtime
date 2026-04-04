# State Admissibility Specification

## Purpose

This document defines the deterministic state-admissibility model used by the DTPE execution boundary.

State admissibility determines whether a proposed transition is admissible relative to canonical current state and canonical transition inputs.

It is a subordinate component of DTPE boundary integrity.

For the integrated mutation-boundary governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Core rule

Boundary admissibility decisions must be deterministically replayable from canonical inputs.

## Decision model

admissible = f(canonical_current_state, canonical_transition)

## Admissibility inputs

The admissibility decision is evaluated from canonical inputs including:

- `canonical_current_state`
- `canonical_transition`
- `canonical_policy_state_hash`
- `execution_intent`
- `authority_hash`
- `crypto_profile`

These inputs define part of the canonical boundary input surface used to determine whether a proposed transition may become real.

This specification does not, by itself, define mutation authority, temporal validity, continuity requirements, or enforceability class.

## Deterministic requirements

- inputs must be canonicalized
- inputs must be reproducible
- inputs must be verifiable offline
- inputs must not depend on hidden runtime context

## Replay requirement

An offline verifier must be able to recompute the admissibility decision using only the canonical receipt inputs.

## Receipt binding

Receipts must contain sufficient evidence to replay admissibility evaluation.

## Failure behavior

If admissibility cannot be recomputed deterministically:

- `execution_state = REFUSED_NON_BINDING`

## Invariant

Boundary admissibility decisions must remain:

- deterministic
- replayable
- independent of hidden runtime state
