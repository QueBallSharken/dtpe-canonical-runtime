# Portable Boundary Invariant

## Purpose

This document defines a portable invariant model for transitions that cross multiple mutation-capable boundaries.

The goal is to prevent a system from:

- authorizing once
- trusting transit
- and only attesting afterward

Instead, the same governing invariant must survive each relevant boundary as a live refusal condition and remain enforceable at the true irreversible primitive.

## Core claim

A transition is not valid merely because it was authorized earlier, executed faithfully, or recorded completely.

A transition is valid only if the same governing invariant survives to every mutation-capable boundary as a live refusal condition and still holds at the true irreversible primitive.

## Why this is needed

Many architectures can still fail governance in the following way:

- authorization was valid when checked
- execution matched what was authorized
- evidence is accurate
- the record is complete
- and the transition is still invalid because admissibility was no longer true when commit occurred

This is the boundary failure the portable invariant is designed to prevent.

## Definitions

### Canonical transition identity

The exact governed transition, represented in canonical form, that is permitted to become real.

This is not a feature label or action name.
It is the specific transition that the system is authorizing and governing.

### Mutation-capable boundary

Any boundary where the transition can be transformed, forwarded, delayed, retried, widened, or become materially closer to an irreversible effect.

### True irreversible primitive

The concrete point-of-no-return after which the governed system can no longer prevent the side effect from becoming real by local refusal alone.

### Portable invariant

The carried governing condition that binds:

- the canonical transition identity
- the authorization basis
- the admissibility basis
- the invalidation rules
- the validity bounds
- and the refusal condition

across every mutation-capable boundary.

### Native refusal

A boundary has native refusal if it can block the transition before further mutation-capable progress occurs.

Logging or attestation without the ability to halt does not count as native refusal.

## Formal invariant

For a transition `T` crossing mutation-capable boundaries `B1 ... Bn`, where `Bn` is the true irreversible primitive:

A transition may proceed at boundary `Bi` only if all of the following hold:

1. **Canonical identity preservation**  
   The transition presented at `Bi` is identical to the canonical transition previously authorized, modulo permitted deterministic narrowing only.

2. **Live admissibility re-derivation**  
   The admissibility predicate is re-derived at `Bi` against current governing state, not inherited as a stale earlier result.

3. **Validity continuity**  
   The transition has not been invalidated by replay, supersession, authority change, policy change, session invalidation, resource-state change, or expiration.

4. **Monotonic attenuation**  
   No boundary may widen scope, authority, allowed effects, or validity window. The invariant may remain equal or become narrower only.

5. **Native refusal**  
   If any bound condition fails at `Bi`, that boundary must refuse the transition before further mutation-capable progress occurs.

6. **Final-boundary enforcement**  
   At the true irreversible primitive `Bn`, the same invariant must still hold as a live refusal condition. Otherwise execution is invalid even if prior authorization, evidence, and records are all correct.

## Short form

A governed transition is valid if and only if the same canonical transition, admissibility basis, invalidation rules, and refusal condition survive each mutation-capable boundary without widening and are re-derived under live state at the true irreversible primitive.

## What the invariant must bind

At minimum, the portable invariant should bind:

- canonical transition identity
- principal or delegation basis
- policy basis or policy hash
- authority basis or authority hash
- admissibility basis or admissibility digest
- replay-prevention material
- validity bounds
- session generation or equivalent invalidation context
- refusal semantics

## Invalidation conditions

A carried invariant must be invalidated when any load-bearing bound condition changes.

Typical invalidation conditions include:

- replay
- supersession
- authority change
- revocation
- policy change
- state mismatch
- session invalidation
- resource-state change
- delegation narrowing
- validity-window expiration

Time may be one validity condition, but it should not be the only one.

A weak TTL by itself is usually insufficient if replay, supersession, or state drift can still occur inside the window.

## Monotonic attenuation rule

Every boundary must preserve monotonic attenuation.

This means:

- scope may remain the same or narrow
- authority may remain the same or narrow
- allowed effects may remain the same or narrow
- validity bounds may remain the same or narrow

No boundary may silently widen any of these.

If widening occurs, the invariant has failed.

## Boundary responsibilities

At every mutation-capable boundary, the system must:

1. import the portable invariant
2. verify canonical transition identity
3. re-derive admissibility under live governing state
4. evaluate invalidation conditions
5. verify no widening has occurred
6. refuse locally on mismatch
7. emit a boundary decision artifact

A boundary that can only log and pass through does not preserve the invariant strongly enough to claim full closure at that boundary.

## Boundary decision artifact

Each boundary should emit a decision artifact that captures:

- what transition was presented
- what invariant was imported
- what live admissibility basis was re-derived
- whether the invariant held or failed
- whether the transition was refused or allowed forward
- what validity or invalidation conditions were evaluated

The artifact should capture the boundary decision, not merely the evidence inputs.

## Flow

### Phase A — define the governed transition

1. Identify the exact canonical transition.
2. Identify the true irreversible primitive.
3. Identify every mutation-capable boundary between request and effect.

### Phase B — construct the invariant

4. Bind canonical transition identity.
5. Bind authorization basis.
6. Bind admissibility basis.
7. Bind invalidation rules.
8. Bind validity bounds.
9. Bind monotonic attenuation rules.

### Phase C — enforce at each boundary

10. Re-derive admissibility under live state.
11. Reject on transition mismatch.
12. Reject on invalidation.
13. Reject on widening.
14. Refuse natively if the boundary can mutate.
15. Emit boundary decision artifact.

### Phase D — carry forward

16. Carry the same invariant forward.
17. Do not treat prior approval as sufficient by itself.
18. Repeat re-derivation at every mutation-capable boundary.

### Phase E — final commit

19. Re-derive again at the true irreversible primitive.
20. Refuse on mismatch, replay, supersession, stale state, revocation, or invalid session state.
21. Only then allow the side effect to become real.
22. Emit final execution evidence bound to the same invariant.

## Flowchart

```mermaid
flowchart TD

A[Start with one intended transition] --> B[Define the exact canonical transition identity]
B --> C[Identify the true irreversible primitive]
C --> D[Identify every mutation-capable boundary on the path]

D --> E[At boundary N, import the portable invariant]
E --> F[Re-derive live admissibility against current governing state]
F --> G{Does invariant still hold here?}

G -->|No| H[Refuse transition and emit boundary denial record]
G -->|Yes| I[Check replay, freshness, supersession, and session invalidation]
I --> J{Still valid?}

J -->|No| H
J -->|Yes| K[Verify no widening of scope, authority, or allowed effects]
K --> L{Monotonic narrowing preserved?}

L -->|No| H
L -->|Yes| M[If this boundary can mutate, enforce refusal locally on mismatch]
M --> N[Emit boundary decision artifact]

N --> O{Is this the true irreversible primitive?}
O -->|No| P[Carry invariant forward to next boundary]
P --> E
O -->|Yes| Q[Execute mutation]
Q --> R[Emit final execution evidence bound to the same invariant]
R --> S[End]
