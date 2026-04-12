# SPECTRE-SENTINEL LEDGER EXTENSION NOTES

## Status

This artifact defines conceptual ledger extension notes for future Sentinel integration.

It is bounded and future-facing.

It does not claim ledger extension is already implemented.

---

## 1. Purpose

This artifact records what ledger surfaces would likely need if future Sentinel integration later becomes bounded runtime work.

---

## 2. Conceptual Ledger Additions

A later ledger extension may need to persist:
- canonical semantic artifact reference
- boundary evaluation reference
- artifact-to-decision linkage
- refusal / allow / downgrade relation where applicable
- replay-useful ordering and integrity relation

---

## 3. What Must Not Be Claimed Yet

Until ledger surfaces are explicitly extended, do not claim:
- ledger completeness for Sentinel integration
- replay completeness through ledger linkage alone
- verifier completeness through ledger presence alone

---

## 4. Collaboration Rule

These notes exist so future collaboration can start from a repo-hosted ledger-extension baseline.

---

## 5. Direct Rule

The direct rule is:

Future Sentinel ledger claims are valid only if ledger surfaces are explicitly extended to preserve artifact-to-boundary-decision linkage in replay-usable form.