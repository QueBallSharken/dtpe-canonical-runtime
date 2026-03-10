DTPE QUICK EVALUATION GUIDE

Purpose

This document allows a reviewer to understand and evaluate the DTPE prototype
in a few minutes.

Problem

Most automated systems rely on logs and internal controls to explain decisions
after they occur.

These approaches require trusting the system that produced the logs.

DTPE explores a different model:

Instead of trusting logs, the system produces deterministic evidence that a
decision followed policy.

The evidence can be verified independently.

Key Idea

DTPE recomputes authority from canonical inputs at execution boundaries.

When a decision occurs, the runtime produces:

- a canonical receipt
- a signed authority record
- a ledger entry

These artifacts allow an external verifier to confirm that the decision
complied with policy.

What the Prototype Demonstrates

The reference runtime demonstrates:

- policy snapshot binding
- authority recomputation at execution boundaries
- canonical receipt generation
- append-only ledger evidence
- independent offline verification

Quick Demo

From the repository root run:

python -m tools.run_demo

Expected output:

PASS: verified 1 ledger record(s)

This indicates that the runtime produced deterministic governance evidence
that can be independently verified.

Research Direction

DTPE explores whether automated systems can move from trust-based governance
(logging and internal controls) to reproducible governance evidence that can
be independently validated.

Repository

https://github.com/QueBallSharken/dtpe-canonical-runtime

END OF FILE
