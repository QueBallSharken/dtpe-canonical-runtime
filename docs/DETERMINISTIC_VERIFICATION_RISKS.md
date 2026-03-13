DTPE Deterministic Verification Risks

Purpose

This document locks in the main risks that could silently break the
core DTPE invariant:

verify without trusting the runtime that generated it

Primary failure mode

A runtime decision uses information that is not canonically recorded
and cannot be reconstructed by an independent verifier.

If that occurs, the runtime may still function, but independent
verification is broken.

------------------------------------------------

Critical Risks

1. Hidden runtime context

Risk
A binding decision depends on in-memory state, transient flags,
local-only counters, or unstored environment context.

Why this breaks verification
The verifier cannot reconstruct the actual decision inputs.

Rule
No binding decision may depend on hidden runtime context.

------------------------------------------------

2. Non-canonical state inputs

Risk
State evaluation depends on data that is not canonicalized or not
bound into receipts, snapshots, or replayable evidence.

Why this breaks verification
The same decision cannot be deterministically reproduced across
environments.

Rule
All binding evaluation inputs must be canonical and replayable.

------------------------------------------------

3. Predicted next state not reproducible

Risk
State admissibility depends on a predicted next state that cannot be
deterministically derived from recorded current state and transition
inputs.

Why this breaks verification
The verifier cannot recompute the admissibility judgment.

Rule
Predicted next state must be either:
- deterministically derivable from canonical inputs, or
- sufficiently captured in canonical evidence

------------------------------------------------

4. Temporal history not reconstructable

Risk
Temporal invariant checks use history that is not derivable from the
ledger or other canonical recorded artifacts.

Why this breaks verification
The verifier cannot replay sequence-level decisions.

Rule
All temporal evaluation context must be reconstructable offline.

------------------------------------------------

5. Silent crypto behavior changes

Risk
Runtime changes signature behavior, profile selection, canonicalization
rules, or migration handling without explicit profile-bound evidence.

Why this breaks verification
Historical receipts become ambiguous or unreplayable.

Rule
Cryptographic behavior must remain policy-governed, explicit, and
profile-bound.

------------------------------------------------

6. Receipt insufficiency

Risk
The runtime emits final decisions without enough evaluation detail for
independent replay.

Why this breaks verification
The verifier sees the outcome but cannot reproduce the reasoning path.

Rule
Receipts must include enough canonical fields for deterministic replay.

------------------------------------------------

7. External dependency leakage

Risk
Boundary decisions depend on live service calls, remote responses,
wall-clock timing, or nondeterministic scheduling.

Why this breaks verification
Offline replay becomes impossible.

Rule
Binding decisions must not depend on non-portable external context.

------------------------------------------------

Must Do

- Use only canonical recorded inputs for binding decisions
- Keep receipt fields sufficient for replay
- Keep receipt schema version explicit
- Keep crypto profiles explicit
- Keep migration rules deterministic
- Keep refusal paths canonical and replayable
- Ensure verifier logic uses only exported artifacts

Must Not Do

- Must not rely on hidden runtime context
- Must not rely on unstored local memory state
- Must not rely on wall-clock dependent behavior
- Must not rely on external service responses
- Must not silently substitute cryptographic algorithms
- Must not silently change canonicalization rules
- Must not introduce runtime state that cannot be replayed offline

Design test

Before any new guard, constraint, or feature is accepted, answer:

1. What are the canonical inputs?
2. Can they be reconstructed offline?
3. What is the deterministic decision function?
4. What receipt fields permit replay?
5. How does the verifier recompute the result?

If any answer is missing, the feature must not participate in binding
execution decisions.

END OF FILE
