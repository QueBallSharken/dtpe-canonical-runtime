DTPE / IAL / SPECTRE — PHASE 7 ADDENDUM (SEMANTIC LOCK)
FINAL CLARIFICATION — NO SCOPE EXPANSION

PURPOSE

This addendum resolves remaining semantic ambiguities in Phase 7 without altering
core architecture, invariants, or implementation structure.

This is a clarification layer, not a redesign.

----------------------------------------------------------------
SECTION A — SEQUENCE SCOPE LIMITATION
----------------------------------------------------------------

Current sequence_id definition:

sequence_scope = {
  "authority_hash": authority_hash,
  "execution_intent": execution_intent
}

sequence_id = SHA256(canonical_json(sequence_scope))

CLARIFICATION:

This definition MAY cause distinct logical workflows to share the same sequence_id
if they have identical authority_hash and execution_intent.

This is ACCEPTED behavior in Phase 7.

Phase 7 does NOT attempt to distinguish independent workflows beyond the canonical inputs above.

IMPLICATION:

- Continuity is enforced across all decisions sharing sequence_id
- Separation of independent workflows with identical authority and intent is NOT guaranteed

EXTENSION RULE (OPTIONAL — FUTURE PHASE):

If stricter separation is required, a canonical discriminator MUST be introduced:

Example:

sequence_scope = {
  "authority_hash": authority_hash,
  "execution_intent": execution_intent,
  "sequence_context_id": str
}

This field MUST be:

- canonical
- recorded
- replayable
- deterministic

No implicit or runtime-derived discriminator is permitted.

----------------------------------------------------------------
SECTION B — TEMPORAL ORDERING SEMANTICS
----------------------------------------------------------------

Current rule:

current.execution_time >= prior.execution_time

CLARIFICATION:

Phase 7 enforces:

MONOTONIC NON-DECREASING TEMPORAL ORDER

This means:

- equal timestamps ARE allowed
- strict increase is NOT required

INTERPRETATION:

- ordering is guaranteed to be non-decreasing
- simultaneous or co-timed decisions are permitted

STRICT ORDERING (OPTIONAL — FUTURE):

If strict ordering is required, rule MUST be replaced with:

current.execution_time > prior.execution_time

Such a change MUST be:

- explicitly defined
- consistently enforced
- verifier-reproducible

----------------------------------------------------------------
SECTION C — TRANSITION AND TEMPORAL INTERACTION
----------------------------------------------------------------

Phase 7 defines two independent checks:

1. FRAME CONTINUITY
2. TEMPORAL CONTINUITY

CLARIFICATION:

These checks are evaluated independently.

AUTHORIZED FRAME TRANSITION:

- is determined solely by canonical transition rules
- is NOT constrained by temporal conditions beyond Phase 6 validity

TEMPORAL CONTINUITY:

- enforces ordering only
- does NOT restrict when transitions may occur

IMPLICATION:

- an authorized transition may occur at any valid execution_time
- no temporal gating of transitions exists unless explicitly introduced

EXTENSION RULE (OPTIONAL — FUTURE):

Temporal constraints on transitions MUST be defined within:

temporal_rule_profile

Such constraints MUST be:

- canonical
- deterministic
- verifier-reproducible

----------------------------------------------------------------
SECTION D — SEQUENCE MODEL (LINEARITY)
----------------------------------------------------------------

Phase 7 defines a LINEAR continuity model.

CLARIFICATION:

Each decision references at most one prior decision:

prior_invariant_frame_hash

Therefore:

- sequences are strictly linear chains
- no branching semantics are defined
- no convergence semantics are defined
- no parallel lineage resolution is defined

IMPLICATION:

- multiple decisions MAY reference the same prior
- such behavior is NOT restricted by Phase 7
- conflict resolution is NOT defined at this layer

OUT OF SCOPE:

- branching validation
- DAG-based continuity
- multi-parent lineage
- sequence termination semantics

EXTENSION RULE (FUTURE PHASE):

If branching is introduced:

- continuity model MUST be extended to graph-based verification
- prior linkage rules MUST be expanded
- verifier MUST support multi-edge validation

----------------------------------------------------------------
FINAL CLARIFICATION STATEMENT
----------------------------------------------------------------

Phase 7 guarantees:

- deterministic frame continuity
- deterministic temporal ordering (non-decreasing)
- explicit prior linkage
- replay-verifiable sequence integrity

Phase 7 does NOT guarantee:

- distinct workflow separation beyond canonical inputs
- strict temporal ordering
- temporal constraints on transitions
- branching or graph-based continuity
