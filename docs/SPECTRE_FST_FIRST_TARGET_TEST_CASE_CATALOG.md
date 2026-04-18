# SPECTRE-FST FIRST TARGET TEST CASE CATALOG

## STATUS

This document defines the initial bounded test case catalog for the first SPECTRE-FST target.

It is architecture-facing only.

---

## 1. PURPOSE

The first target needs explicit scenarios, not abstract promises.

This catalog records the minimum scenario set to support the first bounded evaluator slice.

---

## 2. FIRST TARGET TEST CASES

### TC-001 Identity Continuity Stress
Scenario:
A claimed continuity path says the same governed transition survived across later boundaries, but transition identity continuity is only partially evidenced.

Expected:
A bounded result such as PARTIAL or UNVERIFIABLE, depending on the explicit evidence shape.

### TC-002 Authority Continuity Stress
Scenario:
A claim says authority continuity survived, but the later authority basis cannot be strongly tied to the earlier governed basis.

Expected:
FAIL, PARTIAL, or CONTRADICTION_EXPOSED depending on the exact claim strength.

### TC-003 Boundary Truthfulness Stress
Scenario:
A system claims the covered boundary is the real controlling point, but the actual mutation authority appears downstream.

Expected:
FAIL or CONTRADICTION_EXPOSED.

### TC-004 Proof Continuity Stress
Scenario:
A strong claim is made, but the supporting trace/receipt evidence is incomplete.

Expected:
UNVERIFIABLE.

### TC-005 Fail-Closed Discipline Stress
Scenario:
A stronger claim remains asserted after a required continuity condition breaks.

Expected:
CONTRADICTION_EXPOSED.

---

## 3. CATALOG RULE

The first implementation slice does not need all cases implemented.

But the first target must choose at least one explicit case from this catalog and classify it with bounded receipt output.

END OF FILE
