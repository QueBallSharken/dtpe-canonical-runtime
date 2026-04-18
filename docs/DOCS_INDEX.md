# DOCS INDEX

## PURPOSE

This index identifies the repository-authoritative read order for current implementation orientation.

Use the documents below first when establishing the current committed baseline.

---

## PRIMARY READ ORDER

1. `docs/CURRENT_IMPLEMENTATION_STATE.md`
2. `docs/PHASE8_PHASE9_SPEC.md`
3. `docs/DTPE_SYSTEM_MODEL.md`
4. `docs/SPECTRE_FST_TRIKE_MODEL.md`
5. `docs/IAL_SPEC.md`
6. `docs/SPECTRE_SUBSYSTEM_SPEC.md`
7. `docs/NEXT_IMPLEMENTATION_TARGET.md`
8. `docs/PROJECT_ROADMAP.md`

---

## WHAT THIS READ ORDER ESTABLISHES

This read order is intended to answer, in order:

1. what is committed now
2. what the bounded Phase 7 / 8 / 9 classification is
3. how DTPE, IAL, and SPECTRE relate
4. what the locked trike-model architecture direction is
5. what is future-only direction
6. what sequencing rule governs the next implementation target

---

## LOCKED SUPPORTING SPECS

After the primary read order, consult locked supporting specs as needed, including:

- `docs/SPECTRE_FST_TRIKE_MODEL.md`
- `docs/PHASE7_INVARIANT_FRAME_CONTINUITY.md`
- `docs/PHASE8_SIGNAL_PROFILE_SPEC.md`
- `docs/PHASE8_DECISION_SPACE_COMPOSITION_SPEC.md`
- `docs/PHASE9_EVALUATOR_INTEGRITY_SPEC.md`
- `docs/PHASE10_EXECUTION_INTEGRITY_SPEC.md`
- `docs/PHASE10_MUTATION_INTEGRITY_SPEC.md`

---

## DOCUMENT RULE

Repository-authoritative source documents must avoid:

- non-repository authority wording
- transient local-working-tree claims as durable repo truth
- contradictory bounded phase claims
- future-direction wording that implies current runtime implementation

END OF FILE
