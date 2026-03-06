DTPE CANONICAL RUNTIME CHARTER

Purpose
Build a clean runtime where execution-time authority is recomputed, not inherited.

Primary guarantee
Execution cannot inherit authority.
Authority must resolve at the moment the system acts.

Non-negotiable properties
1. Deterministic serialization
2. Deterministic hashing
3. No mutation before admissibility decision
4. Refusal must be explicit and deterministic
5. Offline verification must reconstruct from exported artifacts alone
6. Identity drift must fail fast
7. No authority material duplicated without equality checks

Out of scope
1. UI polish
2. Optimization
3. Multi-node complexity
4. Convenience shortcuts that bypass invariants
