DTPE Next Implementation Target

Purpose

This document defines the exact next repository-authoritative target for future work sessions.

Current confirmed state

The grounded repo state for this thread is internally inconsistent at the documentation level.

Current planning docs still describe:

- Phase 5 as the effective public baseline
- Phase 6 as the next public implementation target
- Phase 7 as not yet public

But the visible grounded runtime path already includes:

- temporal invariant handling
- frame continuity handling
- bounded signal_profile construction
- bounded decision_space construction
- continuity-related receipt fields
- evaluator_trace-related receipt binding
- evaluator_trace-related verifier validation with evaluator_rule_hash

Core invariant

verify without trusting the runtime that generated it

Exact next target

The exact next target is documentation reconciliation.

Required sequence:

Step 1
Reconcile CURRENT_IMPLEMENTATION_STATE.md with visible committed runtime structures.

Step 2
Reconcile PROJECT_ROADMAP.md with the same current runtime surface.

Step 3
Replace this file so it no longer describes the repo as Phase 5 only or Phase 7 absent.

Step 4
Only after those three files align, define the next bounded implementation target.

PQC / Crypto-Agility Guardrail

All repository-state and planning updates must preserve DTPE's crypto-agility posture.

Nothing in this cleanup authorizes:

- implicit cryptographic behavior
- silent profile substitution
- hard-coding a single permanent algorithm assumption
- weakening replayability across profile transitions

All current and future runtime and documentation alignment must remain compatible with:

- explicit crypto-profile identity
- policy-governed permitted profiles
- governed migration across profile generations
- independently reconstructable historical evidence
- post-quantum readiness

Public repo restriction

Do not authorize additional runtime behavior until the repository's current implemented baseline is described consistently.

Must not do in the next cycle

- must not describe the repo as Phase 5 only
- must not describe Phase 7 as absent from the public repo
- must not describe Phase 9 as both reverted and implemented
- must not use stale planning text as implementation authority
- must not treat the portable-invariant direction as code authorization before baseline reconciliation is complete

Definition of done

This document-cleanup target is complete only when:

- CURRENT_IMPLEMENTATION_STATE.md matches visible repo structures
- PROJECT_ROADMAP.md matches the same baseline
- this file matches the same baseline
- no contradictory Phase 9 statement remains across those files

END OF FILE
