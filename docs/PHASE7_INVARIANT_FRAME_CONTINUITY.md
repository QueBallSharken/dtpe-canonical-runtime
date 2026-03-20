DTPE / IAL / SPECTRE - PHASE 7 (INVARIANT-FRAME + TEMPORAL CONTINUITY)
COMPLETE FINAL LOCKED SPEC (PQC-SAFE)

PURPOSE

Phase 7 enforces:

"A sequence of individually valid decisions must remain globally coherent by proving that each decision was produced under the same canonical invariant frame, or under an explicitly authorized invariant-frame transition, and that the sequence remains temporally ordered and replay-verifiable across decisions."

This prevents:

- frame fragmentation
- cross-decision drift
- locally valid but globally misaligned trajectories
- interpretive drift across execution boundaries
- silent policy/context evolution between decisions
- out-of-order execution across otherwise valid decisions
- replay of sequence steps in invalid temporal order

----------------------------------------------------------------
CORE INVARIANT
----------------------------------------------------------------

Sequence coherence must be:

- evaluated at execution boundary
- recorded in receipt
- stored in ledger
- replayed by verifier
- compared deterministically across decisions

Continuity has two required dimensions:

1. FRAME CONTINUITY
   The governing frame must remain identical across decisions,
   or change only under an explicitly authorized canonical transition.

2. TEMPORAL CONTINUITY
   The sequence must remain temporally ordered and auditable across decisions.

No implicit continuity.
No runtime memory.
No inferred alignment.
No hidden timeline.
No "similar enough" equivalence.

Continuity must be explicitly proven from canonical inputs.

----------------------------------------------------------------
CRITICAL RULE
----------------------------------------------------------------

Frame continuity and temporal continuity are canonical input relations.

The system MUST NOT:

- infer continuity from descriptive fields
- rely on runtime memory
- assume prior context persists
- treat approximate state as continuity
- infer time ordering from ambient clock state
- reset continuity silently by omitting prior linkage

The system MUST:

- bind each decision to a deterministic invariant_frame_hash
- bind each decision to explicit prior linkage when continuity is required
- enforce exact frame continuity OR explicit authorized transition
- enforce deterministic temporal ordering across linked decisions
- persist all continuity evidence in the receipt

----------------------------------------------------------------
SECTION 1 - INVARIANT FRAME (LOCKED SOURCE)
----------------------------------------------------------------

The invariant frame is a canonical structure derived ONLY from governance-defining inputs.

Minimum canonical inputs:

invariant_frame = {
  "policy_hash": str,
  "authority_hash": str,
  "execution_intent": str,
  "constraint_profile": str,
  "temporal_rule_profile": str
}

RULES:

- must be fully deterministic
- must exclude runtime-only values
- must exclude implicit context
- must use canonical JSON (sorted keys, UTF-8)
- must not duplicate crypto internals beyond existing canonical hashes

PROFILE SOURCE RULE (LOCKED)

constraint_profile and temporal_rule_profile MUST each be:

- explicitly recorded canonical values
  OR
- deterministically derived from documented canonical functions over recorded inputs

They MUST NOT be:

- runtime-only configuration
- UI labels
- inferred system state
- unstored memory artifacts
- environment-dependent values

If not already first-class canonical inputs, they MUST be defined and documented before use in invariant frame construction.

----------------------------------------------------------------
SECTION 2 - CANONICAL HASH
----------------------------------------------------------------

invariant_frame_hash = SHA256(canonical_json(invariant_frame))

PROPERTIES:

- deterministic
- reproducible offline
- independent of runtime environment
- independent of crypto algorithm selection

----------------------------------------------------------------
SECTION 3 - SEQUENCE SCOPE (FULLY LOCKED)
----------------------------------------------------------------

Continuity is evaluated ONLY within a deterministic sequence scope.

DEFINE:

sequence_scope = {
  "authority_hash": authority_hash,
  "execution_intent": execution_intent
}

sequence_id = SHA256(canonical_json(sequence_scope))

RULES:

- sequence_id MUST be computed deterministically
- sequence_id MUST be stored in receipt
- continuity comparisons ONLY occur within same sequence_id
- cross-sequence continuity is INVALID and MUST NOT be evaluated

PRIOR LINKAGE RULE (LOCKED)

When continuity is required:

