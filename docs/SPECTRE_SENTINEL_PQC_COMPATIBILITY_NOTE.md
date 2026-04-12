# SPECTRE-SENTINEL PQC COMPATIBILITY NOTE

## Status

This artifact records the PQC / crypto-agility compatibility note for future Sentinel integration.

It is intentionally bounded.

It does not claim full PQC migration.
It does not claim full crypto-agility completion.

---

## 1. Purpose

This artifact defines the required PQC compatibility posture for future Sentinel integration.

---

## 2. Core Requirement

PQC must be on and always at the ready.

That means:
- Sentinel future integration must not assume a structurally legacy-only crypto posture
- claim-relevant crypto posture must be surfaced where applicable
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- future Sentinel artifacts must remain compatible with broader repo crypto direction

---

## 3. What This Does Not Mean

This note does not mean:
- full PQC migration is already complete
- all crypto-agility work is finished
- Sentinel itself provides crypto completeness

It only means the future-integration package must remain compatible with the repo's crypto direction and must not create a legacy-only trap.

---

## 4. Direct Rule

Any future Sentinel artifact that structurally assumes legacy-only crypto posture is incompatible with this package and must be rejected or rewritten.