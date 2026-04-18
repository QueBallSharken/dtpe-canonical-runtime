# SPECTRE-FST SELECTOR MINIMAL PROFILE

## STATUS

This document defines the minimal selector profile for SPECTRE-FST.

It is architecture-facing only.

---

## 1. PURPOSE

SPECTRE-FST requires a selector / evaluator split.

This document defines the smallest selector profile that makes weak-point targeting real without collapsing selector logic into fuzzy evaluation.

---

## 2. SELECTOR ROLE

The selector chooses:

- likely weak point
- relevant stress category
- bounded targeting rationale

The selector does not emit the final bounded primary result.

That belongs to the evaluator.

---

## 3. MINIMAL SELECTOR REQUIREMENTS

A minimal selector profile must support:

- one explicit weak-point target
- one explicit category choice
- one explicit rationale for why that category fits the scenario

---

## 4. FIRST TARGET SELECTOR PROFILE

For the first bounded target:

- weak point = incomplete system-wide refusal continuity support
- selected category = boundary_continuity_stress
- rationale = the claim depends on continuity across boundaries, and the weak point appears at the system-wide refusal layer rather than purely at the local refusal point

---

## 5. NON-CLAIMS

This minimal selector profile does not claim:

- broad adaptive intelligence
- automatic multi-category orchestration
- system-wide architecture discovery
- complete upgrade-analysis maturity

It is a bounded weak-point targeting profile only.

---

## 6. FINAL RULE

The selector must choose the weak point and category explicitly.

If those are not explicit, the evaluator is being asked to do selector work implicitly.

END OF FILE
