import argparse
import json

from core.identity.generator import generate_identity


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deterministic DTPE identity artifacts")
    parser.add_argument("--identity-id", required=True)
    parser.add_argument("--owner-id", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--expires-at", required=True)
    parser.add_argument("--overwrite", action="store_true")

    args = parser.parse_args()

    out = generate_identity(
        identity_id=args.identity_id,
        owner_id=args.owner_id,
        role=args.role,
        expires_at=args.expires_at,
        overwrite=args.overwrite,
    )

    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
