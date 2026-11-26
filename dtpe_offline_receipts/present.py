"""Present a saved fictional DTPE runtime boundary receipt."""

import argparse
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile

from .profile import PROFILE, SOURCE_REVISION, assess, digest, result_fields


PORTABLE_NAME = re.compile(r"[A-Za-z0-9_.-]+")
DEVICE = re.compile(r"(CON|PRN|AUX|NUL|COM[0-9]|LPT[0-9])", re.IGNORECASE)
MAX_FILE = 1024 * 1024


def regular(path, kind):
    info = path.lstat()
    if not kind(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
        raise OSError("Expected a regular local entry without symlinks or reparse points.")


def local_directory(path):
    path = Path(path).absolute()
    if os.name == "nt" and str(path).startswith(chr(92) * 2):
        raise OSError("UNC paths are outside this pilot.")
    for parent in (*reversed(path.parents), path):
        regular(parent, stat.S_ISDIR)
    return path


def read_native(root, relative):
    parts = relative.split("/")
    if any(part in (".", "..") or not PORTABLE_NAME.fullmatch(part) or part.endswith(".")
           or DEVICE.fullmatch(part.split(".")[0]) for part in parts):
        raise OSError("Expected a portable relative intake path.")
    path = local_directory(root)
    for part in parts[:-1]:
        path /= part
        regular(path, stat.S_ISDIR)
    path /= parts[-1]
    regular(path, stat.S_ISREG)
    with path.open("rb") as stream:
        raw = stream.read(MAX_FILE + 1)
    if len(raw) > MAX_FILE:
        raise OSError("Input byte limit exceeded.")
    return raw


def build(raw, expected):
    document, claims, checks, diagnostics = assess(raw, expected)
    state = "DIAGNOSTIC_ONLY" if diagnostics else "COMPLETE"
    result = None if diagnostics else result_fields(document, claims, checks)
    view = {
        "format": "dtpe.saved-receipt-presentation.1",
        "profile": PROFILE,
        "profile_source_revision": SOURCE_REVISION,
        "origin": "FIXTURE",
        "state": state,
        "native_file": None if raw is None else "native.json",
        "native_receipt_id": None if result is None else document["receipt_hash"],
        "result": result,
        "declared_authority": None if result is None else claims,
        "integrity": checks,
        "diagnostics": [dict(code=code, status=status, reason=reason)
                        for code, status, reason in diagnostics],
        "limitations": [
            "Fictional saved data. The authority signature metadata describes only authority_canonical.",
            "Hashes describe distinct preimages. Authenticity and source execution remain unchecked.",
        ],
    }
    machine = json.dumps(view, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    plain = f"DTPE Canonical Runtime saved receipt — {state}\n" + machine
    files = {"receipt.json": machine.encode("ascii"), "receipt.txt": plain.encode("utf-8")}
    if raw is not None:
        files["native.json"] = raw
    return files, state


def publish(output, files):
    requested = Path(output)
    parent = local_directory(requested.parent)
    destination = parent / requested.name
    if not requested.name or requested.name == ".." or os.path.lexists(destination):
        raise OSError("Choose a fresh output directory.")
    lock = parent / (destination.name + ".publish-lock")
    lock.mkdir()
    try:
        with tempfile.TemporaryDirectory(prefix=".dt-", dir=parent) as scratch:
            candidate = Path(scratch) / "p"
            candidate.mkdir()
            for name, raw in files.items():
                (candidate / name).write_bytes(raw)
            if os.path.lexists(destination):
                raise OSError("Output already exists.")
            candidate.rename(destination)
    finally:
        lock.rmdir()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intake", required=True)
    parser.add_argument("--native", required=True)
    parser.add_argument("--origin", required=True, choices=("fixture",))
    parser.add_argument("--expected-native-sha256")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    expected = args.expected_native_sha256
    if expected is not None and not digest(expected):
        parser.error("Expected native digest must have 64 lowercase hex digits.")
    try:
        raw = read_native(args.intake, args.native)
    except OSError:
        raw = None
    try:
        files, state = build(raw, expected)
        publish(args.output, files)
    except OSError as error:
        print(f"Presentation publication failed: {error}", file=sys.stderr)
        return 1
    print(f"{state}: native DTPE offline receipt presentation written.")
    return 0 if state == "COMPLETE" else 2


if __name__ == "__main__":
    sys.exit(main())
