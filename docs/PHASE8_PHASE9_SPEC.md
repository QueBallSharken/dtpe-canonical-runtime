# PHASE 8 / PHASE 9 - IMPLEMENTATION SPEC (LOCKED)

## STATUS

- Phase 7: IMPLEMENTED IN THE COMMITTED RUNTIME SURFACE
- Phase 8: PARTIALLY IMPLEMENTED AND VERIFIED IN BOUNDED SLICES
- Phase 9: PARTIALLY ACTIVE IN COMMITTED RUNTIME SURFACE, BUT NOT YET DESCRIBED CONSISTENTLY ACROSS CURRENT REPO DOCS

Repository runtime does not remain at Phase 7 only.

Current runtime includes:

- committed Phase 7 continuity structures
- committed bounded Phase 8 structures
- committed evaluator_trace-related runtime, receipt, verifier, and test surface

No further Phase 9 implementation should proceed until the exact bounded Phase 9 runtime classification is stated consistently across the repo.

---

## PHASE 8 - DECISION-SPACE INTEGRITY

### PURPOSE

Ensure that the decision space itself is structurally valid before admissibility.

### CORE INVARIANT

Decision-space integrity must be:
- derived from canonical inputs
- recorded in receipt
- stored in ledger
- replayed by verifier
- enforced without inferred fields

### IMPLEMENTATION MODEL

Phase 8 is being implemented in bounded slices.

Current bounded slices are:

- Phase 8A - seed inputs / canonical decision inputs
- Phase 8B - signal_profile and bounded decision_space construction
- Phase 8C - verifier hardening for decision_space structure and forbidden fields

These slices are implemented and verified.

Phase 8 is NOT fully complete.

### CURRENT IMPLEMENTED CANONICAL STRUCTURE

decision_space = {
  "policy_hash": str,
  "authority_hash": str,
  "execution_intent": str,
  "constraint_profile": str,
  "signal_profile": {
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
  },
  "decision_space_version": str
}

### CURRENTLY IMPLEMENTED PHASE 8 FIELDS

Implemented and verified:
- policy_hash
- authority_hash
- execution_intent
- constraint_profile
- signal_profile
- decision_space_version

### DEFERRED / NOT IMPLEMENTED IN PHASE 8

The following Phase 8 fields are deferred and MUST NOT be treated as implemented:

- sequence_id inside decision_space
- visible_alternatives_profile
- risk_frame_profile

These fields are not authorized in the current bounded decision_space structure.

### CURRENT PHASE 8 RECEIPT / VERIFIER STATE

Implemented and verified:
- decision_space is inserted into receipt_material before canonical_json
- decision_space is included in final receipt payload
- decision_space is included in ledger payload
- verifier reconstructs decision_space
- verifier validates required decision_space fields
- verifier validates required nested signal_profile fields
- verifier rejects forbidden deferred fields
- replay parity remains exact

### PHASE 8 COMPLETION CONDITION

Phase 8 is only fully complete when all remaining authorized Phase 8 structures are either:

- implemented and verified, or
- explicitly deferred into committed bounded-slice documentation with no contradiction

Until then, Phase 8 remains partially implemented.

---

## PHASE 9 - EVALUATOR INTEGRITY

### PURPOSE

Ensure the evaluator itself is structurally trustworthy.

### CORE INVARIANT

Evaluator integrity must prove:
- evaluator identity consistency
- rule continuity
- replay fidelity

### CURRENT REPO REALITY

The committed runtime already includes evaluator-trace-related surface.

Visible committed runtime structures include:
- evaluator_trace construction in boundary
- evaluator_trace binding in receipt
- evaluator-trace-related verifier handling
- evaluator_rule_hash present in the committed runtime surface
- committed evaluator-trace-related test coverage

Accordingly, Phase 9 MUST NOT be described in this file as absent from the committed runtime.

### CURRENT DOCUMENTATION CONFLICT

Some current Phase 9 documents still state:

- Phase 9 is not implemented
- no Phase 9 runtime fields exist
- no Phase 9 receipt fields exist
- no Phase 9 verifier fields exist

Those statements are no longer safe as repo-authoritative summaries of the committed runtime surface.

### SAFE CURRENT DESCRIPTION

The safe repo-authoritative statement is:

- evaluator-trace-related runtime surface is present
- the exact bounded Phase 9 slice is not yet described consistently across current repo docs
- no additional Phase 9 implementation should proceed until that bounded classification is reconciled explicitly

### SEQUENCING RULE

Phase 9 documentation must be reconciled before further Phase 9 implementation planning continues.

Phase 9 must attach only to committed, verifier-reconstructable canonical state.

### PQC / CRYPTO GUARDRAIL

Any Phase 9 classification or future implementation must remain:

- crypto-agnostic
- profile-driven where cryptographic behavior exists
- verifier-reconstructable
- free of algorithm-specific branching
- compatible with post-quantum readiness

### FINAL RULE

No further Phase 9 implementation begins until this spec and the related Phase 9 docs are aligned with the actual committed repository state.

END OF FILE
