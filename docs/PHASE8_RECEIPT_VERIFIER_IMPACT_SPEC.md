# PHASE 8 — RECEIPT / VERIFIER IMPACT SPEC (LOCKED)

## STATUS

Design specification locked.
No runtime implementation is authorized by this document.

This document defines the required receipt and verifier behavior if Phase 8 `decision_space` is introduced into runtime.

---

## PURPOSE

Phase 8 cannot be implemented safely unless:

- receipt construction is explicitly defined
- verifier reconstruction is explicitly defined
- canonical equivalence is preserved
- replay parity remains exact

This document locks those requirements before any code change.

---

## CURRENT BASELINE

Current runtime behavior already requires:

- `receipt_material` is built before `canonical_json(...)`
- `receipt_canonical` is derived from `receipt_material`
- `receipt_hash` is derived from `receipt_canonical`
- verifier reconstructs `receipt_material` and fails on mismatch
- replay verification must remain exact

Phase 8 must preserve all of that.

---

## RECEIPT IMPACT (LOCKED)

If `decision_space` is introduced into runtime, it MUST be added to:

- `receipt_material`
- final receipt payload
- ledger payload

It MUST be inserted before:

- `canonical_json(receipt_material)`
- `sha256_hex_str(receipt_canonical)`

No later mutation is allowed.

---

## RECEIPT INCLUSION RULE

Once Phase 8 `decision_space` is authorized as a receipt field:

- it MUST always be present
- it MUST be composition-complete
- it MUST NOT be conditionally omitted
- it MUST NOT contain deferred fields
- it MUST NOT contain unresolved fields

At current locked state, authorized `decision_space` may contain only:

- policy_hash
- authority_hash
- execution_intent
- constraint_profile
- signal_profile
- decision_space_version

It MUST NOT contain:

- visible_alternatives_profile
- risk_frame_profile
- sequence_id

---

## CANONICAL RULE

`decision_space` MUST participate in canonical equivalence exactly like other receipt fields.

That means:

- identical structure in receipt construction
- identical structure in verifier reconstruction
- deterministic canonical JSON ordering only
- no runtime-only fields
- no inferred fields
- no placeholder values

Any mismatch MUST fail verification.

---

## VERIFIER IMPACT (LOCKED)

Verifier MUST be updated to:

1. read `decision_space` from payload
2. validate that it is a JSON object
3. validate required subfields are present
4. validate excluded/deferred fields are absent
5. insert `decision_space` into reconstructed `receipt_material`
6. recompute `canonical_json(receipt_material)`
7. fail on any mismatch

Verifier MUST NOT:

- infer missing values
- regenerate deferred fields
- compute alternatives
- compute risk
- resolve sequence timing
- rely on hidden runtime state

---

## REQUIRED VERIFIER SUBFIELD VALIDATION

If `decision_space` is present, verifier must validate at minimum:

### Top-level fields
- policy_hash: str
- authority_hash: str
- execution_intent: str
- constraint_profile: str
- signal_profile: dict
- decision_space_version: str

### signal_profile fields
- state_admissibility: dict
- system_stability: dict
- temporal_invariant: dict
- frame_continuity: dict
- signal_profile_version: str

### Nested signal subfields

state_admissibility:
- ok: bool
- reason: str

system_stability:
- ok: bool
- reason: str

temporal_invariant:
- ok: bool
- reason: str

frame_continuity:
- ok: bool
- reason: str
- continuity_mode: str
- temporal_continuity_ok: bool

Any mismatch, missing field, or wrong type MUST fail verification.

---

## REPLAY RULE

Verifier replay MUST remain exact.

If boundary replay remains active after Phase 8 introduction, then Phase 8-related receipt fields must not cause replay divergence.

That means one of the following must be true before implementation:

1. Phase 8 `decision_space` is receipt/verifier-only and does not alter boundary decision logic yet
2. boundary replay path is explicitly updated to remain aligned with Phase 8 behavior

No Phase 8 implementation is allowed if replay parity would break.

---

## RECEIPT / VERIFIER CHANGE ORDER

Implementation order is locked as:

1. define `decision_space` composition
2. define receipt insertion rule
3. define verifier reconstruction rule
4. define verifier validation rule
5. only then implement runtime receipt field
6. only then allow decision logic to depend on Phase 8 structures

No direct runtime insertion is allowed before verifier path is defined.

---

## FAILURE CONDITIONS

Implementation MUST STOP if:

- `decision_space` cannot be inserted identically in receipt and verifier
- verifier cannot validate full structure deterministically
- replay parity would diverge
- deferred fields are required to satisfy structure
- any field requires inference or hidden runtime state
- canonical equivalence would break

If any failure condition occurs:

- do not patch
- do not partially implement
- revert to Phase 8 strategy rules

---

## RELATION TO OTHER DOCS

This spec is constrained by:

- docs/PHASE8_DECISION_SPACE_COMPOSITION_SPEC.md
- docs/PHASE8_SIGNAL_PROFILE_SPEC.md
- docs/PHASE8_VISIBLE_ALTERNATIVES_PROFILE_SPEC.md
- docs/PHASE8_RISK_FRAME_PROFILE_SPEC.md
- docs/PHASE8_TWO_STAGE_INTERPRETATION.md
- docs/PHASE8_DECISION_SPACE_IMPLEMENTATION_STRATEGY.md
- docs/CRYPTO_AGILITY_PQC_GUARDRAIL.md
- docs/CURRENT_IMPLEMENTATION_STATE.md

If any conflict exists, implementation must stop until resolved in committed documentation.

---

## FINAL RULE

Phase 8 is not implementation-ready until receipt construction and verifier reconstruction are guaranteed to remain exactly equivalent.

Receipt and verifier must evolve together or not at all.
