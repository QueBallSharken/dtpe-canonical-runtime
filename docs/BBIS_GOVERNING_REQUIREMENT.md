# BBIS - GOVERNING REQUIREMENT
## Boundary-to-Boundary Invariant Survival

**Author:** Stephen Kyle Hensley  
**Alias:** Cueball Shark  
**GitHub:** QueBallSharken

## STATUS

This document defines BBIS as a standalone governing requirement.

It is not a product pitch.
It is not a runtime implementation claim.
It is not a complete architecture by itself.

It defines the requirement that any candidate architecture must satisfy if it claims mutation-bound governance continuity.

---

## 1. PURPOSE

BBIS exists to answer a stricter governance question:

A governed transition is not valid merely because it was approved earlier, executed faithfully, or recorded completely.

It remains valid only if the same governing invariant survives each mutation-capable boundary as a live refusal condition until the true irreversible primitive.

This is the governing requirement.

Architectures may attempt to satisfy it.
They must not be confused with it.

---

## 2. CORE DEFINITION

**Boundary-to-Boundary Invariant Survival (BBIS)** is the requirement that the same governing invariant remain live, binding, and refusal-capable across every mutation-capable boundary in the claimed path until the true irreversible primitive for the claimed scope.

A system does not satisfy BBIS merely because:
- it evaluated policy earlier
- it produced a receipt
- it logged a decision
- it later proved what it believed happened

A system satisfies BBIS only to the extent that the same governing basis can still prevent or invalidate mutation at each required boundary until the relevant irreversible effect is reached.

---

## 3. WHAT BBIS GOVERNS

BBIS governs continuity of the governing basis itself.

That means BBIS asks whether the following survive across the claimed path:

- governing invariant continuity
- authority continuity
- identity continuity where claim-relevant
- refusal continuity
- timing-valid refusal continuity
- mutation-path completeness for the claimed scope
- evidence sufficiency for independent replay and verification

BBIS is therefore a continuity requirement, not merely a point-in-time approval requirement.

---

## 4. TRUE IRREVERSIBLE PRIMITIVE

Every BBIS claim must identify the true irreversible primitive for the claimed scope.

This is the actual boundary, mechanism, or primitive whose successful completion makes the relevant mutation operationally binding or irreversible.

A system cannot honestly claim BBIS satisfaction if it governs an earlier boundary while the true irreversible primitive remains outside the governed path.

Misidentifying the true irreversible primitive is a failure of the claim.

---

## 5. MUTATION-CAPABLE BOUNDARIES

A mutation-capable boundary is any boundary at which a transition can:

- commit
- release
- publish
- promote
- forward
- authorize
- materialize
- otherwise cause a state change with irreversible or operationally binding effect

BBIS applies across these boundaries only where the claim scope includes them.

Coverage must never be assumed.

---

## 6. LIVE REFUSAL REQUIREMENT

The center of BBIS is live refusal continuity.

A governing invariant is not truly surviving if it can only:

- observe
- log
- warn
- recommend
- report after the fact
- impose cost after commit

For BBIS satisfaction, the governing basis must remain able to:

- block mutation before completion
- prevent release before binding effect
- invalidate the governed transition before the true irreversible primitive completes

If refusal exists in theory but cannot act in time, BBIS is not satisfied for that boundary.

---

## 7. WHAT MUST SURVIVE

For BBIS satisfaction, the claimed path must preserve, to the degree relevant to the claim:

### 7.1 Invariant Continuity
The same governing invariant remains in force across the claimed path.

### 7.2 Authority Continuity
The governing authority basis remains the same, or changes only through explicitly governed and replay-verifiable succession.

### 7.3 Identity Continuity
Where transition identity is claim-relevant, the same governed transition remains bound to later boundaries without silent substitution.

### 7.4 Refusal Continuity
The governing basis remains refusal-capable at each required boundary.

### 7.5 Timing Continuity
Refusal remains capable of acting before mutation completes.

