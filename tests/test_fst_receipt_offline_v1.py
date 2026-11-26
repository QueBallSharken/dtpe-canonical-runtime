"""Exercise the DTPE FST offline presenter with saved fictional fixtures."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]
TARGET = "core.spectre.fst.present"
FIXTURES = Path("tests/fixtures/fst_receipt_v1")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def encode(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode()


def run(out, name, file, code, *, intake=FIXTURES, expected=None, dest=None, guarded=True):
    dest = dest or (out / name)
    cmd = [sys.executable, "-B", "-m", TARGET]
    if guarded:
        helper = ROOT / "tests/fst_offline_isolation.py"
        cmd = [sys.executable, "-I", "-B", str(helper), str(out), TARGET]
    cmd += ["--intake", str(intake), "--native", file, "--origin", "fixture", "--output", str(dest)]
    if expected is not None:
        cmd += ["--expected-native-sha256", expected]
    p = subprocess.run(cmd, cwd=ROOT, timeout=30, capture_output=True, text=True, encoding="utf-8")
    print(f"{name}: expected={code} actual={p.returncode}", flush=True)
    print(p.stdout + p.stderr, end="", flush=True)
    if p.returncode != code:
        raise AssertionError(f"{name}: expected {code}, got {p.returncode}")
    return dest


def members(path):
    return {p.relative_to(path): p.read_bytes() for p in path.rglob("*") if p.is_file()}


def preserved(path, raw):
    file = path / "native.json"
    assert file.read_bytes() == raw


def verify(out):
    base = ROOT / FIXTURES
    manifest = load(base / "manifest.json")
    assert (base / "partial.canonical.json").read_bytes() == encode(load(base / "partial.json"))
    for name, fixture in manifest["fixtures"].items():
        raw = (base / name).read_bytes()
        obj = json.loads(raw)
        assert sha(raw) == fixture["raw_sha256"]
        assert sha(encode(obj)) == fixture["native_canonical_sha256"]
        dest = run(out, Path(name).stem, name, 0, expected=sha(raw))
        preserved(dest, raw)
        view = load(dest / "receipt.json")
        checks = view["local_checks"]
        assert checks["raw_native_sha256"] == sha(raw)
        assert checks["native_canonical_sha256"] == sha(encode(obj))
        assert checks["expected_raw_digest_check"] == "MATCH"
        assert checks["native_profile_check"] == "MATCH"
        assert view["evidence_assessment"] == {"validity": "NOT_CHECKED", "source_execution": "NOT_CHECKED"}
        assert view["recorded_assessment"] == obj
    raw = (base / "partial.json").read_bytes()
    obj = json.loads(raw)
    variant = out / "inputs"
    variant.mkdir()
    cases = {
        "compact": (encode(obj), None, 0),
        "invalid": (b'{"', "MALFORMED", 2),
        "duplicate": (b'{"fst_result":"FAIL",' + raw.lstrip()[1:], "MALFORMED", 2),
        "missing-field": (encode({k:v for k,v in obj.items() if k != "fst_gaps"}), "MALFORMED", 2),
        "wrong-type": (encode(obj | {"fst_findings": [1]}), "MALFORMED", 2),
        "outcome": (encode(obj | {"fst_result": "STRONG"}), "UNSUPPORTED", 2),
        "fail-outcome": (encode(obj | {"fst_result": "FAIL"}), "UNSUPPORTED", 2),
        "profile": (encode(obj | {"fst_profile_version": "2.0"}), "UNSUPPORTED", 2),
        "rule": (encode(obj | {"fst_rule_profile_id": "fictional-unknown"}), "UNSUPPORTED", 2),
        "pair": (encode(obj | {"stress_category": "state_continuity_stress"}), "UNSUPPORTED", 2),
        "extension": (encode(obj | {"fst_rule_hash": "a" * 64}), "UNSUPPORTED", 2),
        "suite": (encode({"fst_suite_id": "fictional", "receipts": [obj]}), "UNSUPPORTED", 2),
        "aggregate": (encode({"fst_aggregate_id": "fictional"}), "UNSUPPORTED", 2),
        "decision": (encode({"execution_state": "ALLOW"}), "UNSUPPORTED", 2),
        "surrogate": (b'{"bad":"\\ud800"}', "MALFORMED", 2),
        "depth": (b'{"bad":' + b'[' * 33 + b'null' + b']' * 33 + b'}', "MALFORMED", 2),
        "limit": (b" " * (1048576 + 1), "UNAVAILABLE", 2),
    }
    for name, (blob, status, code) in cases.items():
        (variant / f"{name}.json").write_bytes(blob)
        dest = run(out, name, f"{name}.json", code, intake=variant)
        view = load(dest / "receipt.json")
        if code == 0:
            assert view["local_checks"]["native_canonical_sha256"] == sha(encode(obj))
            assert view["local_checks"]["raw_native_sha256"] != sha(raw)
            assert view["local_checks"]["expected_raw_digest_check"] == "NOT_CHECKED"
        else:
            issue = view["diagnostic"]
            assert issue["status"] == status
            assert not (dest / "envelope.json").exists()
            assert view["recorded_assessment"] is None
        if status != "UNAVAILABLE":
            preserved(dest, blob)
    for case, filename, expectation, status in [
        ("traversal", "../partial.json", None, "UNAVAILABLE"),
        ("missing", "none.json", None, "UNAVAILABLE"),
        ("mismatch", "partial.json", "0"*64, "REJECTED"),
    ]:
        dest = run(out, case, filename, 2, expected=expectation)
        view = load(dest / "receipt.json")
        issue = view["diagnostic"]
        assert issue["status"] == status
        if expectation:
            preserved(dest, raw)
            assert view["local_checks"]["expected_raw_digest_check"] == "MISMATCH"
    first = out / "partial"
    frozen = members(first)
    second = run(out, "repeat", "partial.json", 0, expected=sha(raw), guarded=False)
    assert members(second) == frozen
    run(out, "occupied", "partial.json", 1, dest=first)
    assert members(first) == frozen
    locked = out / "locked"
    locked.with_name(locked.name + ".publish-lock").mkdir()
    run(out, "locked", "partial.json", 1, dest=locked)
    assert not locked.exists()
    run(out, "bad-arg", "partial.json", 2, expected="broken")
    assert not (out / "bad-arg").exists()
    assert (base / "partial.json").read_bytes() == raw


class OfflineReceiptTests(unittest.TestCase):
    def test_fictional_presentations(self):
        with TemporaryDirectory(prefix="fst-") as scratch:
            verify(Path(scratch))


if __name__ == "__main__":
    unittest.main(verbosity=2)
