DTPE Boundary Invariant Rules

Purpose

This document defines the non-negotiable rules that protect the
core DTPE invariant and ensure the system remains independently
verifiable.

Core Invariant

verify without trusting the runtime that generated it

------------------------------------------------

Primary Rule

No binding execution decision may depend on hidden runtime context.

If a verifier cannot reconstruct the inputs used in a decision,
then that decision cannot be considered verifiable.

------------------------------------------------

Deterministic Boundary Requirement

All boundary decisions must be a pure function of canonical inputs.

decision = f(canonical_inputs)

If a verifier cannot replay the decision from canonical inputs,
the execution boundary must not rely on that information.

------------------------------------------------

Architectural Implication

The execution boundary must remain deterministic,
replayable, and independently verifiable.

END OF FILE
