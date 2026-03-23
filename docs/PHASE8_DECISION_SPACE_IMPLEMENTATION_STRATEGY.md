# PHASE 8 DECISION-SPACE IMPLEMENTATION STRATEGY (LOCKED)

## STATUS

Design strategy locked.
No runtime implementation is authorized by this document.

This document defines:

- preferred implementation path
- fallback implementation floor
- rollback triggers
- implementation stop conditions

This document does not modify runtime behavior.

---

## PURPOSE

Phase 8 is locked as:

- Phase 8 = Decision-Space Integrity

This document fixes the implementation strategy before any Phase 8 code is introduced.

Its purpose is to prevent:

- design drift
- partial implementation ambiguity
- non-deterministic field invention
- receipt / verifier divergence
- unsafe rollback decisions

---

## CURRENT BASELINE

Current repository baseline remains:

- Phase 7 implemented and verified
- Phase 8 design locked, not implemented
- Phase 9 design locked, not implemented
- Phase 10 design locked, not implemented

All Phase 8 work must preserve the current verified Phase 7 baseline until full re-verification is complete.

---

## PREFERRED PATH — OPTION B

Preferred implementation target for Phase 8 is:

    Option B = Full Decision-Space Model

Option B is intended to implement the full locked Phase 8 canonical structure, including:

- sequence_id
- policy_hash
- authority_hash
- execution_intent
- signal_profile
- constraint_profile
- visible_alternatives_profile
- risk_frame_profile
- decision_space_version

Option B is the preferred path because it provides the strongest and most complete decision-space integrity model.

---

## FALLBACK FLOOR — OPTION A

Fallback implementation path for Phase 8 is:

    Option A = Minimal Deterministic Decision-Space Core

Option A is permitted only if Option B cannot be completed safely within the repository’s existing invariants.

Option A must remain:

- deterministic
- canonical
- verifier-reconstructable
- crypto-agnostic
- compatible with replay verification
- compatible with the PQC / crypto agility guardrail

Option A must not invent missing fields.

Option A may include only fields that have:

- explicit runtime source
- explicit canonical structure
- explicit verifier reconstruction path

---

## NON-NEGOTIABLE INVARIANTS

Both Option B and Option A MUST preserve:

- determinism
- canonical equivalence
- exact replay verification
- fail-closed behavior
- Phase 7 stable behavior unless intentionally changed and fully re-verified
- crypto agility
- PQC readiness
- verifier reconstruction from recorded payload only

No implementation path may violate these invariants.

---

## ROLLBACK TRIGGERS

Implementation MUST stop and fall back from Option B to Option A if any of the following occurs:

1. A required Phase 8 field has no deterministic runtime source.
2. A required Phase 8 field can only be produced through inferred, hidden, or runtime-only data.
3. Receipt canonical construction cannot remain exactly verifier-reconstructable.
4. Boundary replay diverges from recorded receipt or ledger payload.
5. Phase 8 would require algorithm-specific cryptographic behavior.
6. Phase 8 would violate the crypto agility / PQC guardrail.
7. The sequence_id dependency cannot be resolved safely at the required insertion point.
8. Option B would require unsafe restructuring of already verified Phase 7 behavior.
9. Option B cannot be implemented without introducing partially defined canonical fields.
10. Any required Phase 8 structure lacks a locked derivation rule.

If any rollback trigger is hit:

- stop implementation immediately
- do not patch by intuition
- do not invent missing structure
- revert to Option A planning

---

## SEQUENCE_ID CONFLICT (LOCKED NOTE)

Current runtime analysis identified a timing conflict involving:

- required Phase 8 use of `sequence_id`
- current Phase 7 generation of `sequence_id` within frame continuity evaluation

This conflict is unresolved at strategy-lock time.

No collaborator may silently resolve this conflict by assumption.

Any resolution must preserve:

- determinism
- replay parity
- canonical equivalence
- boundary semantics

If safe resolution is not proven, Option B must fall back to Option A.

---

## MISSING FIELD RULE

The following Phase 8 fields are currently treated as unresolved unless and until their source and derivation are explicitly locked:

- signal_profile
- visible_alternatives_profile
- risk_frame_profile
- decision_space_version

No collaborator may invent, approximate, infer, or silently default these fields.

A field is not implementation-ready until all of the following are true:

- source is known
- canonical format is defined
- insertion timing is known
- receipt inclusion rule is defined
- verifier reconstruction rule is defined

---

## IMPLEMENTATION FREEZE LINE

No Phase 8 implementation may proceed beyond the Option A fallback floor unless:

- Option B field sources are proven
- canonical structures are locked
- verifier reconstruction is defined
- rollback triggers remain unhit

No collaborator may treat Option B as partially authorized.

Option B is all-or-fallback.

---

## CHANGE CONTROL RULE

If future work changes:

- Option B scope
- Option A fallback floor
- rollback triggers
- non-negotiable invariants

then this document must be updated and committed before implementation continues.

No collaborator may change Phase 8 strategy by conversation alone.

---

## RELATION TO OTHER AUTHORITATIVE DOCS

This strategy document is subordinate to and constrained by:

- docs/CURRENT_IMPLEMENTATION_STATE.md
- docs/PHASE8_PHASE9_SPEC.md
- docs/PHASE10_EXECUTION_INTEGRITY_SPEC.md
- docs/CRYPTO_AGILITY_PQC_GUARDRAIL.md

If any implementation idea conflicts with those documents, the implementation idea is invalid until the docs are explicitly updated.

---

## FINAL RULE

This is the implementation control point for Phase 8.

Preferred path:

    Option B

Fallback floor:

    Option A

If Option B cannot be completed safely and deterministically, implementation must stop and fall back without improvisation.
