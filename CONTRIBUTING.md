# Contributing to DTPE

Thank you for your interest in contributing.

## Project Principles

DTPE is designed as a deterministic governance runtime. All contributions
must preserve the following invariants:

- deterministic execution
- canonical serialization
- cryptographic authority binding
- append-only ledger evidence
- independent offline verification

Changes that break deterministic replay or canonical verification are
not accepted.

## Development Guidelines

Contributors should ensure:

- runtime behavior remains deterministic
- canonical JSON serialization rules are preserved
- receipt and ledger verification remain reproducible
- cryptographic profile rules are enforced through policy

## Testing

All changes should allow the demonstration script to run successfully:

python -m tools.run_demo

Verification must produce:

PASS: verified ledger record(s)

## Discussion

Major architectural changes should be discussed before implementation.

DTPE is currently a research-stage deterministic governance runtime.
