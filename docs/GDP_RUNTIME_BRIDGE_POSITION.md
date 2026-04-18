# GDP RUNTIME BRIDGE POSITION

## PURPOSE

This document defines the runtime-repo-authoritative positioning for GDP relative to DTPE / IAL / SPECTRE.

It exists to preserve the distinction between:

- structural sufficiency evaluation
- execution-bound proof substantiation
- bridge comparison between the two

This document is architecture positioning only.
It does not claim GDP runtime implementation inside this repository.

---

## GDP ROLE

GDP is the structural sufficiency sidecar.

GDP evaluates whether a governance model is structurally sufficient in principle.

GDP answers questions such as:

- is the governance model structurally complete
- are the required controls present in model form
- does the described architecture appear sufficient on its own terms

GDP does not itself prove runtime execution truth.

GDP does not itself produce canonical execution proof.

---

## DTPE / IAL / SPECTRE ROLE

DTPE / IAL / SPECTRE is the core governed execution and proof engine.

Its role is to:

- evaluate admissibility at the execution boundary
- bind canonical evidence
- emit receipt-bearing execution artifacts
- support replay-verifiable proof of what execution actually did

DTPE / IAL / SPECTRE substantiates execution-bound proof.

---

## BRIDGE ROLE

The bridge is the comparison layer between GDP structural claims and DTPE proof summary / artifact-backed evidence.

Its role is to determine whether DTPE proof:

- matches GDP structural claims
- is insufficient for GDP structural claims
- contradicts GDP structural claims

The bridge does not collapse GDP into DTPE.
The bridge does not turn GDP into runtime execution.
The bridge does not elevate structural sufficiency into execution truth.

---

## PREFERRED LANGUAGE

Use:

- GDP evaluates structural sufficiency
- DTPE / IAL / SPECTRE substantiate execution proof
- the bridge determines whether DTPE proof matches, is insufficient for, or contradicts GDP structural claims

---

## PROHIBITED LANGUAGE

Do not say:

- GDP verifies runtime execution
- GDP produces canonical execution proof
- DTPE replaces GDP structural evaluation
- GDP alone proves what execution actually did

---

## RELATION TO CURRENT ARCHITECTURE DIRECTION

This repository's current working architecture direction is:

- DTPE / IAL / SPECTRE = core governed execution and proof engine
- GDP = structural sufficiency sidecar
- SPECTRE-FST plus Upgrade Analysis = bounded third-wheel direction for targeted fundamental stress testing, receipt-bound classification, weak-point detection, and evidence-grounded hardening guidance

This document aligns GDP bridge language with that trike-model direction.

See:

- `docs/SPECTRE_FST_TRIKE_MODEL.md`

---

## NON-CLAIMS

This document does not claim:

- GDP runtime implementation in this repository
- bridge runtime implementation in this repository
- completed cross-repo bridge integration
- replacement of DTPE / IAL / SPECTRE by GDP
- replacement of GDP by DTPE / IAL / SPECTRE

---

## FINAL RULE

GDP remains the structural sufficiency sidecar.

DTPE / IAL / SPECTRE remains the execution-bound proof engine.

The bridge remains the comparison layer between GDP structural claims and DTPE artifact-backed execution proof.

These roles must remain separate.

END OF FILE
