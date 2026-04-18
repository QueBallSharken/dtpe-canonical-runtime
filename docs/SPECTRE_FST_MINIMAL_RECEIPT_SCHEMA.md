# SPECTRE-FST MINIMAL RECEIPT SCHEMA

## STATUS

This document defines the minimum bounded receipt schema for SPECTRE-FST.

It is architecture-facing only.

It does not authorize runtime implementation by itself.
It does not claim completed DTPE receipt integration.
It does not replace DTPE receipts.
It does not replace GDP bridge outputs.
It does not redefine BBIS.

---

## 1. PURPOSE

SPECTRE-FST is not meaningful as a bounded evaluator unless its results can be emitted in a stable, interpretable, receipt-bearing form.

This document defines the smallest receipt shape that makes SPECTRE-FST outputs mechanically usable.

---

## 2. DIRECT RULE

Every SPECTRE-FST evaluation must emit exactly one bounded primary result in a receipt structure that is stable enough to support:

- interpretation
- replay
- bounded comparison
- later hardening discussion
- claim discipline

A result without receipt structure is not a meaningful bounded FST output.

---

## 3. REQUIRED FIELDS

A minimal SPECTRE-FST receipt must contain all of the following required fields:

- fst_profile_id
- fst_profile_version
- fst_rule_profile_id
- stress_scenario_id
- stress_category
- fst_result
- fst_findings
- fst_gaps
- fst_contradictions

If any required field is absent, the result is not a conformant minimal SPECTRE-FST receipt.

---

## 4. FIELD DEFINITIONS

### 4.1 fst_profile_id
Identifies the SPECTRE-FST profile under which the evaluation was performed.

### 4.2 fst_profile_version
Identifies the version of the FST profile.

### 4.3 fst_rule_profile_id
Identifies the bounded evaluator rule profile used for this result.

### 4.4 stress_scenario_id
Identifies the scenario or case being evaluated.

### 4.5 stress_category
Identifies the bounded stress category.

### 4.6 fst_result
Identifies the bounded primary result.

Allowed values are governed by:
- docs/SPECTRE_FST_RESULT_VOCABULARY.md

### 4.7 fst_findings
A bounded list of statements describing what held or was positively observed.

### 4.8 fst_gaps
A bounded list of statements describing what could not be supported strongly enough for a stronger claim.

### 4.9 fst_contradictions
A bounded list of materially disqualifying conflicts between the claim and the evaluated structure or evidence.

---

## 5. OPTIONAL FIELDS

A minimal receipt may optionally include:

- fst_rule_hash
- stress_input_hash
- fst_timestamp
- target_weak_point
- upgrade_direction
- receipt_notes

These fields are useful, but not required for the minimum bounded receipt shape.

---

## 6. TYPE SHAPE

The minimum type expectations are:

- fst_profile_id = string
- fst_profile_version = string
- fst_rule_profile_id = string
- stress_scenario_id = string
- stress_category = string
- fst_result = string
- fst_findings = array of strings
- fst_gaps = array of strings
- fst_contradictions = array of strings

Optional fields may be strings or arrays where appropriate, but the minimum shape above must remain stable.

---

## 7. INTERPRETATION RULES

### 7.1 Primary Result Rule
fst_result is the primary bounded classification.

Findings, gaps, and contradictions do not replace it.

### 7.2 Findings Rule
fst_findings state what held strongly enough to be positively asserted.

Findings must not silently imply stronger scope than the primary result allows.

### 7.3 Gaps Rule
fst_gaps state what prevented a stronger bounded result.

Gaps must not be treated as findings.

### 7.4 Contradictions Rule
fst_contradictions state what materially conflicts with the evaluated claim.

If contradictions are present and materially disqualifying, the primary result must remain consistent with that fact.

### 7.5 Empty Array Rule
If no findings, gaps, or contradictions are present in a given category, the relevant field must still be present as an empty array.

Required fields must not disappear merely because their contents are empty.

---

## 8. RELATION TO RESULT VOCABULARY

The receipt schema does not define result meaning by itself.

Result meaning is governed by:
- docs/SPECTRE_FST_RESULT_VOCABULARY.md

This receipt schema only defines how the result is carried.

---

## 9. RELATION TO SELECTOR VS EVALUATOR SPLIT

This minimal receipt is evaluator-facing.

It records the bounded output of evaluation.

It does not require selector internals to be present in the minimum schema.

A later, richer receipt may include selector-related context, but the minimum receipt does not require it.

---

## 10. MINIMUM EXAMPLE SHAPE

A minimal conformant SPECTRE-FST receipt contains:

- fst_profile_id = spectre_fst_minimal_v1
- fst_profile_version = 1.0
- fst_rule_profile_id = spectre_fst_rules_v1
- stress_scenario_id = scenario_001
- stress_category = boundary_continuity_stress
- fst_result = PARTIAL
- fst_findings = ["local refusal boundary remained live"]
- fst_gaps = ["system-wide refusal continuity not proven under in-flight authority change"]
- fst_contradictions = []

This is only an example of shape.
It is not a canonical claim about runtime implementation.

---

## 11. NON-CLAIMS

This minimal receipt schema does not claim:

- completed runtime receipt emission already exists
- completed DTPE receipt integration already exists
- completed GDP bridge integration already exists
- completed selector trace capture already exists
- completed upgrade analysis output already exists
- that minimal receipt shape alone is sufficient for BBIS conformance

This is the minimum bounded FST receipt shape only.

---

## 12. FINAL RULE

A minimal SPECTRE-FST result is receipt-bearing only if it contains all required fields:

- fst_profile_id
- fst_profile_version
- fst_rule_profile_id
- stress_scenario_id
- stress_category
- fst_result
- fst_findings
- fst_gaps
- fst_contradictions

Anything less is still informal analysis, not a bounded receipt schema.

END OF FILE