### 7.6 Path Continuity
No alternate uncontrolled mutation path invalidates the stronger claim for the claimed scope.

### 7.7 Evidence Continuity
The evidence required to verify these facts remains sufficient for independent replay and review.

---

## 8. WHAT DOES NOT SATISFY BBIS

BBIS is not satisfied by:

- earlier approval alone
- faithful later execution alone
- receipts alone
- audit logs alone
- witnesses without refusal power
- advisory systems without mechanically effective refusal
- sidecars, monitors, or TEEs that cannot actually prevent mutation
- coverage of one path while another uncontrolled path can still mutate reality
- evidence of observation without evidence of live refusal continuity

BBIS is stricter than:
- policy evaluation
- execution-bound approval
- post-hoc verification
- logging
- auditability

These may support BBIS.
They do not equal BBIS.

---

## 9. FAILURE MODES

A BBIS claim fails or degrades when any required continuity breaks.

Core failure classes include:

- invariant continuity failure
- authority continuity failure
- identity continuity failure
- refusal failure
- latency failure
- alternate path failure
- truth-boundary failure
- evidence insufficiency failure
- scope inflation failure

A system must not silently preserve a stronger BBIS claim once one of these failures occurs.

It must downgrade or reject the claim.

---

## 10. EVIDENCE REQUIREMENT

BBIS is not satisfied by architecture description alone.

For the claimed scope, evidence must be sufficient to independently evaluate:

- what was claimed
- which path was covered
- what boundaries were mutation-capable
- what the true irreversible primitive was
- what governing basis remained in force
- whether refusal remained live
- whether refusal remained timely
- whether alternate paths escaped governance
- where continuity was lost
- whether the final claim exceeded what the evidence supports

If these cannot be shown, the stronger BBIS claim cannot survive.

---

## 11. CLASSIFICATION

BBIS claims should be classified conservatively.

At minimum:

### 11.1 Strong
The same governing invariant remained live and refusal-capable across all required mutation-capable boundaries until the true irreversible primitive for the claimed scope, with sufficient evidence for independent replay.

### 11.2 Partial
Some continuity requirements survived, but not all. The claim must be explicitly bounded to the surviving scope.

### 11.3 Fail
The governing basis did not remain live and refusal-capable across the required boundaries, or the evidence is insufficient to support the stronger claim.

No stronger class may be inferred from a weaker one.

---

## 12. RELATIONSHIP TO ARCHITECTURE

BBIS is the requirement.

Architectures are candidate realizations.

That means:

- BBIS is not DTPE
- BBIS is not IAL
- BBIS is not SPECTRE
- BBIS is not GDP
- BBIS is not SPECTRE-FST
- BBIS is not Model 9
- BBIS is not Sentinel

Those may be architectures, subsystems, evaluators, or bounded answers that attempt to satisfy BBIS for some scope.

They must not replace the requirement itself.

---

## 13. RELATIONSHIP TO MODEL 9

Model 9 is not BBIS.

Model 9 is one bounded architectural answer to the BBIS question.

If Model 9 satisfies BBIS for a claimed scope, that is because its architecture actually preserves the required continuity conditions for that scope.

Model 9 does not redefine BBIS.
It is evaluated against BBIS.

---

## 14. RELATIONSHIP TO DTPE / IAL / SPECTRE

DTPE / IAL / SPECTRE is not BBIS.

It is an architecture stack that may satisfy BBIS in bounded form if:

- the governing invariant remains live at every required mutation-capable boundary
- refusal remains mechanically effective and timely
- the true irreversible primitive is actually governed for the claimed scope
- replay and evidence are sufficient to verify the claim honestly

Architecture must not be mistaken for conformance.

---

## 15. FINAL RULE

BBIS must remain above any candidate architecture.

The law is:

The same governing invariant must remain live, binding, and refusal-capable across every mutation-capable boundary in the claimed path until the true irreversible primitive for the claimed scope.

If that does not hold, the stronger continuity claim must not survive.

END OF FILE
