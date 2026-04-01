# PHASE 9B - EVALUATOR RULE SOURCE SPEC

## STATUS

- Repo-authoritative rule source definition
- Documentation only
- No runtime implementation authorized by this document

---

## PURPOSE

This document defines the canonical evaluator rule source required for Phase 9B.

Its purpose is to make evaluator rule identity explicit, deterministic, and verifier-reconstructable.

This document defines the canonical rule artifact that Phase 9B will later hash and bind.

---

## CORE RULE

Evaluator rule identity must not be inferred from runtime behavior alone.

Evaluator rule identity must be defined by a canonical evaluator_rule_profile artifact that is:

- explicit
- deterministic
- canonically serializable
- hashable with sha256_hex_str(canonical_json(...))
- reconstructable by verifier without hidden runtime context

---

## CANONICAL ARTIFACT NAME

The canonical rule artifact is:

evaluator_rule_profile

---

## CURRENT REPO-ALIGNED PROFILE

evaluator_rule_profile = {
  "evaluator_rule_profile_id": "spectre_boundary_rules_v1",
  "evaluator_rule_version": "1.0"
}

---

## DERIVATION RULE

evaluator_rule_hash = sha256_hex_str(canonical_json(evaluator_rule_profile))

---

## FINAL RULE

No evaluator_rule_hash is valid unless it is derived from evaluator_rule_profile exactly.