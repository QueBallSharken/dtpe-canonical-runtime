DTPE Next Implementation Target

Purpose

This document defines the exact next implementation target so future
work sessions, contributors, and reviewers can continue without
reconstructing context.

Current confirmed state

Implemented and committed:
- architecture overview and roadmap documents
- boundary invariant rules
- Phase 5 execution boundary architecture
- Phase 6 temporal invariant architecture
- Phase 7 governance kernel roadmap
- deterministic verification risks
- PQC governance direction
- receipt schema v2
- Phase 5 scaffold runtime modules

Current scaffold modules
- core/spectre/boundary.py
- core/spectre/state_guard.py
- core/spectre/stability_guard.py

Core invariant

verify without trusting the runtime that generated it

Non-negotiable rules

- No binding execution decision may depend on hidden runtime context.
- All binding decisions must be replayable from canonical recorded inputs.
- Receipts must remain sufficient for offline recomputation.
- Crypto profile handling must remain explicit and policy-governed.

Current architectural alignment

STATE_ADMISSIBILITY_SPEC.md defines:

admissible = f(canonical_current_state, canonical_transition)

Required admissibility inputs:
- canonical_current_state
- canonical_transition
- canonical_policy_state_hash
- execution_intent
- authority_hash
- crypto_profile

Current code gap

core/spectre/boundary.py currently passes:
- current_state
- proposed_transition

This means the scaffold is not yet fully aligned with the admissibility specification.

Exact next implementation target

Step 1
Align core/spectre/state_guard.py interface to STATE_ADMISSIBILITY_SPEC.md.

Step 2
Update core/spectre/boundary.py so it passes the full canonical admissibility input set.

Step 3
Do not yet widen scope to temporal invariants or multi-system orchestration until Phase 5 spec-to-code alignment is complete.

Expected next commit scope

The next engineering commit should:
- update the admissibility interface
- update the boundary call signature
- preserve deterministic replayability
- avoid introducing hidden runtime context
- avoid changing receipt semantics beyond what is required for alignment

Must not do in the next commit

- Must not introduce non-canonical state inputs
- Must not introduce wall-clock or environment-dependent decision inputs
- Must not silently infer missing canonical fields
- Must not expand into Phase 6 implementation yet
- Must not break offline replay assumptions

Definition of done for this target

This target is complete only when:
- boundary.py matches STATE_ADMISSIBILITY_SPEC.md inputs
- state admissibility evaluation can be replayed from canonical inputs
- the new interface preserves the core invariant

END OF FILE
