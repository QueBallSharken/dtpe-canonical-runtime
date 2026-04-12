# SPECTRE-SENTINEL FUTURE INTEGRATION SPEC

## Status

This artifact defines a repo-ready future-integration package for Sentinel inside the public `dtpe-canonical-runtime` repo.

It is intentionally constrained.

It does not treat Sentinel as an already-normalized core runtime layer.
It does not imply runtime authorization from IAL positioning.
It does not replace DTPE / IAL / SPECTRE.
It does not claim BBIS is complete.
It does not authorize normative implementation claims by implication.

This artifact is safe only as a future-integration profile pending:
- direct repo-file alignment
- full docs alignment
- README alignment
- bounded implementation authorization under repo phase rules

---

## 1. Purpose

This artifact defines the safe future-integration position for Sentinel relative to the current public DTPE / IAL / SPECTRE architecture.

It exists to:
- keep Sentinel subordinate to the current public architecture
- prevent implied runtime expansion by wording drift
- define the proper Sentinel -> IAL -> SPECTRE -> DTPE evidence mapping
- define do / do not / must / must not rules
- define what Sentinel integration solves and does not solve
- define the conceptual object model for future bounded integration
- require full docs alignment and README alignment before any normative claim

---

## A. CURRENT PUBLIC REPO POSITION

This section states the required current public-repo position for this future-integration package.

### A.1 Already public

The public architecture triad is:
- DTPE
- IAL
- SPECTRE

### A.2 Already authorized

The current public position is treated as:
- IAL is the canonical semantic artifact layer
- SPECTRE evaluates IAL-defined semantic artifacts at the execution boundary
- DTPE carries canonical receipt / ledger / offline verifier evidence paths
- boundary integrity requires that no irreversible mutation occur except through explicit mutation authority evaluating a still-governing admissibility predicate

### A.3 Explicitly not authorized by implication

The following must be treated as not authorized by implication:
- Sentinel runtime work from IAL positioning alone
- Sentinel as an already-normalized public runtime surface
- Sentinel as a replacement for SPECTRE
- Sentinel as a replacement for BBIS
- Sentinel as a completed architecture layer today

### A.4 Current safety rule

Until direct repo-file verification and docs alignment are complete, Sentinel must be treated as:
- future integration only
- subordinate to current DTPE / IAL / SPECTRE public architecture
- non-normative for runtime expansion
- non-authorizing by implication

---

## B. SENTINEL FUTURE-INTEGRATION POSITION

### B.1 Where Sentinel sits

Sentinel sits as a:
- future semantic / interception ingress layer
- front-side semantic / interception / sentinel shell

### B.2 What Sentinel feeds

Sentinel feeds:
- IAL-native canonical semantic artifacts

### B.3 What happens next

The intended future path is:
- Sentinel forms or helps form a canonical semantic object
- that object lives as an IAL-native artifact
- SPECTRE evaluates that artifact at the execution / mutation boundary
- DTPE later carries receipt / ledger / verifier consequences if and when implemented under bounded repo rules

### B.4 What Sentinel does not replace

Sentinel does not replace:
- SPECTRE
- IAL
- DTPE
- BBIS

### B.5 Safe framing

Sentinel must be framed as:
- a proposed future integration profile
- subordinate to the public DTPE / IAL / SPECTRE architecture
- compatible with BBIS but not merged into core BBIS by default
- requiring explicit docs alignment before normative implementation claims

---

## PRIMARY ARCHITECTURE MAPPING

Use this mapping unless direct repo-file inspection forces a tighter variant:

- SPECTRE-SENTINEL -> future semantic / interception ingress layer
- IAL -> canonical semantic artifact layer -> owns the semantic objects Sentinel would have to emit in canonical form
- SPECTRE -> execution / mutation-bound evaluation layer -> evaluates IAL-defined semantic artifacts at the execution boundary
- DTPE -> canonical receipt / ledger / offline verifier evidence path
- BBIS -> continuity / conformance requirement across the full mutation path -> not replaced by Sentinel -> not implied solved by a detector, gateway, or ingress block alone

---

## C. CANONICAL OBJECT MODEL

### C.1 Core rule

Sentinel must not pass downstream only:
- a score
- a label
- an alert
- a detector verdict

Those are insufficient.

### C.2 Required future direction

The strongest future direction is:

BBIS-constrained Sentinel integration through IAL and SPECTRE.

