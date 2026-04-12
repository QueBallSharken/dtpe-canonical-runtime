# SPECTRE-SENTINEL FUTURE INTEGRATION POSITION

## Status

This artifact defines the bounded future-integration position for Sentinel relative to the current public DTPE / IAL / SPECTRE repo posture.

It is intentionally constrained.

It does not imply runtime authorization today.
It does not replace SPECTRE.
It does not replace DTPE.
It does not replace BBIS.
It does not imply completion.

---

## 1. Purpose

This artifact defines where Sentinel sits in a future integration profile.

It exists to state:
- where Sentinel sits
- what layer it is
- what it feeds
- what it does not replace
- what must remain future-only

---

## 2. Sentinel Layer Position

Sentinel sits as:
- a future semantic / interception ingress layer
- a future front-side semantic / interception shell
- a future pre-boundary shaping layer

It does not sit as:
- the public runtime core
- the execution-bound evaluator
- the receipt / ledger / verifier layer

---

## 3. What Sentinel Feeds

Sentinel feeds:
- IAL-native canonical semantic artifacts

It should not feed only:
- scores
- labels
- alerts
- detector verdicts

Those may exist as auxiliary outputs, but they are not sufficient as the governing downstream object.

---

## 4. What Happens Next

The future integration path is:

1. Sentinel observes or intercepts candidate transition context
2. Sentinel forms or helps form semantic findings
3. those findings are carried into an IAL-native canonical semantic artifact
4. SPECTRE evaluates that artifact at the execution / mutation boundary
5. DTPE carries receipt / ledger / verifier effects if and when bounded runtime integration extends those surfaces

---

## 5. What Sentinel Does Not Replace

Sentinel does not replace:
- IAL
- SPECTRE
- DTPE
- BBIS

Sentinel must not be described as:
- already-normalized runtime surface
- public replacement for boundary evaluation
- substitute for mutation-bound enforcement
- substitute for continuity conformance across the full mutation path

---

## 6. Safe Framing

Sentinel must be framed as:
- a proposed future integration profile
- subordinate to the public DTPE / IAL / SPECTRE architecture
- compatible with BBIS but not merged into core BBIS by default
- requiring explicit docs alignment before normative implementation claims

---

## 7. Unsafe Framing

Sentinel must not be framed as:
- replacing SPECTRE
- silently extending IAL into runtime by implication
- an already-authorized public runtime surface
- a completed architecture layer today
- a substitute for BBIS

---

## 8. Future-Only Rule

Until BBIS is completely implemented and stabilized, Sentinel must remain:
- future integration only
- bounded in claim language
- subordinate in architecture language
- non-authorizing by implication

---

## 9. Direct Position Statement

The direct future-integration position is:

SPECTRE-SENTINEL is a future semantic / interception ingress layer that feeds IAL-native canonical semantic artifacts for later SPECTRE evaluation at the execution boundary and later DTPE evidence integration if explicitly implemented under bounded repo rules.

That is the safe position.