- prior_invariant_frame_hash MUST be explicit
- prior_execution_time MUST be explicit
- prior linkage MUST refer to a previously recorded receipt in the same sequence_id

Verifier MUST:

- confirm referenced prior receipt exists
- confirm prior receipt belongs to same sequence_id
- NOT infer alternate prior frames
- NOT perform implicit sequence discovery beyond explicit prior linkage

Initial implementation MUST:

- rely on explicit prior linkage only
- NOT use runtime context
- NOT infer "closest previous" record heuristically

----------------------------------------------------------------
SECTION 4 - INITIAL FRAME (BOOTSTRAP RULE)
----------------------------------------------------------------

initial_frame is valid ONLY if one of the following holds:

1. continuity_required == false
2. no prior governed decision exists in same sequence_id
3. canonical bootstrap rule explicitly permits new chain creation

Otherwise:

- missing prior_invariant_frame_hash MUST FAIL
- missing prior_execution_time MUST FAIL

No silent resets allowed.

----------------------------------------------------------------
SECTION 5 - AUTHORIZED FRAME TRANSITION (FULLY DEFINED)
----------------------------------------------------------------

Authorized invariant-frame transition MUST be determined by a canonical rule.

transition_authorized MUST:

- be derived from recorded inputs only
- be deterministic
- be reproducible by verifier

INITIAL LOCKED MODES:

1. DISABLED MODE (DEFAULT)
   - any frame mismatch -> FAIL
   - transition_authorized = false

2. EXPLICIT_MAP MODE (OPTIONAL)
   - mismatch passes ONLY if transition exists in canonical allowed-transition map
   - map MUST be:
     - recorded
     - deterministic
     - replayable
     - policy-governed

POLICY GOVERNANCE OF TRANSITIONS (LOCKED)

Authorized transitions MUST be governed by:

- canonical policy state
  OR
- canonical transition map bound to recorded artifacts

Runtime configuration MUST NOT authorize transitions.

Verifier MUST reconstruct authorization from recorded data only.

If EXPLICIT_MAP mode is not implemented:
- all frame mismatches MUST be treated as unauthorized

----------------------------------------------------------------
SECTION 6 - TEMPORAL CONTINUITY (LOCKED)
----------------------------------------------------------------

Temporal continuity is distinct from Phase 6 temporal admissibility.

Phase 6 answers:
- "Is this decision temporally valid at execution time?"

Phase 7 temporal continuity answers:
- "Is this decision temporally ordered and coherent relative to the prior decision in the same sequence?"

TEMPORAL CONTINUITY RULE

For linked decisions within same sequence_id:

current.execution_time MUST be >= prior.execution_time

If:
current.execution_time < prior.execution_time
-> temporal continuity FAILS

This ordering check is mandatory.

OPTIONAL STRONGER RULE (allowed if canonically defined):
current.execution_time MUST also satisfy any recorded sequence-level temporal continuity constraints derived from temporal_rule_profile

If stronger rule is not implemented:
minimum monotonic ordering rule is still REQUIRED.

No backward time movement allowed within a continuity chain.

----------------------------------------------------------------
SECTION 7 - RESULT STRUCTURE (FINAL)
----------------------------------------------------------------

frame_continuity_result = {
  "ok": bool,
  "reason": str,
  "continuity_mode": str,
  "current_invariant_frame_hash": str,
  "prior_invariant_frame_hash": str | None,
  "transition_authorized": bool,
  "sequence_id": str,
  "prior_execution_time": str | None,
  "current_execution_time": str,
  "temporal_continuity_ok": bool
}

----------------------------------------------------------------
CONTINUITY MODES (CANONICAL ENUM)
----------------------------------------------------------------

- "INITIAL"
- "EXACT"
- "AUTHORIZED_TRANSITION"
- "VIOLATION"

NO OTHER VALUES PERMITTED

----------------------------------------------------------------
REASON CODES (STRICT)
----------------------------------------------------------------

- "initial_frame"
- "frame_continuity_ok"
- "authorized_frame_transition"
- "unauthorized_frame_transition"
- "frame_mismatch"
- "missing_prior_frame_hash"
- "missing_prior_execution_time"
- "missing_prior_linkage"
- "sequence_violation"
- "temporal_order_violation"

No free-form reason strings allowed.

----------------------------------------------------------------
SECTION 8 - ARCHITECTURE FLOW
----------------------------------------------------------------

