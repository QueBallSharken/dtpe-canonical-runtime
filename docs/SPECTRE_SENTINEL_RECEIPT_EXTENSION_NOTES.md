# SPECTRE-SENTINEL RECEIPT EXTENSION NOTES

## Status

This artifact defines conceptual receipt extension notes for future Sentinel integration.

It is bounded and future-facing.

It does not claim receipt extension is already implemented.

---

## 1. Purpose

This artifact records what receipt surfaces would likely need if future Sentinel integration later becomes bounded runtime work.

---

## 2. Conceptual Receipt Additions

A later receipt extension may need to carry:
- canonical semantic artifact identity
- reference to IAL-native object
- SPECTRE evaluation linkage to that object
- refusal / allow / downgrade relation where applicable
- integrity linkage sufficient for replay

---

## 3. What Must Not Be Claimed Yet

Until receipt surfaces are explicitly extended, do not claim:
- receipt completeness for Sentinel integration
- receipt-backed verifier completeness
- replay completeness through receipts alone

---

## 4. Collaboration Rule

These notes exist so future collaboration can start from repo-hosted receipt-extension assumptions rather than reconstructing them from memory.

---

## 5. Direct Rule

The direct rule is:

Future Sentinel receipt claims are valid only if receipt surfaces are explicitly extended to carry artifact identity and boundary-decision linkage.