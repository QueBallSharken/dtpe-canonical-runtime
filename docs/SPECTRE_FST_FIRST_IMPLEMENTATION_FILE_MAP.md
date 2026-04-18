# SPECTRE-FST FIRST IMPLEMENTATION FILE MAP

## STATUS

This document defines the first bounded file map for SPECTRE-FST implementation planning.

It is planning-facing only.

It does not claim these files already exist.

---

## 1. PURPOSE

The first runtime slice should begin from an explicit file map, not improvised placement.

This document defines the minimum file targets for the first implementation slice.

---

## 2. MINIMUM FILE MAP

A safe first implementation file map may include:

- core/spectre/fst/
- core/spectre/fst/__init__.py
- core/spectre/fst/result_vocabulary.py
- core/spectre/fst/rule_profiles.py
- core/spectre/fst/receipt_schema.py
- core/spectre/fst/evaluator.py
- core/spectre/fst/scenarios.py
- tools/test_fst_first_target.py

---

## 3. ROLE OF EACH FILE

### result_vocabulary.py
Carries the bounded primary result vocabulary.

### rule_profiles.py
Carries the first-target rule profile identity and interpretation rules.

### receipt_schema.py
Carries the minimal receipt shape.

### evaluator.py
Applies one bounded scenario to one bounded category under one bounded rule profile.

### scenarios.py
Carries explicit first-target scenario definitions.

### test_fst_first_target.py
Proves the first bounded target behaves deterministically and emits the expected minimal receipt structure.

---

## 4. FINAL RULE

The first implementation slice should remain narrow enough that each file has one bounded purpose.

END OF FILE
