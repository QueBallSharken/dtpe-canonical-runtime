# SPECTRE-SENTINEL DOCS ALIGNMENT PLAN

## Status

This artifact defines the required docs-alignment plan for future Sentinel integration.

It is mandatory planning, not optional cleanup.

It does not itself change repo docs.
It defines what must be inspected and normalized before normative Sentinel wording is safe.

---

## 1. Purpose

This artifact defines the explicit docs-alignment plan required before Sentinel future-integration wording can be treated as normative.

---

## 2. Minimum Files To Inspect

At minimum, inspect:
- `README.md`
- `docs/ARCHITECTURE_OVERVIEW.md`
- `docs/EXECUTION_INTEGRITY_MODEL.md`
- `docs/BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`
- `docs/IAL_SPEC.md`

Also inspect any other current public docs that:
- describe DTPE / IAL / SPECTRE responsibilities
- imply runtime authorization
- describe semantic artifacts
- describe mutation authority
- describe verifier / receipt / replay semantics

---

## 3. Contradictions To Resolve

At minimum, resolve contradictions around:
- whether Sentinel is current runtime or future integration only
- whether IAL implies runtime authorization
- whether SPECTRE remains the execution / mutation-bound evaluator
- whether BBIS is being collapsed into ingress detection
- whether DTPE evidence responsibilities remain distinct
- whether public wording implies completion rather than proposal

---

## 4. Wording To Normalize

Normalize wording so that:
- Sentinel = future integration profile
- IAL = canonical semantic artifact layer
- SPECTRE = execution / mutation-bound evaluation layer
- DTPE = canonical receipt / ledger / offline verifier evidence path
- BBIS = continuity / conformance requirement across the full mutation path

---

## 5. Naming Mismatches To Address

At minimum, address:
- any visible mismatch around IAL naming
- any wording that treats semantic ingress as execution-bound enforcement
- any wording that implies Sentinel already exists as a current normalized public architecture layer

---

## 6. Completion Rule

Docs alignment is complete only when:
- contradictory wording is resolved
- Sentinel future-only posture is explicit
- DTPE / IAL / SPECTRE responsibility boundaries are consistent
- BBIS is preserved as the continuity requirement
- no public doc implies runtime authorization by implication

---

## 7. Direct Rule

The direct docs-alignment rule is:

Sentinel future-integration wording is not safe to publish as normative until the current public docs are inspected and normalized against the constrained DTPE / IAL / SPECTRE architecture mapping.