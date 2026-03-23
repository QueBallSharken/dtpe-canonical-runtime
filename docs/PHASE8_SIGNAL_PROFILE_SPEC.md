# PHASE 8 — SIGNAL PROFILE SPEC (LOCKED)

## STATUS

Design specification locked.
No runtime implementation is authorized by this document.

This document defines the canonical structure, source mapping, and reconstruction rules for:

    signal_profile

This specification is required before any Phase 8 implementation.

---

## PURPOSE

`signal_profile` captures the evaluated decision signals produced by boundary guard execution.

It provides a deterministic, canonical, and replayable representation of:

- admissibility signals
- stability signals
- temporal signals
- continuity signals

This structure must be:

- fully derived from existing runtime outputs
- free of inference or approximation
- reconstructable by verifier from receipt payload only

---

## PHASE PLACEMENT

`signal_profile` belongs to:

    Phase 8B — Decision-Space Resolution

It MUST NOT be constructed in Phase 8A.

Reason:

All required inputs are produced only during boundary guard evaluation.

---

## CANONICAL STRUCTURE

The canonical structure of `signal_profile` is:

{
  "state_admissibility": {
    "ok": bool,
    "reason": str
  },
  "system_stability": {
    "ok": bool,
    "reason": str
  },
  "temporal_invariant": {
    "ok": bool,
    "reason": str
  },
  "frame_continuity": {
    "ok": bool,
    "reason": str,
    "continuity_mode": str,
    "temporal_continuity_ok": bool
  },
  "signal_profile_version": str
}

---

## SOURCE MAPPING (AUTHORITATIVE)

All fields MUST be derived exactly as follows:

state_admissibility:

- ok ← state_result["ok"]
- reason ← state_result["reason"]

system_stability:

- ok ← stability_result["ok"]
- reason ← stability_result["reason"]

temporal_invariant:

- ok ← temporal_result["ok"]
- reason ← temporal_result["reason"]

frame_continuity:

- ok ← frame_continuity_result["ok"]
- reason ← frame_continuity_result["reason"]
- continuity_mode ← frame_continuity_result["continuity_mode"]
- temporal_continuity_ok ← frame_continuity_result["temporal_continuity_ok"]

signal_profile_version:

- fixed constant string (e.g. "v1")

---

## DERIVATION RULES

All values must be:

- directly copied from runtime guard outputs
- not transformed beyond structural normalization
- not enriched with inferred metadata
- not reordered outside canonical JSON rules

No additional fields may be added.

---

## PROHIBITED CONTENT

`signal_profile` MUST NOT include:

- raw guard objects
- policy internals
- authority internals
- timestamps not already required by signals
- confidence scores
- weighted values
- derived or inferred judgments
- cryptographic data
- algorithm-specific fields

---

## CANONICALIZATION RULE

`signal_profile` MUST:

- be included in receipt_material before canonical_json(...)
- follow deterministic key ordering via canonical_json
- be identical across replay

No conditional omission is allowed once introduced.

---

## VERIFIER RECONSTRUCTION REQUIREMENT

Verifier MUST:

1. reconstruct `signal_profile` from receipt payload
2. validate structure integrity
3. include it in canonical_json reconstruction
4. fail on any mismatch

Verifier MUST NOT:

- infer missing fields
- recompute signals independently
- rely on runtime guard execution

---

## VERSIONING RULE

`signal_profile_version` MUST:

- be present
- be a fixed constant per version
- change only via committed spec update

No implicit versioning is allowed.

---

## FAILURE CONDITIONS

Implementation must stop if:

- any source field is missing at runtime
- any field cannot be deterministically mapped
- any field cannot be reconstructed by verifier
- any structure diverges during replay
- any additional field is required beyond this spec

If any failure condition occurs:

- do not patch
- do not approximate
- revert to Phase 8 strategy fallback rules

---

## RELATION TO OTHER DOCS

This spec is constrained by:

- docs/PHASE8_PHASE9_SPEC.md
- docs/PHASE8_TWO_STAGE_INTERPRETATION.md
- docs/PHASE8_DECISION_SPACE_IMPLEMENTATION_STRATEGY.md
- docs/CRYPTO_AGILITY_PQC_GUARDRAIL.md

If any conflict exists, implementation must stop until resolved in documentation.

---

## FINAL RULE

`signal_profile` is a canonical, deterministic projection of boundary signals.

It must reflect exactly what the system evaluated, not what the system might infer.
