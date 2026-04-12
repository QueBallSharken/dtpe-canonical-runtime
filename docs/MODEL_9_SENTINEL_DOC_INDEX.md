# MODEL 9 / SPECTRE-SENTINEL DOCUMENT INDEX

## Status

This file is the entry-point index for the bounded Model 9 / SPECTRE-SENTINEL documentation set.

It exists to:
- give the repo a single navigation point
- identify the canonical document set
- define reading order
- define usage order
- distinguish architecture, acceptance, and implementation artifacts
- preserve the bounded first-target ceiling

This file is index-only.

It does not broaden claims.
It does not replace the underlying canonical documents.
It does not authorize implementation by itself.

---

## 1. Governing Split

Use this exact split:

- BBIS = conformance lens
- DTPE / IAL / SPECTRE / SPECTRE-SENTINEL = architecture capable of satisfying that lens in bounded form

Do not merge them conceptually.

---

## 2. Standing Architectural Requirement

PQC must be on and always at the ready.

This requirement applies across the full document set.

That means:
- PQC readiness is active, not decorative
- claim-relevant crypto posture must be surfaced where applicable
- unsupported or mismatched claim-relevant crypto posture must fail closed or downgrade
- bounded first-target work must not be structured as if PQC can be deferred without consequence

---

## 3. Canonical Document Set

### 3.1 Consolidation Seed

- `docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md`
  - temporary canonical seed preserving the original thread-derived architecture record
  - use for provenance and recovery
  - do not treat as the preferred day-to-day entry point now that the split set exists

### 3.2 Model Core

- `docs/MODEL_9_TIGHTENING_SPEC.md`
  - tightened definition of Model 9
  - defines bounded active accompaniment
  - defines non-claim boundary

- `docs/MODEL_9_TO_DTPE_IAL_SPECTRE_MAPPING.md`
  - maps tightened Model 9 into DTPE / IAL / SPECTRE / SPECTRE-SENTINEL
  - defines required enforcement and evidence surfaces

- `docs/MODEL_9_CONFORMANCE_AND_CLASSIFICATION_RULES.md`
  - defines conformance conditions
  - defines classification states
  - defines downgrade semantics

### 3.3 Sentinel Architecture Core

- `docs/MODEL_9_SENTINEL_STATE_MODEL.md`
  - defines required states
  - defines transition and downgrade events
  - defines state-loss to classification-loss mapping

- `docs/MODEL_9_SENTINEL_EVIDENCE_SCHEMA.md`
  - defines required evidence categories
  - defines mandatory evidence by state and classification
  - defines replay input expectations

- `docs/MODEL_9_SENTINEL_REPLAY_RULES.md`
  - defines replay ordering
  - defines replay sufficiency and downgrade rules
  - defines replay pass/fail logic

- `docs/MODEL_9_SENTINEL_MINIMAL_ARCHITECTURE_PROFILE.md`
  - defines minimum architecture capability tiers
  - defines first meaningful bounded incorporation threshold

### 3.4 First-Target Package

- `docs/MODEL_9_SENTINEL_FIRST_INCORPORATION_TARGET.md`
  - defines the exact first bounded target

- `docs/MODEL_9_SENTINEL_FIRST_TARGET_ACCEPTANCE_RULES.md`
  - defines exact pass/fail rules for first-target acceptance

- `docs/MODEL_9_SENTINEL_FIRST_TARGET_IMPLEMENTATION_CHECKLIST.md`
  - defines mandatory implementation surfaces and completion criteria

- `docs/MODEL_9_SENTINEL_FIRST_TARGET_PROOF_HARNESS_OUTLINE.md`
  - defines required proof structure and mandatory scenario types

- `docs/MODEL_9_SENTINEL_FIRST_TARGET_TEST_CASE_CATALOG.md`
  - defines concrete test cases and expected outcomes

- `docs/MODEL_9_SENTINEL_FIRST_TARGET_PHASED_IMPLEMENTATION_PLAN.md`
  - defines phased build order and phase gates

---

## 4. Reading Order

Use this reading order if starting fresh:

