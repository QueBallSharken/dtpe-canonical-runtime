# SPECTRE - SUBSYSTEM SPEC

## PURPOSE

This document defines SPECTRE as the execution-boundary evaluation subsystem inside DTPE.

It also records the relationship between SPECTRE, IAL, SPECTRE-FST, and parked future-only Sentinel material.

---

## WHAT SPECTRE IS

SPECTRE is the execution-boundary evaluation subsystem inside DTPE.

SPECTRE is responsible for determining whether admissibility holds at the boundary where DTPE currently makes binding execution decisions.

SPECTRE conceptually covers concerns such as:

- state admissibility
- temporal validity
- continuity across linked decisions
- bounded continuity-result output
- bounded decision-space evidence
- bounded evaluator-trace-related boundary evidence

---

## CURRENT COMMITTED RUNTIME POSITION

The current committed runtime already includes `core/spectre` execution-boundary surfaces.

The committed runtime surface includes:

- state admissibility handling
- temporal invariant handling
- frame continuity handling
- bounded `signal_profile` construction
- bounded `decision_space` construction
- bounded `evaluator_trace`-related runtime, receipt, verifier, and test surface

The committed Phase 7 continuity path also includes bounded `continuation_disposition` handling inside `frame_continuity_result`.

That continuity artifact is part of the Phase 7 continuity result.
It is not a Phase 8 structure change.

---

## WHAT SPECTRE OWNS CONCEPTUALLY

SPECTRE conceptually owns execution-boundary evaluation of canonical admissibility inputs, including:

- whether current state is admissible
- whether temporal validity holds
- whether frame continuity holds
- whether bounded decision-space evidence is internally valid
- whether bounded evaluator-trace evidence remains consistent with recorded canonical state

SPECTRE is boundary evaluation.

---

## WHAT SPECTRE DOES NOT OWN

SPECTRE does not own:

- semantic artifact definition as a whole
- global architecture identity
- mutation authority by naming alone
- Phase 10 runtime authority by implication
- Sentinel activation or runtime authority by implication

---

## RELATION TO IAL

IAL defines the canonical semantic artifacts that express what is being enforced.

SPECTRE evaluates those artifacts at the execution boundary.

IAL defines.
SPECTRE evaluates.

---

## RELATION TO SPECTRE-FST

SPECTRE-FST is the bounded fundamental stress evaluation direction attached to the current repository architecture framing.

Safe current wording is:

- SPECTRE evaluates admissibility at the execution boundary
- SPECTRE-FST stress-tests whether claimed governing truth survives bounded deformation classes
- SPECTRE-FST is architecture direction only unless separately implemented
- SPECTRE-FST does not replace SPECTRE boundary evaluation

---

## FUTURE-ONLY SENTINEL POSITION

Sentinel is parked future-only material in the current repository.

Safe current wording is:

- Sentinel remains future-only direction
- this document does not create a current Sentinel runtime surface
- Sentinel is not part of the active trike-model direction
- no Sentinel package, module, or enforcement layer is authorized merely because this document exists

See:

- `docs/SENTINEL_PARKED_POSITION.md`

---

## CURRENT BOUNDED PHASE POSITION

Within the current committed runtime surface:

- Phase 5-7 cover execution-boundary admissibility, temporal handling, and continuity
- Phase 8 covers bounded decision-space and signal-profile evidence
- Phase 9 includes bounded `evaluator_trace`-related runtime, receipt, verifier, and test surface
- Phase 10 remains future design / docs-only direction

This document does not broaden that bounded phase position.

---

## FINAL STATEMENT

SPECTRE is the DTPE execution-boundary evaluation subsystem.

SPECTRE evaluates admissibility at the boundary.
SPECTRE-FST is the current bounded stress-direction companion to that framing.
Sentinel remains parked future-only material and is not current runtime surface.

END OF FILE
