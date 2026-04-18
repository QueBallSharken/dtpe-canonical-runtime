# NEXT IMPLEMENTATION TARGET

## PURPOSE

This document defines the exact next repository-authoritative target for future work.

---

## CURRENT CONFIRMED BASELINE

The committed runtime surface is beyond a Phase 5-only baseline.

The committed repository already includes:

- temporal invariant handling
- frame continuity handling
- bounded `signal_profile` construction
- bounded `decision_space` construction
- continuity-related receipt fields
- bounded `evaluator_trace`-related receipt binding
- bounded `evaluator_trace`-related verifier validation
- bounded `continuation_disposition` handling inside `frame_continuity_result`

The immediate priority is no longer to discover whether later runtime structures exist.
The immediate priority is to keep repository-authoritative documentation aligned with the committed runtime surface.

---

## CORE INVARIANT

verify without trusting the runtime that generated it

All future work must preserve this property.

---

## EXACT NEXT TARGET

The next repository-authoritative target is:

- complete the remaining repository-authoritative documentation alignment for the current committed bounded Phase 9 slices
- explicitly preserve the current bounded Phase 8 structure without silent expansion
- explicitly preserve the current bounded Phase 9 classification without broadening it by implication
- only after that alignment is complete, define the next bounded implementation target explicitly from repo truth

---

## REQUIRED SEQUENCE

### Step 1
Align implementation-state and roadmap documents with the committed runtime surface.

### Step 2
Align architecture-positioning documents so DTPE, IAL, SPECTRE, GDP bridge positioning, and SPECTRE-FST use one consistent repository-authoritative description.

### Step 3
Preserve the distinction between:

- committed runtime surface
- bounded design lock
- future direction
- active trike-model architecture direction
- future-only Sentinel direction

### Step 4
Only after those documents align, define the next bounded implementation target.

---

## MUST NOT DO IN THE NEXT CYCLE

The next cycle must not:

- describe the repository as Phase 5 only
- describe Phase 7 as absent
- describe Phase 9 as absent
- treat the bounded Phase 7 `continuation_disposition` change as Phase 8 scope expansion
- introduce new Phase 8 fields by implication
- begin Phase 10 runtime work
- introduce a `SPECTRE_SENTINEL` runtime surface
- treat planning text as implementation authority

---

## PQC / CRYPTO-AGILITY GUARDRAIL

All repository-state and planning updates must preserve DTPE's crypto-agility posture.

Nothing in this document authorizes:

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

---

## DEFINITION OF DONE

This target is complete only when:

- implementation-state docs match the committed runtime surface
- roadmap docs match the same bounded baseline
- architecture-positioning docs match the same bounded baseline
- no repository-authoritative source doc uses contradictory Phase 7 / 8 / 9 wording
- the next bounded implementation target can be stated without relying on stale planning text

END OF FILE