1. `docs/MODEL_9_TIGHTENING_SPEC.md`
2. `docs/MODEL_9_TO_DTPE_IAL_SPECTRE_MAPPING.md`
3. `docs/MODEL_9_CONFORMANCE_AND_CLASSIFICATION_RULES.md`
4. `docs/MODEL_9_SENTINEL_STATE_MODEL.md`
5. `docs/MODEL_9_SENTINEL_EVIDENCE_SCHEMA.md`
6. `docs/MODEL_9_SENTINEL_REPLAY_RULES.md`
7. `docs/MODEL_9_SENTINEL_MINIMAL_ARCHITECTURE_PROFILE.md`
8. `docs/MODEL_9_SENTINEL_FIRST_INCORPORATION_TARGET.md`
9. `docs/MODEL_9_SENTINEL_FIRST_TARGET_ACCEPTANCE_RULES.md`
10. `docs/MODEL_9_SENTINEL_FIRST_TARGET_IMPLEMENTATION_CHECKLIST.md`
11. `docs/MODEL_9_SENTINEL_FIRST_TARGET_PROOF_HARNESS_OUTLINE.md`
12. `docs/MODEL_9_SENTINEL_FIRST_TARGET_TEST_CASE_CATALOG.md`
13. `docs/MODEL_9_SENTINEL_FIRST_TARGET_PHASED_IMPLEMENTATION_PLAN.md`

Use the consolidation seed only if you need provenance or recovery:
- `docs/MODEL_9_SENTINEL_THREAD_CONSOLIDATION.md`

---

## 5. Usage Order

Use this order when doing actual work:

### 5.1 Architecture definition
- `docs/MODEL_9_TIGHTENING_SPEC.md`
- `docs/MODEL_9_TO_DTPE_IAL_SPECTRE_MAPPING.md`
- `docs/MODEL_9_CONFORMANCE_AND_CLASSIFICATION_RULES.md`

### 5.2 Sentinel architecture surfaces
- `docs/MODEL_9_SENTINEL_STATE_MODEL.md`
- `docs/MODEL_9_SENTINEL_EVIDENCE_SCHEMA.md`
- `docs/MODEL_9_SENTINEL_REPLAY_RULES.md`
- `docs/MODEL_9_SENTINEL_MINIMAL_ARCHITECTURE_PROFILE.md`

### 5.3 First-target build and acceptance
- `docs/MODEL_9_SENTINEL_FIRST_INCORPORATION_TARGET.md`
- `docs/MODEL_9_SENTINEL_FIRST_TARGET_ACCEPTANCE_RULES.md`
- `docs/MODEL_9_SENTINEL_FIRST_TARGET_IMPLEMENTATION_CHECKLIST.md`
- `docs/MODEL_9_SENTINEL_FIRST_TARGET_PROOF_HARNESS_OUTLINE.md`
- `docs/MODEL_9_SENTINEL_FIRST_TARGET_TEST_CASE_CATALOG.md`
- `docs/MODEL_9_SENTINEL_FIRST_TARGET_PHASED_IMPLEMENTATION_PLAN.md`

---

## 6. Bounded Claim Ceiling

The first-target package supports only:

- bounded single-segment accompaniment
- one covered mutation-capable boundary
- replay-verifiable bounded classification
- fail-closed downgrade discipline
- claim-relevant crypto handling where applicable
- PQC-ready posture preserved as an active requirement

It does not support claims of:
- full Model 9 implementation
- end-to-end accompaniment
- universal downstream continuity
- full BBIS closure
- full PQC migration completion
- full crypto-agility completion

---

## 7. Practical Repo Rule

For this work, authority order is:

1. canonical repo docs
2. acceptance and test artifacts
3. implementation artifacts
4. thread history only as provenance

Do not allow the thread to become the source of truth again.

---

## 8. Recommended Next Step

The canonical split set is complete.

The next useful move should be one of:

- repo-specific implementation planning
- repo-specific work breakdown structure
- runnable test planning from the test case catalog
- issue/task decomposition against the first-target checklist

Choose one and keep the bounded first-target ceiling intact.

---

## 9. Maintenance Rule

If a future artifact changes:
- Model 9 meaning
- classification semantics
- first-target ceiling
- required replay behavior
- required crypto handling
- PQC readiness posture

then this index should be updated to keep navigation and interpretation accurate.