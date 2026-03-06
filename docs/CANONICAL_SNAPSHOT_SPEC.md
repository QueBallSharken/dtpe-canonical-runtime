CANONICAL SNAPSHOT SPEC

Policy snapshot fields
- policy_version
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
- authority_canonical
- authority_hash

Phase-4 execution envelope fields
- authority_hash_v4
- crypto_profile
- snapshot_hash

Rules
- JSON must use sort_keys=True
- JSON separators must be comma and colon with no extra spaces
- UTF-8 encoding
- SHA-256 for hashes unless explicitly versioned otherwise
