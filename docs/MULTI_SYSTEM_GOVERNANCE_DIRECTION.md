DTPE Multi-System Governance Direction

Purpose

This document defines the strategic direction that extends DTPE from
single-runtime deterministic governance toward governance across
multiple systems while preserving the core invariant.

Core invariant

verify without trusting the runtime that generated it

Strategic direction

DTPE is evolving toward a deterministic governance system that can
govern not only a single execution environment, but also coordinated
actions across multiple systems.

Interpretation

Single-system DTPE proves:
- who acted
- why the action was authorized
- whether the resulting state was admissible
- whether the system remained stable
- whether temporal invariants were preserved

Multi-system DTPE must preserve the same properties across interacting
systems.

Multi-system governance objective

Enable multiple systems to emit canonical governance evidence such that
an independent verifier can reconstruct:
- which system acted
- which authority and policy context applied
- which state transition was proposed
- which cross-system constraints applied
- why the action was allowed or refused
- whether the combined system trajectory remained inside permitted bounds

Non-negotiable requirement

Cross-system governance must not rely on hidden shared runtime context.

Any cross-system decision must remain replayable from canonical,
recorded, independently verifiable inputs.

Required properties for future multi-system support

- system identity must be explicit
- governance evidence must remain canonical
- cross-system interactions must be independently reconstructable
- crypto profiles must remain explicit and policy-governed
- refusal paths must remain canonical and replayable
- temporal reasoning must remain ledger-derivable or otherwise
  canonically recorded

Forbidden future pattern

decision = f(local_inputs + hidden_cross_system_state)

Required future pattern

decision = f(canonical_local_inputs + canonical_cross_system_inputs)

Implications

Future federation or orchestration features must:
- define canonical cross-system input models
- define replayable cross-system receipt evidence
- define verifier recomputation rules
- preserve offline independent verification

Relationship to PQC direction

Multi-system governance must remain durable across crypto profile
transitions.

This means:
- profile identity must remain explicit across systems
- profile migration must remain governed and evidenced
- historical cross-system evidence must remain reconstructable across
  profile generations

Long-term expected outcome

DTPE becomes a deterministic governance kernel capable of governing
actions within and across multiple systems while preserving canonical
receipts, append-only evidence, and independent offline verification.

Design gate

No multi-system feature is complete unless an independent verifier can
recompute the cross-system decision context from canonical recorded
inputs alone.

END OF FILE
