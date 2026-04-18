# SPECTRE-FST RESULT VOCABULARY

## STATUS

This document defines the bounded result vocabulary for SPECTRE-FST.

It is architecture-facing only.

It does not authorize runtime implementation by itself.
It does not broaden DTPE runtime state.
It does not replace GDP evaluation.
It does not redefine BBIS.

---

## 1. PURPOSE

SPECTRE-FST must not emit vague outcomes.

A bounded stress evaluator is meaningful only if its result classes are:
- explicit
- finite
- interpretable
- non-overlapping enough to support disciplined use
- strict enough to prevent stronger claims from being inferred from weaker results

This document defines that bounded result vocabulary.

---

## 2. DIRECT RULE

Every SPECTRE-FST evaluation must terminate in exactly one bounded primary result.

Additional findings, gaps, contradictions, and hardening notes may accompany that result.

They do not replace the result.

---

## 3. PRIMARY RESULT SET

The bounded primary result set is:

- STRONG
- PARTIAL
- FAIL
- UNVERIFIABLE
- CONTRADICTION_EXPOSED

No stronger result may be inferred from a weaker one.

---

## 4. RESULT DEFINITIONS

### 4.1 STRONG

STRONG means:

- the evaluated claim survived the relevant bounded stress category
- the required continuity or integrity condition held within the claimed scope
- no contradiction was found that defeats the claim
- evidence was sufficient for the bounded result being asserted

STRONG does not mean:
- universal correctness
- all categories passed
- system-wide closure beyond the stated scope
- BBIS completion
- mutation-bound governance completion

STRONG is always scope-bounded.

---

### 4.2 PARTIAL

PARTIAL means:

- some required continuity or integrity conditions held
- but one or more required elements did not survive strongly enough for a stronger result
- the evaluated claim remains supportable only in a narrower, explicitly bounded form

PARTIAL does not mean:
- informal success
- near-STRONG by vibes
- acceptable without qualification

PARTIAL requires explicit boundedness.

If the surviving scope cannot be stated clearly, the result should not remain PARTIAL.

---

### 4.3 FAIL

FAIL means:

- the evaluated claim did not survive the relevant stress category for the claimed scope
- a required continuity or integrity condition broke
- the stronger claim cannot honestly survive

FAIL does not require contradiction.
A claim may fail simply because the required continuity condition is absent or broken.

FAIL does not mean:
- the entire architecture is worthless
- every other category fails
- no bounded claim can ever survive

FAIL is category- and scope-specific unless explicitly aggregated at a higher level.

---

### 4.4 UNVERIFIABLE

UNVERIFIABLE means:

- the claim may have been made
- but the available evidence is insufficient to support a bounded strong or partial result
- replay, trace, receipt, or supporting proof is inadequate for the claimed classification

UNVERIFIABLE is not the same as FAIL.

A system may be structurally sound in principle yet still be UNVERIFIABLE for a claimed result.

UNVERIFIABLE does not mean:
- false
- disproven
- automatically PARTIAL
- automatically FAIL

It means the stronger claim cannot be sustained from the available evidence.

---

### 4.5 CONTRADICTION_EXPOSED

CONTRADICTION_EXPOSED means:

- the stated claim and the available evidence or structure conflict in a materially disqualifying way
- the system says one thing, but the stress result shows another

This is stronger than ordinary failure.

CONTRADICTION_EXPOSED should be used where:
- the architecture claims continuity but the identified boundary cannot actually refuse
- the system claims governed mutation but the true mutation authority is elsewhere
- the system claims strong scope but only bounded partial support is evidenced
- the system claims verification sufficiency but the receipt or trace structure cannot support the claim

CONTRADICTION_EXPOSED does not automatically mean maliciousness.
It means the stronger claim is materially inconsistent with the evaluated reality.

---

## 5. RESULT ORDERING

For conservative interpretation, the result set should be understood in this order:

1. STRONG
2. PARTIAL
3. FAIL
4. UNVERIFIABLE
5. CONTRADICTION_EXPOSED

This ordering is not a numeric score.
It is a discipline rule for claim strength and degradation.

A system must never move upward in this ordering without new bounded support.

---

## 6. DOWNGRADE DISCIPLINE

A stronger claim must be downgraded whenever:

- the surviving scope narrows
- a required continuity condition fails
- evidence becomes insufficient
- a contradiction is exposed
- a claimed boundary is not the true mutation authority
- a required refusal path is no longer live
- a trace or receipt gap prevents bounded verification

Safe downgrade examples:

- STRONG -> PARTIAL
- STRONG -> FAIL
- STRONG -> UNVERIFIABLE
- STRONG -> CONTRADICTION_EXPOSED
- PARTIAL -> FAIL
- PARTIAL -> UNVERIFIABLE
- PARTIAL -> CONTRADICTION_EXPOSED

A weaker result must never be silently restated as a stronger one.

---

## 7. RELATION TO FINDINGS / GAPS / CONTRADICTIONS

Primary result is not enough by itself.

Each result should be accompanied, where applicable, by:

- findings
- gaps
- contradictions
- bounded hardening direction

Safe interpretation rule:

- findings explain what held
- gaps explain what could not be supported
- contradictions explain what materially conflicts
- the primary result states the bounded classification

These must remain distinct.

---

## 8. RELATION TO STRESS CATEGORIES

The same primary result vocabulary applies across bounded stress categories.

That means:

- identity continuity stress can return STRONG, PARTIAL, FAIL, UNVERIFIABLE, or CONTRADICTION_EXPOSED
- authority continuity stress can return STRONG, PARTIAL, FAIL, UNVERIFIABLE, or CONTRADICTION_EXPOSED
- mutation-authority truthfulness stress can return STRONG, PARTIAL, FAIL, UNVERIFIABLE, or CONTRADICTION_EXPOSED

Category identity is fixed.
Result varies by scenario and evidence.

---

## 9. NON-CLAIMS

This vocabulary does not claim:

- that all future SPECTRE-FST profiles must use no additional secondary labels
- that this alone completes the receipt format
- that this alone completes selector logic
- that this alone completes upgrade analysis
- that STRONG in one category means strong system-wide conformance

This is the primary bounded result vocabulary only.

---

## 10. FINAL RULE

SPECTRE-FST must use bounded primary results.

Those results are:

- STRONG
- PARTIAL
- FAIL
- UNVERIFIABLE
- CONTRADICTION_EXPOSED

No stronger claim may be inferred from a weaker result.

Every stronger claim must remain explicitly bounded by:
- category
- scope
- evidence sufficiency
- contradiction status

END OF FILE
