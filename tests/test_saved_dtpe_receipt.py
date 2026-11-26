"""Tests for the saved fictional DTPE receipt profile and standalone CLI."""

import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

from dtpe_offline_receipts.present import main

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "dtpe_receipt_v1"


def audit(event, _args):
    if event.startswith(("socket.", "subprocess.", "os.exec", "os.spawn")) or event in {
        "os.system", "os.startfile",
    }:
        raise AssertionError(f"Offline isolation violated: {event}")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")


def rebuild(document):
    material = {key: val for key, val in document.items()
                if key not in {"receipt_canonical", "receipt_hash"}}
    raw = encode(material)
    return encode(dict(material, receipt_canonical=raw.decode("utf-8"), receipt_hash=sha(raw)))


class SavedReceiptTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.allow = (FIXTURES / "allow.json").read_bytes()
        self.refused = (FIXTURES / "refused.json").read_bytes()
        self.counter = 0

    def present(self, raw, code=0, *, expected=None, source="receipt.json", destination=None):
        (self.root / "receipt.json").write_bytes(raw)
        self.counter += 1
        output = destination or self.root / f"p{self.counter}"
        args = ["--intake", str(self.root), "--native", source, "--origin", "fixture",
                "--output", str(output)]
        if expected is not None:
            args += ["--expected-native-sha256", expected]
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(args), code)
        return output

    def view(self, output, raw):
        capture = output / "native.json"
        if raw is not None:
            self.assertEqual(capture.read_bytes(), raw)
        elif capture is not None:
            self.assertFalse(capture.exists())
        return json.loads((output / "receipt.json").read_bytes())

    def result(self, output, raw):
        view = self.view(output, raw)
        return view["result"]

    def assert_diagnostic(self, raw, key, *, expected=None):
        output = self.present(raw, 2, expected=expected)
        view = self.view(output, raw)
        self.assertIn(key, {item["code"] for item in view["diagnostics"]})
        self.assertEqual(view["state"], "DIAGNOSTIC_ONLY")
        return view

    def test_native_decisions_and_signature_metadata(self):
        for raw, state, reason, signature in (
            (self.allow, "ALLOW", "BOUNDARY_ALLOW", "PRESENT_UNVERIFIED"),
            (self.refused, "REFUSED_NON_BINDING", "BOUNDARY_REFUSED_NON_BINDING", "ABSENT"),
        ):
            output = self.present(raw, expected=sha(raw))
            result = self.result(output, raw)
            self.assertEqual((result["execution_state"], result["reason"]), (state, reason))
            self.assertEqual(result["authority_result"],
                             {"execution_state": "ALLOW", "ok": True, "reason": "admissible"})
            self.assertEqual(result["signature"]["state"], signature)
            self.assertEqual(result["signature"]["subject"], "authority_canonical")
            self.assertEqual(result["signature"]["authority_signature_b64"],
                             json.loads(raw).get("authority_signature_b64"))
            for key in ("raw_bytes", "outer_material", "receipt_hash", "authority_hash"):
                self.assertEqual(result["integrity"][key]["state"], "MATCH")
            for key in ("signature_validity", "trusted_key_binding", "authenticity",
                        "source_execution", "ledger_continuity", "replay", "protected_effects"):
                self.assertEqual(result["integrity"][key], "NOT_CHECKED")
            text = (output / "receipt.txt").read_bytes()
            self.assertIn(reason.encode(), text)
            self.assertIn(signature.encode(), text)

    def test_rejects_outer_tamper_with_matching_embedded_hash(self):
        native = json.loads(self.allow)
        native["execution_state"], native["reason"] = "REFUSED_NON_BINDING", "BOUNDARY_REFUSED_NON_BINDING"
        changed = encode(native)
        self.assertEqual(native["receipt_hash"], sha(native["receipt_canonical"].encode("utf-8")))
        view = self.assert_diagnostic(changed, "outer-material-rejected")
        self.assertEqual(view["integrity"]["outer_material"]["state"], "MISMATCH")
        self.assertEqual(view["integrity"]["receipt_hash"]["state"], "MATCH")
        self.assertIsNone(view["result"])

    def test_distinct_hash_domains_and_missing_authority_preimage(self):
        native = json.loads(self.allow)
        wrong_hash = encode(dict(native, receipt_hash="0" * 64))
        self.assert_diagnostic(wrong_hash, "receipt-hash-rejected")
        wrong_authority = rebuild(dict(native, authority_hash="0" * 64))
        self.assert_diagnostic(wrong_authority, "authority-hash-rejected")
        self.assert_diagnostic(self.allow, "native-digest-rejected", expected="0" * 64)
        reformatted = b"\xef\xbb\xbf" + json.dumps(native, indent=2).encode()
        result = self.result(self.present(reformatted), reformatted)
        self.assertEqual(result["integrity"]["raw_bytes"]["state"], "NOT_CHECKED")
        self.assertNotEqual(sha(reformatted), sha(self.allow))
        self.assertEqual(result["integrity"]["receipt_hash"]["state"], "MATCH")
        native.pop("authority_canonical")
        self.assert_diagnostic(rebuild(native), "native-malformed")
        native.pop("authority_signature_b64")
        raw = rebuild(native)
        result = self.result(self.present(raw), raw)
        self.assertEqual(result["integrity"]["authority_hash"]["state"], "UNAVAILABLE")

    def test_off_profile_inputs_and_inert_output(self):
        native = json.loads(self.allow)
        for raw, key in (
            (b"{", "native-malformed"),
            (b'{"reason":"one","reason":"two"}', "native-malformed"),
            (b'{"key":"\\ud800"}', "native-malformed"),
            (encode({"payload": native, "record_hash": "0" * 64}), "native-unsupported"),
            (encode({"fst_result": "stress-only"}), "native-unsupported"),
            (rebuild(dict(native, crypto_profile="future-profile")), "native-unsupported"),
            (rebuild(dict(native, execution_state="FUTURE")), "native-unsupported"),
            (rebuild(dict(native, reason="BOUNDARY_UNKNOWN")), "boundary-pair-unsupported"),
        ):
            with self.subTest(code=key):
                self.assert_diagnostic(raw, key)
        native["authority_result"]["reason"] = "Fictional\ncontrol\x1b <tag>"
        raw = rebuild(native)
        output = self.present(raw)
        self.assertEqual(self.result(output, raw)["authority_result"]["reason"],
                         native["authority_result"]["reason"])
        self.assertNotIn(b"\x1b", (output / "receipt.txt").read_bytes())

    def test_intake_publication_and_determinism(self):
        for relative in ("../receipt.json", "missing.json"):
            output = self.present(self.allow, 2, source=relative)
            self.assertEqual(self.view(output, None)["diagnostics"][0]["code"], "native-unavailable")
        output = self.present(b" " * (1024 * 1024 + 1), 2)
        self.assertEqual(self.view(output, None)["diagnostics"][0]["code"], "native-unavailable")
        first, second = self.present(self.allow), self.present(self.allow)
        def inventory(directory):
            return {item.relative_to(directory): item.read_bytes()
                    for item in directory.rglob("*") if item.is_file()}
        saved = inventory(first)
        self.assertEqual(saved, inventory(second))
        self.present(self.refused, 1, destination=first)
        self.assertEqual(saved, inventory(first))
        blocked = self.root / "blocked"
        blocked.with_suffix(".publish-lock").mkdir()
        self.present(self.allow, 1, destination=blocked)
        self.assertFalse(blocked.exists())
        self.assertFalse(any(self.root.glob(".dt-*")))

    def test_no_operational_or_peer_imports(self):
        self.present(self.allow)
        self.assertFalse(any(name.split(".")[0] in {"core", "tools", "integrations"} for name in sys.modules))



if __name__ == "__main__":
    sys.addaudithook(audit)
    unittest.main(verbosity=2)
