# PHASE 9B - EVALUATOR RULE SOURCE SPEC (PROPOSED)

## STATUS

- Phase 9B: DEFINITION DRAFT
- Documentation only
- No runtime implementation authorized by this document

---

## PURPOSE

This document defines the canonical evaluator rule source required before Phase 9B runtime implementation can begin.

Its purpose is to resolve the missing rule-identity problem by defining a deterministic, replay-reconstructable evaluator rule artifact.

This document does not implement Phase 9B.
This document defines the artifact that Phase 9B will later hash, record, and verify.

---

## CORE RULE

Evaluator rule identity must not be inferred from runtime behavior alone.

Evaluator rule identity must be defined by a canonical evaluator rule artifact that is:

- explicit
- deterministic
- serializable with canonical_json(...)
- hashable with sha256_hex_str(...)
- reconstructable by verifier without hidden runtime context

---

## CANONICAL ARTIFACT

evaluator_rule_profile = {
  "evaluator_rule_profile_id": "spectre_boundary_rules_v1",
  "state_admissibility_rule": {
    "rule_id": "state_admissibility_v1",
    "required_inputs": [
      "canonical_current_state",
      "canonical_transition",
      "canonical_policy_state_hash",
      "execution_intent",
      "authority_hash",
      "crypto_profile"
    ],
    "success_condition": {
      "ok_field": "ok",
      "ok_value": true
    }
  },
  "system_stability_rule": {
    "rule_id": "system_stability_v1",
    "required_inputs": [
      "system_state",
      "canonical_transition"
    ],
    "success_condition": {
      "ok_field": "ok",
      "ok_value": true
    }
  },
  "temporal_invariant_rule": {
    "rule_id": "temporal_invariant_v1",
    "required_inputs": [
      "canonical_transition",
      "execution_time"
    ],
    "success_condition": {
      "ok_field": "ok",
      "ok_value": true
    }
  },
  "frame_continuity_rule": {
    "rule_id": "frame_continuity_v1",
    "required_inputs": [
      "canonical_policy_state_hash",
      "authority_hash",
      "execution_intent",
      "constraint_profile",
      "temporal_rule_profile",
      "execution_time",
      "prior_invariant_frame_hash",
      "prior_execution_time",
      "continuity_required",
      "transition_mode",
      "allowed_frame_transitions"
    ],
    "success_condition": {
      "continuity_mode_allowed_values": [
        "INITIAL",
        "EXACT",
        "AUTHORIZED_TRANSITION"
      ],
      "temporal_continuity_ok": true
    }
  },
  "boundary_composition_rule": {
    "allow_when_all_true": [
      "authority_ok",
      "state_ok",
      "stability_ok",
      "temporal_ok",
      "frame_continuity_ok",
      "temporal_continuity_ok"
    ],
    "allow_execution_state": "ALLOW",
    "refuse_execution_state": "REFUSED_NON_BINDING"
  },
  "evaluator_rule_version": "1.0"
}

---

## DERIVATION RULE

evaluator_rule_hash = sha256_hex_str(canonical_json(evaluator_rule_profile))

---

## FINAL RULE

No evaluator_rule_hash is valid unless it is derived from evaluator_rule_profile.
