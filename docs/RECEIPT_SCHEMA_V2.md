# Receipt Schema V2

## Purpose

This document defines the receipt-level evidence structure used by DTPE.

The receipt is the canonical evidence artifact emitted from the execution boundary and preserved for ledger append and offline verification.

The receipt is evidence of the governing boundary decision.
It is not a substitute for enforcing that decision inline.

For the integrated mutation-boundary governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Core requirement

A receipt must contain sufficient canonical evidence to allow an offline verifier to replay the recorded boundary decision deterministically from canonical inputs.

A structurally incomplete receipt is not valid governance evidence.

## Receipt function

The receipt binds enough information to determine:

- what transition was attempted
- what authority or policy basis governed evaluation
- what admissibility-relevant state was used
- what execution-time binding applied
- whether the outcome was refusal or success

## Required evidence fields

Receipt V2 must preserve boundary-relevant evidence including:

- `execution_state`
- `reason`
- `authority_hash`
- `policy_state_hash`
- `crypto_profile`
- `state_admissibility_result`
- `stability_result`
- `receipt_canonical`
- `receipt_hash`

Where temporal invariants are active, the receipt must also preserve:

- `temporal_invariant_result`
- `execution_time` where required by the active boundary phase

## Boundary evidence and execution evidence

The receipt may record both:

- boundary decision evidence
- execution evidence

These are related but not interchangeable.

A system can accurately record what happened and still fail governance if invalid admissibility was allowed to survive to mutation.

Accordingly, receipt accuracy does not weaken the requirement that the execution boundary refuse invalid mutation inline.

## Refusal behavior

A refusal outcome is a governed result.

A receipt for refusal must preserve enough canonical evidence to show:

- what was evaluated
- why the boundary refused
- how an offline verifier can replay that refusal deterministically

A refusal receipt is not an error artifact or undefined side path.

## Deterministic requirements

Receipt generation must be:

- canonical
- deterministic
- replayable
- independent of hidden runtime context

## Offline verification requirement

An offline verifier must be able to recompute the recorded boundary decision from canonical receipt inputs and detect divergence.

## Relationship to other specifications

Receipt Schema V2 works with:

- `PHASE5_EXECUTION_BOUNDARY.md`
- `STATE_ADMISSIBILITY_SPEC.md`
- `PHASE6_TEMPORAL_INVARIANTS.md`
- verifier tooling and ledger verification flows
