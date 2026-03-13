STATE ADMISSIBILITY SPECIFICATION

Purpose
Define the deterministic admissibility model used by the DTPE execution boundary.

Core Rule
Boundary admissibility decisions must be deterministically replayable from canonical inputs.

Decision Model
admissible = f(canonical_current_state, canonical_transition)

Admissibility Inputs
- canonical_current_state
- canonical_transition
- canonical_policy_state_hash
- execution_intent
- authority_hash
- crypto_profile

Deterministic Requirements
- Inputs must be canonicalized
- Inputs must be reproducible
- Inputs must be verifiable offline
- Inputs must not depend on hidden runtime context

Replay Requirement
An offline verifier must be able to recompute the admissibility decision using only the canonical receipt inputs.

Receipt Binding
Receipts must contain sufficient evidence to replay admissibility evaluation.

Failure Behavior
If admissibility cannot be recomputed deterministically:

execution_state = REFUSED_NON_BINDING

Invariant
Boundary admissibility decisions must remain:

deterministic
replayable
independent of hidden runtime state
