"""Present a saved fictional SPECTRE-FST receipt."""

import argparse
import json
import sys

from dtpe_offline_receipts.present import publish, read_native

from .offline_input import DIGEST, FormatError, Unsupported, decode, sha
from .offline_profile import check, facts
from .receipt_schema import get_minimal_receipt_hash


def build(raw, expected):
    digest = sha(raw) if raw is not None else None
    receipt = None
    native_digest = None
    diagnostic = None
    if raw is None:
        diagnostic = ("UNAVAILABLE", "Input is missing or cannot be read safely.")
    elif expected is not None and digest != expected:
        diagnostic = ("REJECTED", "Raw SHA-256 differs from the supplied expectation.")
    else:
        try:
            document = decode(raw)
            check(document)
            native_digest = get_minimal_receipt_hash(document)
            receipt = document
        except Unsupported as error:
            diagnostic = ("UNSUPPORTED", str(error))
        except FormatError as error:
            diagnostic = ("MALFORMED", str(error))
    state = "COMPLETE" if receipt is not None else "DIAGNOSTIC_ONLY"
    checks = facts(digest, expected, native_digest)
    checks["native_profile_check"] = "MATCH" if receipt is not None else (
        diagnostic[0] if diagnostic[0] in {"MALFORMED", "UNSUPPORTED"} else "NOT_CHECKED"
    )
    view = dict(format="spectre-fst.saved-receipt-presentation.1", state=state,
                origin="FIXTURE", boundary="Fictional paper-token workflow",
                recorded_assessment=receipt, local_checks=checks,
                evidence_assessment=dict(validity="NOT_CHECKED", source_execution="NOT_CHECKED"),
                diagnostic=None if diagnostic is None else dict(
                    status=diagnostic[0], reason=diagnostic[1]),
                native_file="native.json" if raw is not None else None)
    machine = json.dumps(view, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    plain = "SPECTRE-FST recorded assessment and local checks\n" + machine
    files = {"receipt.json": machine.encode("ascii"), "receipt.txt": plain.encode("ascii")}
    if raw is not None:
        files["native.json"] = raw
    return files, state


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intake", required=True)
    parser.add_argument("--native", required=True)
    parser.add_argument("--origin", required=True, choices=("fixture",))
    parser.add_argument("--expected-native-sha256")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    expected = args.expected_native_sha256
    if expected is not None and not DIGEST.fullmatch(expected):
        parser.error("Expected native digest must have 64 lowercase hex digits.")
    try:
        raw = read_native(args.intake, args.native)
    except OSError:
        raw = None
    try:
        files, state = build(raw, expected)
        publish(args.output, files)
    except OSError:
        print("Presentation publication failed. Check the fresh local output path.", file=sys.stderr)
        return 1
    print(f"{state}: SPECTRE-FST presentation written.")
    return 0 if state == "COMPLETE" else 2


if __name__ == "__main__":
    sys.exit(main())