INPUT
->
pipeline
->
boundary
- authority_result
- state_admissibility_result
- stability_result
- temporal_invariant_result
- frame_continuity_result
->
decision
->
receipt
->
ledger
->
verifier
- reconstruct invariant_frame
- recompute invariant_frame_hash
- validate frame continuity
- validate temporal continuity
- compare stored vs recomputed results

----------------------------------------------------------------
SECTION 9 - FRAME CONTINUITY GUARD
----------------------------------------------------------------

FILE:
core/spectre/frame_continuity.py

RESPONSIBILITY:

- construct canonical invariant frame
- compute invariant_frame_hash
- validate sequence scope
- compare with prior frame
- validate authorized transition rule
- validate temporal continuity across linked decisions
- return deterministic result structure

INPUT:

- policy_hash
- authority_hash
- execution_intent
- constraint_profile
- temporal_rule_profile
- current_execution_time
- prior_invariant_frame_hash (if required)
- prior_execution_time (if required)
- continuity_required
- canonical transition map or policy-governed transition artifact (if enabled)

RULES:

- no crypto signing logic
- no runtime memory
- no implicit context
- no ambient clock reads
- deterministic only

----------------------------------------------------------------
SECTION 10 - BOUNDARY INTEGRATION
----------------------------------------------------------------

FILE:
core/spectre/boundary.py

OLD:
allowed =
  authority_ok AND state_ok AND stability_ok AND temporal_ok

NEW:
allowed =
  authority_ok
  AND state_ok
  AND stability_ok
  AND temporal_ok
  AND frame_continuity_ok
  AND temporal_continuity_ok

WHERE:

frame_continuity_ok =
  (continuity_mode == "INITIAL")
  OR (continuity_mode == "EXACT")
  OR (continuity_mode == "AUTHORIZED_TRANSITION")

temporal_continuity_ok =
  frame_continuity_result["temporal_continuity_ok"] == true

RETURN MUST INCLUDE:

- frame_continuity_result
- invariant_frame_hash
- prior_invariant_frame_hash
- sequence_id

----------------------------------------------------------------
SECTION 11 - PIPELINE INTEGRATION
----------------------------------------------------------------

FILE:
core/phase4/pipeline.py

REQUIREMENTS:

- MUST pass prior_invariant_frame_hash explicitly when continuity_required is true
- MUST pass prior_execution_time explicitly when continuity_required is true
- MUST pass current execution_time (already required by Phase 6)
- MUST NOT infer prior state
- MUST NOT use runtime memory
- MUST NOT use ambient clock state

If continuity_required is false:
- initial_frame handling is permitted under bootstrap rules only

----------------------------------------------------------------
SECTION 12 - RECEIPT
----------------------------------------------------------------

FILE:
core/phase4/receipt.py

Receipt MUST include:

- invariant_frame_hash
- prior_invariant_frame_hash
- frame_continuity_result
- continuity_mode
- sequence_id
- prior_execution_time
- current_execution_time

Receipt MUST remain canonical JSON.

----------------------------------------------------------------
SECTION 13 - LEDGER
----------------------------------------------------------------

Ledger MUST store:

- invariant_frame_hash
- prior_invariant_frame_hash
- frame_continuity_result
- sequence_id
- prior_execution_time
- current_execution_time

Ledger append behavior remains deterministic.

----------------------------------------------------------------
SECTION 14 - VERIFIER (CRITICAL)
----------------------------------------------------------------

FILE:
tools/verify_ledger.py

FRAME RECONSTRUCTION RULE

Verifier MUST:

- reconstruct invariant_frame
- canonicalize it
- recompute invariant_frame_hash
- compare to recorded hash

Verifier MUST NOT trust stored hash alone.

CONTINUITY CHECK

Verifier MUST:

- validate sequence_id deterministically
- validate prior linkage exists
- validate prior receipt belongs to same sequence_id
- recompute transition authorization
- recompute continuity_mode
- recompute temporal continuity
- compare stored vs recomputed result

FAILURE CONDITIONS

If invariant_frame_hash mismatch:
raise RuntimeError("invariant_frame continuity mismatch")

If unauthorized transition:
raise RuntimeError("unauthorized frame transition")

If temporal continuity mismatch:
raise RuntimeError("temporal continuity mismatch")

