# SPECTRE-SENTINEL CURRENT PUBLIC REPO POSITION

## Status

This artifact states the bounded current-public-repo position that must govern all Sentinel future-integration work.

It is intentionally conservative.

It does not authorize runtime expansion by implication.
It does not normalize Sentinel into the current public runtime surface.
It does not replace DTPE / IAL / SPECTRE.
It does not claim BBIS is complete.

This artifact must be treated as a repo-facing control statement pending direct verification against current public repo docs.

---

## 1. Purpose

This artifact defines the current public-repo posture that Sentinel future-integration work must respect.

It exists to state:
- what is already public
- what is already authorized
- what is explicitly not authorized by implication
- what architectural role boundaries must remain intact

---

## 2. Current Public Architecture Position

The required working public position is:

- DTPE / IAL / SPECTRE is the public architecture triad
- IAL is the canonical semantic artifact layer
- SPECTRE evaluates IAL-defined semantic artifacts at the execution boundary
- DTPE is the canonical receipt / ledger / offline verifier evidence path
- boundary integrity requires that no irreversible mutation occur except through explicit mutation authority evaluating a still-governing admissibility predicate

---

## 3. What Is Already Public

The public architecture surface is treated as already exposing:
- DTPE
- IAL
- SPECTRE

These are the current public architectural anchors.

---

## 4. What Is Already Authorized

The current public repo position is treated as authorizing:
- IAL-native semantic artifact ownership
- SPECTRE execution-bound evaluation of IAL-defined artifacts
- DTPE evidence and offline verification posture
- mutation-bound admissibility evaluation at explicit mutation authority

---

## 5. What Is Not Authorized by Implication

The following are explicitly not authorized by implication:

- Sentinel runtime work from IAL positioning alone
- Sentinel as a normalized public runtime layer
- Sentinel as a replacement for SPECTRE
- Sentinel as a replacement for DTPE evidence paths
- Sentinel as a substitute for BBIS
- Sentinel as a completed architecture layer today

---

## 6. Sentinel Safety Position

Until BBIS is fully implemented and stabilized, Sentinel must be treated as:
- future integration only
- subordinate to DTPE / IAL / SPECTRE
- front-side semantic / interception layer only
- non-normative for current public runtime expansion
- non-authorizing by implication

---

## 7. Public Safety Rule

Any future Sentinel wording must preserve:
- DTPE / IAL / SPECTRE architectural priority
- IAL semantic object ownership
- SPECTRE execution-bound evaluation role
- DTPE receipt / ledger / verifier role
- BBIS as continuity requirement across the full mutation path

---

## 8. Verification Requirement

This position must be checked against at minimum:
- `README.md`
- `docs/ARCHITECTURE_OVERVIEW.md`
- `docs/EXECUTION_INTEGRITY_MODEL.md`
- `docs/BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`
- `docs/IAL_SPEC.md`

No stronger normative claim should be made until those checks are complete.

---

## 9. Direct Rule

The direct current-public-repo rule is:

Sentinel is not a currently normalized public runtime layer.
Sentinel is future integration only.
IAL does not authorize Sentinel runtime work by implication.
SPECTRE remains the execution / mutation-bound evaluator.
DTPE remains the evidence path.
BBIS remains the continuity requirement.