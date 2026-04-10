# IAL - INVARIANT ASSERTION LAYER SPEC

## PURPOSE

IAL defines the canonical semantic artifact layer inside DTPE.

IAL exists so that replay, reconstruction, and later mutation-integrity work operate over explicit canonical objects rather than inferred behavior.

---

## WHAT IAL DEFINES

IAL defines canonical semantic artifacts that express what DTPE governs.

IAL answers:

- what authority is being asserted
- what invariant is being preserved
- what semantic object is being evaluated
- what evidence object must remain replayable and reconstructable

IAL therefore defines semantic artifact classes such as:

- authority-bearing objects
- invariant-bearing objects
- transition-semantic objects
- evidence-binding semantic objects

---

## CURRENT REPOSITORY POSITION

IAL is positioned architecturally in the current repository.

That positioning does not require a complete standalone IAL runtime package to be valid.

Safe current wording is:

- IAL is part of the DTPE architecture model
- IAL defines semantic objects that DTPE governs
- IAL positioning is current
- broad standalone IAL runtime implementation is not implied by this document

---

## REQUIRED PROPERTIES OF IAL ARTIFACTS

IAL artifacts must be:

- canonical
- explicit
- replayable
- suitable for receipt binding
- suitable for ledger binding
- suitable for verifier reconstruction
- crypto-neutral at the semantic layer

IAL artifacts must be canonically serializable before they can be safely bound into governance evidence.

---

## RELATION TO DTPE

DTPE is the umbrella governance architecture.

IAL defines the semantic object space that DTPE governs.

DTPE then binds governance evaluation into canonical evidence paths such as:

- receipt material
- ledger payload
- verifier reconstruction

---

## RELATION TO SPECTRE

SPECTRE evaluates IAL-defined semantic artifacts at the execution boundary.

IAL defines the semantic object.
SPECTRE evaluates whether it holds.

IAL does not own mutation authority.
IAL does not replace receipt, ledger, or verifier evidence.

---

## CURRENT BOUNDED PHASE RULE

IAL positioning does not authorize phase expansion by itself.

In particular, this document does not authorize:

- Phase 8 structure changes
- Phase 9 runtime expansion by implication
- Phase 10 runtime work
- Sentinel runtime work

IAL remains the semantic layer that makes DTPE governance more explicit, replayable, and eventually reconstructable without semantic guesswork.

END OF FILE