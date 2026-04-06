# DTPE Architecture Overview

## Purpose

This document provides a concise system overview so contributors and reviewers can quickly understand the DTPE runtime structure.

## Core invariant

verify without trusting the runtime that generated it

## High-level execution flow

request -> execution boundary -> decision -> canonical receipt -> ledger append -> offline verification

## Execution boundary

The execution boundary is the point where DTPE determines whether a proposed transition may become real.

This boundary evaluates the governing decision inputs before irreversible mutation and produces the canonical decision basis recorded in the receipt and ledger.

The DTPE boundary model includes authority validity, state admissibility, system stability, temporal validity, and later continuity-oriented invariants as the architecture evolves.

## Boundary integrity and mutation authority

DTPE governs mutation through an explicit execution boundary.

That boundary functions as mutation authority when it actually controls the irreversible primitive that would make a transition real.

This means DTPE distinguishes:

- authorization integrity
- execution evidence
- mutation authority
- boundary integrity

These are not interchangeable.

A system can validate authority, record a receipt, and replay a decision afterward, yet still fail governance if stale or invalid admissibility can survive to the mutation point.

DTPE therefore treats admissibility as a gating condition on whether a transition may become real, not merely as a descriptive property of an action record.

For the integrated mutation-boundary governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Portable continuity direction

DTPE's portable-invariant / boundary-to-boundary continuity direction extends the existing execution-boundary model.

It does not replace authority validity, state admissibility, temporal validity, receipts, ledger evidence, or offline replay.

It strengthens the governance claim by requiring the governing basis to survive mutation-capable boundaries as a live refusal condition rather than treating prior authorization or later evidence as sufficient by itself.

For the continuity model, see:

- `PORTABLE_BOUNDARY_INVARIANT.md`
- `PORTABLE_INVARIANT_MAPPING_TO_DTPE.md`

## PQC / crypto-agility posture

Portable-invariant / boundary-to-boundary continuity must remain crypto-profile explicit, policy-governed, and replay-reconstructable across profile transitions.

Nothing in this architecture direction authorizes:

- implicit cryptographic behavior
- silent profile substitution
- hard-coded permanent algorithm assumptions
- weakening replayability across profile transitions

This direction must remain compatible with post-quantum readiness.

## Runtime artifacts

The runtime produces:

- canonical policy snapshots
- canonical authority snapshots
- canonical receipts
- append-only ledger records
- offline verification results

## Strategic direction

DTPE is evolving from a verification runtime into a deterministic governance kernel for automated systems.

That direction includes stronger continuity claims across mutation-capable boundaries while preserving canonical evidence and independent offline verification.
