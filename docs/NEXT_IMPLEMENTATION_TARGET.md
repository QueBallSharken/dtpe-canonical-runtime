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

- preserve the current bounded isolated FST category-expansion surface as committed repo truth
- complete the remaining thin isolated FST category expansions
- explicitly queue the remaining bounded isolated FST scenario work without implying it is already implemented
- only after that bounded isolated FST category work is complete, define the next bounded implementation target explicitly from repo truth

---

## CURRENT ISOLATED FST STOPPING POINT

The committed isolated FST continuity-stress surface currently has:

- `boundary_continuity_stress`: 4 scenarios
- `authority_continuity_stress`: 4 scenarios
- `temporal_continuity_stress`: 4 scenarios
- `state_continuity_stress`: 4 scenarios
- `path_continuity_stress`: 1 scenario
- `transport_continuity_stress`: 1 scenario

Current committed isolated FST scenario total:

- 18 scenarios

This is the current bounded stopping point.

---

## REQUIRED NEXT ISOLATED FST WORK

The next bounded isolated FST implementation work is:

- add 3 more `path_continuity_stress` scenarios
- add 3 more `transport_continuity_stress` scenarios

Total queued next-step isolated FST scenario work:

- 6 scenarios

When that work is complete, all currently implemented isolated FST categories will be at 4 scenarios each.

---

## REQUIRED SEQUENCE

### Step 1
Complete the remaining isolated FST thin-category expansions:

- path
- transport

### Step 2
Reconfirm the committed isolated FST category counts and total scenario count in repository-authoritative docs.

### Step 3
Only after that bounded isolated FST depth work is complete, define the next bounded implementation target.

---

## MUST NOT DO IN THE NEXT CYCLE

The next cycle must not:

- describe path expansion as already complete
- describe transport expansion as already complete
- imply DTPE integration work has already begun
- describe the isolated FST category-expansion surface as broader than what is committed
- introduce new categories by implication
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

- the remaining isolated FST thin categories are expanded
- the repo docs reflect the resulting committed category counts
- the repo docs reflect the resulting committed total scenario count
- the next bounded implementation target can be stated without relying on stale planning text

END OF FILE