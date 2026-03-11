DTPE Architecture Overview

Purpose

This document provides a concise system overview so contributors and
reviewers can quickly understand the DTPE runtime structure.

Core invariant

verify without trusting the runtime that generated it

High-level execution flow

request
→ execution boundary
→ decision
→ canonical receipt
→ ledger append
→ offline verification

Execution boundary

Phase-4
authority validation

Phase-5
authority validation
state admissibility
system stability

Phase-6
authority validation
state admissibility
system stability
temporal invariant enforcement

Runtime artifacts

The runtime produces:

- canonical policy snapshots
- canonical authority snapshots
- canonical receipts
- append-only ledger records
- offline verification results

Strategic direction

DTPE is evolving from a verification runtime into a deterministic
governance kernel for automated systems.

END OF FILE
