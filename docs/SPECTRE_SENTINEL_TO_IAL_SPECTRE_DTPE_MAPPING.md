# SPECTRE-SENTINEL TO IAL / SPECTRE / DTPE MAPPING

## Status

This artifact defines the architecture mapping for future Sentinel integration into the current public DTPE / IAL / SPECTRE repo posture.

It is intentionally constrained.

It does not treat Sentinel as an already-normalized runtime core.
It does not authorize runtime expansion by implication.
It does not replace BBIS.
It does not replace SPECTRE.
It does not claim current integration completeness.

This artifact is safe only as a future-integration mapping profile pending:
- direct repo-file alignment
- full docs alignment
- README alignment
- bounded implementation authorization under repo phase rules

---

## 1. Purpose

This artifact maps Sentinel into the existing DTPE / IAL / SPECTRE public architecture without creating public contradiction.

It exists to define:
- where Sentinel sits
- what Sentinel emits
- what IAL owns
- what SPECTRE evaluates
- what DTPE carries
- what BBIS still requires
- what later receipt / ledger / verifier work would need
- what must remain future-only until BBIS is complete

---

## 2. Governing Current-Repo Position

For this mapping, the working repo-safe position is:

- DTPE / IAL / SPECTRE is the current public architecture triad
- IAL is the canonical semantic artifact layer
- SPECTRE evaluates IAL-defined semantic artifacts at the execution boundary
- DTPE carries canonical receipt / ledger / offline verifier evidence paths
- boundary integrity requires no irreversible mutation except through explicit mutation authority evaluating a still-governing admissibility predicate
- Sentinel is not authorized as a public runtime layer by implication
- Sentinel remains future integration only until BBIS is fully implemented and stabilized

This mapping must be checked against current repo language before being treated as normative.

---

## 3. Governing Split

Use this exact split:

- Sentinel = future semantic / interception ingress layer
- IAL = canonical semantic artifact layer
- SPECTRE = execution / mutation-bound evaluation layer
- DTPE = canonical receipt / ledger / offline verifier evidence path
- BBIS = continuity / conformance requirement across the full mutation path

Do not merge these responsibilities conceptually.

---

## 4. Sentinel Position

### 4.1 Layer position

Sentinel sits at the front side of the system as:
- a future semantic ingress layer
- a future interception shell
- a future semantic pre-boundary shaping layer

### 4.2 Safe role

Sentinel may:
- observe
- intercept
- analyze
- enrich
- shape canonical semantic input

Sentinel may not, by default wording alone:
- replace execution-bound evaluation
- replace mutation-bound enforcement
- replace offline verification
- imply BBIS completion

### 4.3 Safe output

Sentinel should not emit only:
- a score
- a label
- an alert
- a detector verdict

Sentinel should emit or help form:
- a canonical semantic artifact suitable for IAL ownership

---

## 5. IAL Position

### 5.1 Ownership role

IAL owns:
- canonical semantic objects
- semantic artifact definitions
- canonical structure
- semantic admissibility-relevant representation
- canonical semantic normalization rules

### 5.2 Mapping consequence

Sentinel output is not the final governing object by itself.

The governing object for downstream use should be:
- an IAL-native canonical semantic artifact

### 5.3 Safety rule

IAL positioning must not be used to imply:
- Sentinel runtime authorization
- completed runtime integration
- automatic mutation-bound governance

---

## 6. SPECTRE Position

### 6.1 Evaluation role

SPECTRE remains:
- the execution / mutation-bound evaluation layer
- the boundary evaluator of IAL-defined semantic artifacts

### 6.2 Mapping consequence

The proper future path is:
- Sentinel forms or helps form semantic artifact
- IAL owns canonical artifact
- SPECTRE evaluates canonical artifact at execution boundary

### 6.3 Safety rule

Sentinel does not replace SPECTRE.

Any wording that makes Sentinel sound like the new boundary evaluator is unsafe and must be rejected.

---

## 7. DTPE Position

### 7.1 Evidence role

DTPE remains:
- canonical receipt path
- canonical ledger path
- offline verifier evidence path

### 7.2 Mapping consequence

If Sentinel future integration later becomes bounded runtime work, DTPE is the place where:
- receipt impacts
- ledger impacts
- offline verifier impacts

must be defined explicitly.

### 7.3 Safety rule

Do not claim verifier integration merely because Sentinel emits semantic input.

Verifier integration exists only if:
- receipt surfaces are extended where needed
- ledger surfaces are extended where needed
- replay and verifier logic are extended where needed

---

## 8. BBIS Position

### 8.1 BBIS role

BBIS remains:
- the continuity requirement
- the conformance requirement across the full mutation path

### 8.2 Mapping consequence

Sentinel may support a future BBIS-constrained architecture, but Sentinel does not itself solve BBIS.

### 8.3 Safety rule

Do not equate:
- detector
- ingress gateway
- semantic shell
- interception block

