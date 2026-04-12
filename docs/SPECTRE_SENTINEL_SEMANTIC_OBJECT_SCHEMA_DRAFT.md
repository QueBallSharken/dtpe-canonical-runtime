# SPECTRE-SENTINEL SEMANTIC OBJECT SCHEMA DRAFT

## Status

This artifact defines a conceptual draft schema for the canonical semantic object Sentinel must emit or help form for future integration through IAL and SPECTRE.

It is a draft object model only.

It does not imply current runtime normalization.
It does not replace IAL ownership.
It does not authorize implementation by implication.

---

## 1. Purpose

This artifact provides a conceptual schema draft so future collaboration can discuss the same object shape from the repo.

---

## 2. Conceptual Schema Fields

### Required core fields
- object_id
- object_type
- semantic_subject
- semantic_target
- semantic_findings
- asserted_predicates
- provenance
- applicability_scope
- admissibility_relevance
- mutation_boundary_relevance
- canonical_form_version
- integrity_binding
- replay_visibility

### Optional supporting fields
- supporting_context
- detector_metadata
- confidence_metadata
- additional_annotations

Optional fields must not replace the governing semantic content.

---

## 3. Ownership Rule

This object must conceptually belong to:
- IAL as the canonical semantic artifact layer

Sentinel may:
- emit it
- help form it
- enrich it

Sentinel must not be treated as the long-term owner of canonical semantic object meaning.

---

## 4. Boundary Rule

This object becomes governance-relevant only when:
- carried in canonical form
- evaluated by SPECTRE at the execution / mutation boundary

---

## 5. Evidence Rule

If later carried into DTPE evidence surfaces, the object would require:
- stable identity
- stable canonical representation
- integrity binding
- replay-sufficient visibility

---

## 6. Collaboration Rule

This schema draft exists so future collaborators can reference a repo-hosted conceptual object instead of relying on thread history.

---

## 7. Direct Rule

The direct rule is:

Sentinel should emit or help form a canonical semantic object that IAL can own, SPECTRE can evaluate, and DTPE can later reference if evidence surfaces are explicitly extended.