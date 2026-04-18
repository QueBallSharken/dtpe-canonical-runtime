# SPECTRE-FST MINIMAL RECEIPT EXAMPLE SET

## STATUS

This document defines a bounded example set for the minimal SPECTRE-FST receipt schema.

It is architecture-facing only.

It does not claim runtime emission already exists.

---

## 1. PURPOSE

The minimal receipt schema is easier to interpret if the repository also contains bounded example shapes.

This document provides those example shapes.

---

## 2. EXAMPLE RULE

The examples in this document are shape examples only.

They do not claim runtime implementation.
They do not claim real evaluation already occurred.
They do not broaden first-target scope.

---

## 3. EXAMPLE: PARTIAL

- fst_profile_id = spectre_fst_minimal_v1
- fst_profile_version = 1.0
- fst_rule_profile_id = spectre_fst_first_target_rules_v1
- stress_scenario_id = fst_first_target_scenario_001
- stress_category = boundary_continuity_stress
- fst_result = PARTIAL
- fst_findings = ["local refusal boundary remained live"]
- fst_gaps = ["system-wide refusal continuity not proven under in-flight authority change"]
- fst_contradictions = []

---

## 4. EXAMPLE: UNVERIFIABLE

- fst_profile_id = spectre_fst_minimal_v1
- fst_profile_version = 1.0
- fst_rule_profile_id = spectre_fst_first_target_rules_v1
- stress_scenario_id = fst_first_target_scenario_001
- stress_category = proof_continuity_stress
- fst_result = UNVERIFIABLE
- fst_findings = []
- fst_gaps = ["receipt or trace evidence insufficient to sustain stronger continuity claim"]
- fst_contradictions = []

---

## 5. EXAMPLE: CONTRADICTION_EXPOSED

- fst_profile_id = spectre_fst_minimal_v1
- fst_profile_version = 1.0
- fst_rule_profile_id = spectre_fst_first_target_rules_v1
- stress_scenario_id = fst_first_target_scenario_001
- stress_category = fail_closed_discipline_stress
- fst_result = CONTRADICTION_EXPOSED
- fst_findings = []
- fst_gaps = []
- fst_contradictions = ["stronger continuity claim exceeded what the bounded scenario evidence supports"]

---

## 6. FINAL RULE

These examples exist to clarify shape and interpretation.

They must not be mistaken for proof of runtime maturity.

END OF FILE
