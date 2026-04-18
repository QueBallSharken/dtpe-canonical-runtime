# DTPE - SYSTEM MODEL

## STATUS

- Repo-authoritative architecture positioning document
- Documentation only
- No runtime implementation authorized by this document
- Does not override current committed Phase 7 / Phase 8 / Phase 9 classification documents

---

## PURPOSE

This document defines the top-level system model for DTPE as it exists in the current repository direction.

It positions the relationship between:

- DTPE
- IAL
- SPECTRE
- GDP bridge position
- SPECTRE-FST
- mutation authority
- receipt / ledger / verifier evidence
- future-only Sentinel direction

This document is architectural positioning only.
It must not be used to silently expand runtime scope.

---

## CURRENT REPO POSITION

DTPE is the umbrella governance architecture of this repository.

DTPE currently governs a runtime path that already includes:

- execution-bound admissibility
- canonical receipt construction
- append-only ledger evidence
- offline replay verification
- temporal admissibility
- continuity-related boundary enforcement
- bounded decision-space evidence
- evaluator-trace-related evidence surface

This document does not reclassify the exact bounded Phase 9 state.
That remains governed by the current phase documents.

---

## TOP-LEVEL MODEL

DTPE is responsible for the full governance chain:

1. canonical inputs are defined
2. admissibility is evaluated at the execution boundary
3. canonical evidence is constructed
4. evidence is recorded
5. evidence is replay-verified
6. later phases strengthen reconstruction integrity
7. later mutation-integrity layers ensure reality cannot change unless the governing predicate still holds at the mutation boundary

---

## INTERNAL POSITIONING

### IAL

IAL is the Invariant Assertion Layer inside DTPE.

IAL defines the canonical semantic artifacts that answer:

- what invariant is being enforced?
- what evaluator rule identity is being bound?
- what future evaluator-output identity must be reconstructable?

IAL is a semantic layer.
It is not, by itself, evidence storage or mutation control.

This document introduces IAL as architecture positioning.
It does not claim full IAL runtime implementation already exists.

---

### SPECTRE

SPECTRE is the execution-boundary evaluation subsystem inside DTPE.

SPECTRE conceptually covers execution-bound evaluation concerns such as:

- state admissibility
- system stability
- temporal admissibility
- continuity
- bounded decision-space evidence
- evaluator-trace-related boundary evidence

This document positions SPECTRE conceptually.
It does not claim that the current repository already contains a separately named SPECTRE runtime package or module.

---

### GDP BRIDGE POSITION

GDP is not part of the DTPE execution-bound evaluator.

GDP is the structural sufficiency sidecar.

The GDP bridge position inside the current architecture direction is:

- GDP evaluates whether a governance model is structurally sufficient in principle
- DTPE / IAL / SPECTRE substantiate execution-bound proof
- the bridge determines whether DTPE proof matches, is insufficient for, or contradicts GDP structural claims

This preserves the distinction between structural sufficiency and execution truth.

---

### SPECTRE-FST

SPECTRE-FST is the bounded fundamental stress evaluation direction attached to the current architecture framing.

Its intended role is to:

- stress-test whether claimed governing truth survives deformation classes
- emit bounded classification results
- support receipt-bearing findings, gaps, and contradictions
- feed evidence-grounded Upgrade Analysis

SPECTRE-FST is current architecture direction only in the repository.
No runtime implementation is authorized by this document.

---

### UPGRADE ANALYSIS

Upgrade Analysis is a downstream architecture direction derived from SPECTRE-FST findings.

Its intended role is to:

- identify hardening opportunities
- map factual weaknesses to bounded upgrade recommendations
- remain grounded in observed findings rather than generic best practices

Upgrade Analysis is architecture direction only in the current repository.

---

### FUTURE-ONLY SENTINEL POSITION

Sentinel remains future-only direction in the current repository.

Sentinel is not:

- the current runtime direction
- part of the active trike model
- the current third-wheel answer
- a normalized active runtime surface

Any future Sentinel work must remain explicitly bounded and must not silently replace the DTPE / IAL / SPECTRE plus GDP plus SPECTRE-FST architecture direction.

---

### MUTATION AUTHORITY

Mutation authority is the component that controls the true state-changing primitive.

It answers the question:

- can reality change now?

Mutation authority is distinct from:

- policy evaluation
- receipt issuance
- later attestation
- later recording

Mutation authority becomes critical wherever the thing that changes reality is not identical to the component that enforced admissibility at the execution boundary.

---

### EVIDENCE SUBSYSTEM

DTPE evidence is carried through canonical artifacts such as:

- receipt
- ledger
- verifier reconstruction inputs

This evidence layer proves:

- what canonical inputs were used
- what boundary decision was made
- what was recorded
- what can be replayed
- what can later be reconstructed more strongly

Evidence alone is necessary but not sufficient for full mutation-bound governance.

---

## HIERARCHY

DTPE
- IAL
- SPECTRE
- GDP bridge position
- SPECTRE-FST
- Upgrade Analysis
- Mutation Authority
- Receipt / Ledger / Verifier
- future-only Sentinel direction

---

## PHASE POSITIONING

This document does not replace the current phase docs.

It positions the concepts relative to the existing direction:

- Phase 5-7: execution-bound admissibility, temporal enforcement, continuity
- Phase 8: bounded decision-space and signal-profile evidence
- Phase 9: evaluator integrity and reconstruction-strengthening layers
- Phase 10: mutation integrity / execution hardening

---

## PQC / CRYPTO-AGILITY RULE

All DTPE architecture and future implementation must remain:

- crypto-profile-driven
- algorithm-agnostic at the semantic layer
- canonically serializable
- replay-verifiable
- independently reconstructable without hidden runtime dependence
- compatible with post-quantum readiness

No semantic governance artifact may depend on a single permanent cryptographic algorithm.

Cryptographic mechanisms prove canonical artifacts.
They do not define the semantic identity of those artifacts.

---

## FINAL RULE

DTPE is the umbrella governance architecture.

IAL defines canonical semantic artifacts.
SPECTRE evaluates admissibility at the execution boundary.
GDP remains the structural sufficiency sidecar and bridge-comparison position.
SPECTRE-FST plus Upgrade Analysis is the current bounded third-wheel architecture direction.
Sentinel remains future-only direction and is not the active runtime direction.
Mutation authority controls whether reality may change.
Receipt, ledger, and verifier provide canonical evidence.

This document is architecture positioning only.
It does not authorize runtime implementation beyond the current repo-authoritative phase boundary.
