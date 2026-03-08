CANONICAL SNAPSHOT SPEC

Policy snapshot fields
- policy_version
- crypto_profile
- permitted_crypto_profiles
- migration_window
- policy_canonical
- policy_state_hash

Authority snapshot fields
- identity_id
- owner_id
- intent
- action
- expires_at
- policy_version
- policy_state_hash
- crypto_profile
- authority_canonical
- authority_hash

Phase-4 execution envelope fields
- authority_hash_v4
- crypto_profile
- snapshot_hash

Receipt fields
- execution_state
- reason
- authority_hash
- policy_state_hash
- crypto_profile
- receipt_canonical
- receipt_hash

Rules
- JSON must use sort_keys=True
- JSON separators must be comma and colon with no extra spaces
- UTF-8 encoding
- SHA-256 for hashes unless explicitly versioned otherwise
- crypto_profile is mandatory in policy snapshot, authority snapshot, receipt, and replayable evidence
- permitted_crypto_profiles is mandatory in policy snapshot
- permitted_crypto_profiles must be a non-empty array of non-empty strings
- permitted_crypto_profiles must be deterministically ordered
- policy snapshot crypto_profile must be a member of permitted_crypto_profiles
- if runtime-enforced crypto_profile is not permitted by policy, execution state must be REFUSED_NON_BINDING
- migration_window is optional in policy snapshot
- if present, migration_window must be a JSON object
- migration_window must contain:
  - from_crypto_profile
  - to_crypto_profile
  - not_before
  - not_after
- from_crypto_profile and to_crypto_profile must be non-empty strings
- not_before and not_after must be ISO-8601 datetime strings
- not_before must be earlier than not_after
- from_crypto_profile and to_crypto_profile must both be members of permitted_crypto_profiles
- migration rules must be deterministic and replayable from policy snapshot content alone
- outside an active migration window, crypto_profile mismatch remains REFUSED_NON_BINDING