If sequence mismatch:
raise RuntimeError("sequence continuity mismatch")

----------------------------------------------------------------
SECTION 15 - TESTS
----------------------------------------------------------------

1. FRAME GUARD TEST
tools/test_phase7_frame_continuity.py

Must verify:

- initial frame passes only under bootstrap conditions
- identical frames pass
- mismatched frames fail in DISABLED mode
- authorized transition passes only under EXPLICIT_MAP mode
- missing prior hash fails when required
- missing prior execution_time fails when required
- temporal order violation fails
- reason codes correct
- continuity_mode correct

2. BOUNDARY TEST
tools/test_phase7_boundary_frame_path.py

Must verify:

- continuity success -> allow
- frame continuity failure -> refusal
- temporal continuity failure -> refusal
- result present

3. PIPELINE TEST

Must verify:

- receipt contains Phase 7 fields
- current_execution_time present
- prior_execution_time present when required
- crypto_profile unchanged

4. REPLAY VERIFIER TEST
tools/test_phase7_replay_verifier.py

Must verify:

- sequence continuity enforced
- mismatch triggers hard failure
- verifier recomputes frame hash
- verifier recomputes temporal continuity

5. REFUSAL PATH TEST

Must verify:

- frame mismatch causes refusal
- unauthorized transition causes refusal
- temporal order violation causes refusal
- replay confirms exact refusal reason

----------------------------------------------------------------
SECTION 16 - SCHEMA
----------------------------------------------------------------

FILE:
docs/RECEIPT_SCHEMA_V3.md

ADD:

- invariant_frame_hash
- prior_invariant_frame_hash
- frame_continuity_result
- continuity_mode
- sequence_id
- prior_execution_time
- current_execution_time

----------------------------------------------------------------
SECTION 17 - PQC SAFETY (MANDATORY)
----------------------------------------------------------------

Phase 7 MUST NOT:

- modify crypto_profile
- introduce algorithm-specific logic
- alter signing format
- alter signature verification logic
- assume classical vs PQC differences

Phase 7 MUST:

- remain crypto-agnostic
- operate purely on canonical governance hashes
- preserve deterministic replay across crypto profiles

IMPORTANT:

invariant_frame_hash is NOT a signature.
It does NOT replace cryptographic verification.
It is strictly a governance continuity artifact.

----------------------------------------------------------------
SECTION 18 - FAILURE MODES TO AVOID
----------------------------------------------------------------

The system MUST reject:

- implicit sequence switching
- missing prior frame when one exists
- missing prior execution_time when continuity is required
- authority change during unauthorized transition
- non-deterministic frame construction
- runtime-derived continuity values
- cross-sequence comparisons
- temporal reordering within a sequence
- implicit initial-frame reset
- non-canonical transition authorization
- undefined profile sources

----------------------------------------------------------------
SECTION 19 - STRICT IMPLEMENTATION ORDER
----------------------------------------------------------------

1. frame_continuity guard + tests
2. boundary integration + tests
3. pipeline integration
4. receipt update
5. pipeline test (crypto unchanged)
6. verifier integration
7. replay verifier test
8. refusal path update
9. schema update

NO SKIPPING
NO MERGING STEPS

----------------------------------------------------------------
SECTION 20 - DEFINITION OF DONE
----------------------------------------------------------------

Phase 7 is complete ONLY if:

- invariant frame is canonical
- frame hash is deterministic
- sequence_id is deterministic and enforced
- prior linkage is explicit and unambiguous
- initial frame cannot be abused
- authorized transition rule is deterministic and policy-governed
- temporal continuity is enforced across sequence
- boundary enforces both frame and temporal continuity
- receipt stores all continuity evidence
- ledger contains all continuity evidence
- verifier reconstructs frame
- verifier reconstructs continuity
- refusal path is implemented
- schema updated
- PQC behavior unchanged
- crypto_profile unchanged

----------------------------------------------------------------
FINAL INVARIANT
----------------------------------------------------------------

Authority proves a decision is allowed.
Temporal proves it is valid at execution.
Invariant-frame continuity proves successive decisions belong to the same governing frame.
Temporal continuity proves that governing sequence remains ordered across time.

Together, they prove that a valid decision sequence remains the same governing system across decisions.

END OF PHASE 7 COMPLETE FINAL LOCK