with:
- full mutation-bound continuity
- boundary-to-boundary invariant survival
- BBIS completion

---

## 9. Canonical Object Flow

The intended future-integrated object flow is:

1. Sentinel observes or intercepts candidate transition context
2. Sentinel forms or helps form semantic findings
3. those findings are carried into a canonical IAL-native semantic artifact
4. SPECTRE evaluates that artifact at the execution / mutation boundary
5. DTPE records receipt / ledger / verifier consequences if and when bounded runtime integration extends those surfaces

This is the correct architecture mapping.

---

## 10. Semantic Object Requirements

The Sentinel-origin semantic object should conceptually carry or help produce:

- object identity
- semantic subject / target
- semantic findings
- semantic predicates asserted
- provenance / source of analysis
- scope of applicability
- admissibility-relevant conditions
- mutation relevance or boundary relevance
- canonical representation suitable for IAL
- integrity metadata compatible with repo crypto direction
- replay-sufficient structure

These are conceptual mapping requirements, not yet a claim of current normalized runtime implementation.

---

## 11. Boundary Impact Notes

Future Sentinel integration would affect the boundary layer only through:
- IAL-native canonical semantic artifacts
- evaluated by SPECTRE at the execution boundary

Safe boundary claims:
- stronger semantic ingress posture
- better semantic object formation pressure
- better bridge from semantic analysis to boundary evaluation

Unsafe boundary claims:
- Sentinel itself is now the execution-bound evaluator
- Sentinel alone closes mutation-bound governance
- Sentinel alone closes boundary-to-boundary continuity

---

## 12. Receipt / Ledger / Verifier Impact Notes

Any future Sentinel integration that claims verifier compatibility must explicitly define:

### 12.1 Receipt impact
- how semantic artifact identity is carried into receipts
- how boundary evaluation outcome references the canonical artifact
- how refusal / allow / downgrade semantics are recorded where applicable

### 12.2 Ledger impact
- how the semantic artifact reference is persisted
- how evaluation result linkage is persisted
- how later replay can reconstruct the relation

### 12.3 Verifier impact
- how offline verifier reconstructs the semantic artifact relation
- how verifier checks boundary evaluation against the artifact
- how verifier remains deterministic and replayable
- how crypto posture relevant to artifact integrity remains visible if claim-relevant

Without those explicit extensions, verifier completeness must not be claimed.

---

## 13. What This Future Integration Solves

A bounded Sentinel integration can solve or improve:
- stronger front-side semantic / interception posture
- pressure toward canonical semantic artifact formation
- a cleaner bridge from semantic analysis to execution-bound governance
- stronger ingress-side refusal conditions before mutation
- a cleaner future path for BBIS-constrained semantic governance
- a cleaner future path into DTPE evidence surfaces

---

## 14. What This Future Integration Does Not Solve

A bounded Sentinel integration does not solve:
- BBIS completion
- boundary-to-boundary invariant survival by itself
- mutation-bound enforcement at the true irreversible primitive by itself
- replacement of SPECTRE
- runtime authorization by implication
- verifier integration by itself unless receipt / ledger / replay surfaces are explicitly extended
- downstream continuity merely because ingress logic exists
- universal path closure
- full PQC migration
- full crypto-agility completion

---

## 15. Docs Alignment Requirements

Before this mapping is treated as normative, align against at minimum:
- `README.md`
- `docs/ARCHITECTURE_OVERVIEW.md`
- `docs/EXECUTION_INTEGRITY_MODEL.md`
- `docs/BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`
- `docs/IAL_SPEC.md`

Additional docs must be checked if they:
- describe DTPE / IAL / SPECTRE responsibilities
- imply runtime authorization
- describe semantic artifacts
- describe mutation authority
- describe verifier / receipt / replay semantics

---

## 16. README Alignment Requirements

README must be checked and updated if needed so that:
- Sentinel is not implied as already-normalized runtime surface
- DTPE / IAL / SPECTRE responsibilities remain consistent
- future-integration wording is explicit
- BBIS is not collapsed into Sentinel
- any IAL naming mismatch is either resolved or explicitly bounded and explained

---

## 17. Safe Publication Rule

This mapping is safe to publish later only if:
- current repo language is checked against it
- docs alignment is performed
- README alignment is performed
- runtime authorization is not implied
- BBIS is preserved as the continuity requirement
- SPECTRE remains the boundary evaluator
- DTPE remains the evidence path
- Sentinel remains future integration until BBIS is complete

---

## 18. Direct Final Mapping

The direct repo-safe mapping is:

- Sentinel -> future semantic / interception ingress layer
- IAL -> canonical semantic artifact layer
- SPECTRE -> execution / mutation-bound evaluation layer
- DTPE -> canonical receipt / ledger / offline verifier path
- BBIS -> continuity requirement across the full mutation path

That is the safe architecture mapping.

It preserves:
- current public architecture priority
- bounded future integration posture
- docs alignment requirement
- README alignment requirement
- verifier safety
- BBIS separation