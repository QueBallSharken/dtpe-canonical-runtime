# SPECTRE-SENTINEL CANONICAL OBJECT MODEL

## Status

This artifact defines the implementation-facing conceptual object model for future Sentinel integration through IAL and SPECTRE.

It is intentionally bounded.

It does not claim that the object model is already normalized in runtime.
It does not authorize runtime work by implication.
It does not replace existing IAL ownership rules.

---

## 1. Purpose

This artifact defines the conceptual semantic object Sentinel must emit or help form in a future integration profile.

It exists to state:
- what semantic object Sentinel must emit or help form
- how that object maps into IAL
- what SPECTRE evaluates
- what later DTPE evidence integration would require

---

## 2. Core Rule

Sentinel must not pass downstream only:
- a score
- a label
- an alert
- a detector verdict

Sentinel must emit or help form:
- a canonical semantic object suitable for IAL ownership

---

## 3. Conceptual Object Role

The object is:
- semantic
- canonical
- replay-sufficient
- admissibility-relevant
- mutation-relevant
- integrity-carrying
- suitable for boundary evaluation by SPECTRE

It is not merely:
- a detector output
- a convenience label
- a UI-facing annotation

---

## 4. Minimal Conceptual Fields

The conceptual object should contain at minimum:
- object identity
- semantic subject or target
- semantic findings
- semantic predicates asserted
- provenance or source of analysis
- scope of applicability
- admissibility-relevant conditions
- mutation-boundary relevance
- canonical structure suitable for IAL ownership
- integrity / crypto binding metadata compatible with repo direction
- replay-sufficient structure

---

## 5. IAL Mapping

IAL conceptually owns:
- canonical semantic representation
- semantic field definitions
- canonical normalization rules
- object identity rules
- admissibility-relevant schema structure

Sentinel should therefore produce or help produce an object that is:
- IAL-native
or
- transformable into IAL-native canonical form without semantic loss

---

## 6. SPECTRE Mapping

SPECTRE evaluates:
- the IAL-defined canonical semantic object
- at the execution / mutation boundary
- against still-governing admissibility predicates

The object is therefore an input to SPECTRE evaluation, not a substitute for it.

---

## 7. DTPE Mapping

Later DTPE integration would require:
- persistent object identity
- canonical integrity carriage
- object-to-boundary-evaluation linkage
- receipt reference rules
- ledger reference rules
- offline verifier reconstruction rules

Without those, verifier completeness must not be claimed.

---

## 8. Safety Rules

This object model must not be used to imply:
- Sentinel runtime authorization by implication
- completed runtime integration
- BBIS completion
- replacement of SPECTRE
- replacement of DTPE evidence surfaces

---

## 9. Direct Model Rule

The direct model rule is:

Sentinel should emit or help form a canonical semantic artifact that belongs conceptually to IAL, is evaluated by SPECTRE at the execution boundary, and may later be carried into DTPE receipt / ledger / verifier paths only if those surfaces are explicitly extended.