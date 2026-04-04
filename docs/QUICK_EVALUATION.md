# DTPE Quick Evaluation Guide

## Purpose

This document allows a reviewer to understand and evaluate the DTPE prototype in a few minutes.

## Problem

Most automated systems rely on logs and internal controls to explain decisions after they occur.

These approaches require trusting the system that produced the logs.

DTPE explores a different model.

Instead of trusting logs, the system produces deterministic evidence that a decision followed policy.

That evidence can be verified independently.

## Key idea

DTPE recomputes authority from canonical inputs at execution boundaries and preserves canonical evidence for offline verification.

When a decision occurs, the runtime produces:

- a canonical receipt
- a signed authority record
- a ledger entry

These artifacts allow an external verifier to confirm that the decision complied with policy.

## What the prototype demonstrates

The reference runtime demonstrates:

- policy snapshot binding
- authority recomputation at execution boundaries
- canonical receipt generation
- append-only ledger evidence
- independent offline verification

## Boundary-governance review questions

A reviewer should now ask more than whether the runtime logs decisions correctly.

For each mutation-capable path, the stronger governance questions are:

- what is the irreversible primitive
- what component is the mutation authority
- what admissibility inputs govern the transition
- what prevents stale admissibility from surviving to mutation
- what evidence is preserved for replay and verification
- what enforceability class the path honestly achieves

For the integrated mutation-boundary governance model, see `BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`.

## Quick demo

From the repository root run:

```bash
python -m tools.run_demo
