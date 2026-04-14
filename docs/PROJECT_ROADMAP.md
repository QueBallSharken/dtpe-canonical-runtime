# PROJECT ROADMAP

## PURPOSE

This document provides repository-authoritative orientation for contributors, reviewers, and future work.

It describes the committed system baseline, the current bounded phase position, and the next sequencing rule.

---

## PROJECT OVERVIEW

DTPE (Delegated Task Provenance Engine) is a deterministic governance runtime that produces cryptographically verifiable evidence showing how automated decisions are made.

The system generates canonical receipts and append-only ledger records that can be independently verified without trusting the runtime that produced them.

---

## CORE INVARIANT

verify without trusting the runtime that generated it

All architecture and implementation decisions must preserve this property.

---

## CURRENT COMMITTED BASELINE

The committed repository state is beyond a Phase 5-only baseline.

The committed runtime surface includes:

- execution-boundary admissibility handling
- temporal invariant handling
- frame continuity handling
- bounded `signal_profile` construction
- bounded `decision_space` construction
- continuity-related receipt fields
- bounded `evaluator_trace`-related receipt and verifier handling
- bounded `continuation_disposition` handling inside `frame_continuity_result`

Accordingly, this roadmap must not describe the current committed baseline as:

- Phase 5 only
- Phase 7 absent
- Phase 9 runtime absent

---

## CURRENT BOUNDED PHASE POSITION

Safe repository-authoritative phase position:

- Phase 7: implemented in the committed runtime surface
- Phase 8: partially implemented and verified in bounded slices
- Phase 9: bounded `evaluator_trace`-related runtime, receipt, verifier, and test surface is present in the committed runtime
- Phase 10: design-only / not implemented in runtime

This roadmap uses that bounded classification as the current baseline.

---

## DTPE / IAL / SPECTRE POSITION

DTPE remains the umbrella governance architecture.

Within DTPE:

- IAL is the semantic / invariant artifact layer
- SPECTRE is the execution-boundary evaluation subsystem
- SPECTRE_SENTINEL is future direction only and is not current runtime surface

The current committed runtime already includes `core/spectre` execution-boundary surfaces.
That does not authorize future-direction runtime expansion by naming alone.

---

## CURRENT ROADMAP PRIORITY

The immediate roadmap priority is completing the remaining repository-authoritative alignment for the current committed bounded Phase 9 slices.

That means:

1. keep implementation-state docs aligned with committed runtime
2. keep architecture-positioning docs aligned with committed runtime
3. keep bounded Phase 8 and bounded Phase 9 descriptions explicit
4. only then define the next bounded runtime implementation target explicitly from repo truth

---

## PHASE 8 RULE

The committed bounded Phase 8 structure must remain explicit and unchanged unless a new bounded Phase 8 expansion is separately authorized.

The bounded Phase 7 `continuation_disposition` change is not a Phase 8 structure change.

---

## PHASE 9 RULE

The committed repository already contains bounded `evaluator_trace`-related Phase 9 surface.

That surface must be described conservatively.

No further Phase 9 implementation planning should proceed on the basis of contradictory documentation.

---

## PHASE 10 RULE

Phase 10 remains future design / docs-only direction in the current repository.

Nothing in the current baseline authorizes:

- Phase 10 runtime work
- mutation-integrity runtime claims
- execution-hardening runtime claims beyond the currently committed surface

---

## PQC / CRYPTO-AGILITY GUARDRAIL

All roadmap and implementation planning must preserve DTPE's crypto-agility posture.

Nothing in roadmap alignment authorizes:

- implicit cryptographic behavior
- silent profile substitution
- hard-coding a single permanent algorithm assumption
- weakening replayability across profile transitions

All current and future alignment must remain compatible with:

- explicit crypto-profile identity
- policy-governed permitted profiles
- governed migration across profile generations
- independently reconstructable historical evidence
- post-quantum readiness

END OF FILE