That means:
- Sentinel should form or help form a canonical semantic object
- that object should live as an IAL-native artifact
- SPECTRE should evaluate that artifact at the mutation boundary
- later runtime / evidence integration must remain replayable, reconstructable, and verifier-checkable

### C.3 Minimal conceptual semantic object

The semantic object Sentinel must emit or help form should conceptually include:
- object identity
- semantic subject / target
- semantic findings
- semantic predicates asserted
- provenance / source of analysis
- scope of applicability
- mutation relevance or target-boundary relevance
- admissibility-relevant content
- canonical form suitable for IAL ownership
- integrity / crypto binding fields compatible with repo crypto direction
- replay-sufficient structure

### C.4 How it maps into IAL

IAL conceptually owns:
- canonical semantic representation
- canonical field definitions
- canonical serialization / normalization rules
- semantic object identity
- semantic object admissibility structure

### C.5 What SPECTRE evaluates

SPECTRE evaluates:
- the IAL-defined semantic artifact
- at the execution / mutation boundary
- against still-governing admissibility predicates

### C.6 What later DTPE integration would require

Later receipt / ledger / verifier integration would require:
- semantic object identity persistence
- canonical object integrity carriage
- evaluation result persistence
- receipt extensions where needed
- ledger extensions where needed
- verifier replay rules where needed
- reconstructable linkage between Sentinel-origin semantic artifact and SPECTRE boundary decision

---

## D. DO / DO NOT / MUST / MUST NOT

### D.1 DO

- DO keep Sentinel subordinate to DTPE / IAL / SPECTRE.
- DO keep it future integration until BBIS is fully implemented.
- DO require canonical semantic artifacts rather than score-only downstream carry-forward.
- DO preserve replayability, reconstructability, and verifier-compatibility.
- DO require docs alignment.
- DO require README alignment.
- DO keep claims path-bounded and mutation-bounded.
- DO preserve PQC / crypto-agility compatibility with current repo direction.
- DO preserve offline verification posture.
- DO state what Sentinel integration solves.
- DO state what Sentinel integration does not solve.
- DO explicitly name non-goals.

### D.2 DO NOT

- DO NOT imply Sentinel runtime authorization from IAL positioning.
- DO NOT present a detector as equivalent to BBIS.
- DO NOT collapse execution-bound enforcement and mutation-bound continuity.
- DO NOT replace SPECTRE with Sentinel.
- DO NOT create public architectural contradictions across docs.
- DO NOT treat ingress blocking as proof of boundary-to-boundary invariant survival.
- DO NOT treat semantic analysis alone as mutation-bound enforcement.
- DO NOT imply future integration equals current normalized runtime layer.

### D.3 MUST

- MUST keep claims path-bounded and mutation-bounded.
- MUST require canonical semantic objects, not score-only carry-forward.
- MUST keep PQC / crypto-agility posture compatible with current repo direction.
- MUST preserve offline verification posture.
- MUST avoid silent semantic substitution.
- MUST identify any new receipt / ledger / verifier impacts before claiming integration completeness.
- MUST require full docs alignment and README alignment before normative publication.
- MUST explicitly define non-goals.
- MUST keep Sentinel future-only until BBIS is complete.

### D.4 MUST NOT

- MUST NOT claim Sentinel already closes BBIS.
- MUST NOT claim Sentinel already normalizes public runtime architecture.
- MUST NOT imply IAL alone authorizes Sentinel runtime integration.
- MUST NOT present README or public docs in contradictory terms once Sentinel wording is added.
- MUST NOT claim verifier compatibility unless receipt / ledger / replay surfaces are explicitly extended accordingly.

---

## E. WHAT IT SOLVES

A bounded future Sentinel integration can solve or improve:
- stronger semantic / interception ingress posture
- canonical semantic artifact formation pressure
- a cleaner bridge from semantic analysis to mutation governance
- stronger front-side refusal conditions before mutation
- a cleaner future path for BBIS-constrained semantic governance
- a better bridge from semantic ingress to SPECTRE boundary evaluation
- a cleaner future path into DTPE receipt / ledger / verifier surfaces

---

## F. WHAT IT DOES NOT SOLVE

A bounded future Sentinel integration does not solve:
- BBIS completion
- boundary-to-boundary invariant survival by itself
- mutation-bound enforcement at the true irreversible primitive by itself
- replacement of SPECTRE
- runtime authorization by implication
- verifier integration by itself unless receipt / ledger / replay surfaces are extended accordingly
- downstream continuity merely because ingress blocking exists
- execution-bound governance merely because semantic analysis occurred earlier
- proof that the named ingress point is the true mutation authority
- universal path closure

