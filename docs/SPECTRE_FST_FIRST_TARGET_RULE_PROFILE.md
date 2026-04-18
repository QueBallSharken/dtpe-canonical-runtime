# SPECTRE-FST FIRST TARGET RULE PROFILE

## STATUS

This document defines the minimal bounded rule profile for the first SPECTRE-FST target.

It is architecture-facing only.

It does not authorize runtime implementation by itself.
It does not broaden DTPE runtime state.
It does not replace GDP evaluation.
It does not redefine BBIS.

---

## 1. PURPOSE

The first bounded target must not rely on undefined evaluator meaning.

This document defines the rule profile that governs first-target interpretation.

---

## 2. RULE PROFILE ID

`spectre_fst_first_target_rules_v1`

## 3. RULE PROFILE VERSION

`1.0`

---

## 4. RULE PROFILE SCOPE

This profile governs only:

- the first bounded target scenario
- the first bounded stress category selection
- the bounded primary result interpretation
- the bounded findings / gaps / contradictions interpretation

It does not govern future broader FST categories automatically.

---

## 5. RULES

### 5.1 Bounded Category Rule
The evaluator must use only explicitly declared stress categories.

### 5.2 Single Primary Result Rule
Exactly one bounded primary result must be emitted.

### 5.3 Scope Discipline Rule
No stronger claim may be inferred than the scenario evidence supports.

### 5.4 Determinism Rule
The same canonical scenario under the same rule profile must yield the same result.

### 5.5 Receipt Rule
The result must be expressible in the minimal receipt schema.

### 5.6 Downgrade Rule
If stronger continuity cannot be sustained, the result must downgrade rather than preserve the stronger claim.

---

## 6. ALLOWED PRIMARY RESULTS

Allowed result set is governed by:

- docs/SPECTRE_FST_RESULT_VOCABULARY.md

For the first target, safe outcomes are expected to come from:

- PARTIAL
- UNVERIFIABLE
- CONTRADICTION_EXPOSED

---

## 7. INTERPRETATION RULE

The rule profile interprets:

- findings as what held
- gaps as what blocked a stronger claim
- contradictions as what materially conflicts with the stronger claim

These must remain distinct.

---

## 8. NON-CLAIMS

This rule profile does not claim:

- full evaluator maturity
- full category coverage
- completed selector sophistication
- completed upgrade analysis
- broad system-wide stress authority

It is first-target-only.

---

## 9. FINAL RULE

The first bounded FST target must be governed by an explicit rule profile.

Without an explicit rule profile, the result is descriptive only.

END OF FILE
