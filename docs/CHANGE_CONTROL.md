CHANGE CONTROL

Purpose

This file defines how architectural and runtime changes must be controlled.

No contributor may change authority-bearing behavior casually.

------------------------------------------------

CHANGE CLASSES

Class A — Locked surfaces

These surfaces are architecture-defining and require explicit review before modification:

• canonical serialization rules
• hash algorithm or hash versioning
• identity derivation model
• identity invariant rules
• policy snapshot structure
• authority snapshot structure
• phase-4 decision semantics
• refusal semantics
• receipt structure
• ledger linkage rules
• offline verifier logic

Class B — Proof-required surfaces

These surfaces may be changed only if deterministic proof is provided in the same work unit:

• identity generation flow
• startup invariant verification
• policy recomputation logic
• authority recomputation logic
• execution boundary logic
• receipt hashing logic
• ledger append logic

Required proof must show that invariants still hold.

Class C — Low-risk surfaces

These may be changed without architectural review if system behavior is unchanged:

• comments
• formatting
• non-semantic documentation
• filenames that do not alter imports
• test descriptions
• error wording that does not change control flow

------------------------------------------------

MANDATORY RULE

No change to an authority-bearing path is valid unless the contributor also provides deterministic proof that the invariant set still holds.

------------------------------------------------

REQUIRED EVIDENCE FOR CLASS A OR B CHANGES

A valid change should include, where applicable:

• exact files changed
• reason for change
• invariant impact statement
• deterministic test results
• replay/verifier impact statement
• refusal-path impact statement

------------------------------------------------

DISALLOWED CHANGE PATTERNS

Contributors must not:

• change canonical field names without updating specs
• introduce new stored authority values without recomputation rules
• bypass invariant checks temporarily
• change refusal semantics without updating tests
• change signature handling without proving end-to-end behavior
• mutate runtime state before admissibility decision

------------------------------------------------

DEFAULT DECISION RULE

If uncertainty exists:

prefer refusal over silent acceptance  
prefer recomputation over trust  
prefer explicit proof over assumed correctness

------------------------------------------------

END