---

## G. IMPLEMENTATION NOTES

### G.1 New artifact classes needed

Conceptually, Sentinel future integration needs at least:
- Sentinel-origin semantic ingress artifact
- IAL-native canonical semantic object definition or extension point
- SPECTRE evaluation binding for that object
- receipt impact notes
- ledger impact notes
- verifier replay notes

### G.2 Where they should live conceptually

- Sentinel-origin analysis should live at the future ingress / interception layer
- canonical semantic object definition should live in IAL
- boundary evaluation should live in SPECTRE
- receipt / ledger / offline verification effects should live in DTPE evidence surfaces

### G.3 Existing surfaces they would touch

Conceptually, they would touch:
- IAL semantic artifact schema or canonical object layer
- SPECTRE boundary evaluation inputs
- DTPE receipt / ledger / verifier evidence chain
- docs / README / architecture overview surfaces
- mutation-authority documentation surfaces
- execution-integrity wording surfaces

### G.4 What should remain future-only until BBIS is complete

The following should remain future-only:
- normative runtime Sentinel layer claims
- public claim that Sentinel is an already-authorized execution surface
- broad BBIS closure language
- any claim that ingress blocking equals full mutation-bound continuity
- any claim that verifier integration is complete before receipt / ledger / replay impacts are defined

---

## H. DOCS ALIGNMENT PLAN

### H.1 Files to inspect

Minimum required:
- `README.md`
- `docs/ARCHITECTURE_OVERVIEW.md`
- `docs/EXECUTION_INTEGRITY_MODEL.md`
- `docs/BOUNDARY_INTEGRITY_AND_MUTATION_AUTHORITY.md`
- `docs/IAL_SPEC.md`

Other docs must also be inspected if they:
- describe DTPE / IAL / SPECTRE responsibilities
- imply runtime authorization
- describe semantic artifacts
- describe mutation authority
- describe verifier / receipt / replay semantics

### H.2 Contradictions to resolve

At minimum, resolve contradictions around:
- whether Sentinel is current runtime or future integration only
- whether IAL implies runtime authorization
- whether SPECTRE remains the execution / mutation-bound evaluator
- whether BBIS is being collapsed into ingress detection
- whether DTPE evidence responsibilities remain distinct
- whether public wording implies completion rather than proposal

### H.3 Wording to normalize

Normalize wording so that:
- Sentinel = future integration profile
- IAL = canonical semantic artifact layer
- SPECTRE = execution / mutation-bound evaluation layer
- DTPE = canonical receipt / ledger / offline verifier evidence path
- BBIS = continuity / conformance requirement across the full mutation path

### H.4 README changes required

README must be checked and updated if needed so that:
- Sentinel is not implied as already-normalized runtime surface
- DTPE / IAL / SPECTRE responsibilities remain consistent
- future-integration wording is explicit
- BBIS is not accidentally collapsed into Sentinel
- any IAL naming mismatch is either resolved or explicitly bounded and explained

### H.5 Public naming mismatches to address

At minimum:
- any visible mismatch around IAL naming
- any wording that treats semantic ingress as execution-bound enforcement
- any wording that implies Sentinel already exists as a current normalized public architecture layer

---

## I. REPO SAFETY RULE

Any proposed Sentinel wording must be checked against the current public repo language before being treated as normative.

That means:
- this package is safe only as a future-integration package
- any stronger public claim requires direct repo-file verification
- any implementation claim requires explicit repo-surface alignment
- any README or docs wording must be checked for contradiction before merge
- Sentinel must remain future integration until BBIS is completely implemented

---

## Final bounded future-integration package summary

This spec keeps the repo-safe position as:

- Sentinel is a future semantic / interception ingress layer
- Sentinel feeds IAL-native canonical semantic artifacts
- SPECTRE remains the execution / mutation-bound evaluator
- DTPE remains the canonical receipt / ledger / offline verifier path
- BBIS remains the continuity requirement and is not replaced by Sentinel
- docs alignment is required
- README alignment is required
- runtime authorization is not implied
- verifier completeness is not implied
- future integration is safe only if path-bounded, mutation-bounded, replayable, reconstructable, verifier-compatible, and docs-aligned