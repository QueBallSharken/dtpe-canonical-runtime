# DTPE Architecture Overview

## Purpose

This document provides a concise system overview so contributors and reviewers can quickly understand the DTPE runtime structure.

## Core invariant

verify without trusting the runtime that generated it

## High-level execution flow

request → execution boundary → decision → canonical receipt → ledger append → offline verification

## Execution boundary

The execution boundary is the point where DTPE determines whether a proposed transition may become real.

This boundary evaluates the governing decision inputs before irreversible mutation and produces the canonical decision basis recorded in the receipt and ledger.

DTPE phase progression at the boundary is:

- Phase 4: authority validation
- Phase 5: authority validation, state admissibility, system stability
- Phase 6: authority validation, state admissibility, system stability, temporal invariant enforcement

## Boundary integrity and mutation authority

DTPE governs mutation through an explicit execution boundary.

That boundary functions as mutation authority when it actually controls the irreversible primitive that would make a transition real.

This means DTPE distinguishes:

- authorization integrity
- execution evidence
- boundary integrity

These are not interchangeable.

A system can validate authority, record a receipt, and replay a decision afterward, yet still fail governance if stale or invalid admissibility can survive to the mutation point.

DTPE therefore treats admissibility as a gating condition on whether a transition may become real, not merely as a descriptive property of an action record.

For the integrated mutation-boundary governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Runtime artifacts

The runtime produces:

- canonical policy snapshots
- canonical authority snapshots
- canonical receipts
- append-only ledger records
- offline verification results

## Strategic direction

DTPE is evolving from a verification runtime into a deterministic governance kernel for automated systems.
