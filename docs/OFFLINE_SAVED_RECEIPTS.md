# Present a saved fictional DTPE receipt

From the DTPE Canonical Runtime repository root with Python 3.10 or later:

```powershell
python -B -m dtpe_offline_receipts.present --intake tests/fixtures/dtpe_receipt_v1 --native refused.json --origin fixture --output new-receipt
python -B -m tests.test_saved_dtpe_receipt
```

Use a portable relative input path under a local, operator-controlled intake
directory and a fresh output directory under an existing local parent. Input
is bounded to 1 MiB with limits on JSON nesting and integers. The only
supported profile is the fictional bare runtime boundary receipt shape pinned
to DTPE revision `7ee51f421529bf1a33d14800b151d01b3e4be711`. Fixture origin is
a caller declaration. Ledger, IAL, FST and other receipt shapes are outside
this profile.

The output contains `receipt.json`, `receipt.txt` and `native.json` when
offer bytes were readable. The result shows the boundary outcome and reason
alongside the separate authority-stage claim. A reported authority allow can
coexist with a boundary refusal. The fictional allow fixture carries dummy
authority signature bytes for display.

The presenter checks the outer material against the native canonical text,
the declared receipt hash against that text, and the declared authority hash
against the authority preimage where supplied. The saved-byte SHA-256 always
covers the original bytes. Supply an independently recorded
`--expected-native-sha256` value to compare this raw digest. A declared
authority signature describes the authority preimage. Signature validity, key
binding, authenticity, source execution, replay, continuity and effects
remain unchecked. Other nested evidence is retained as recorded native data.

Exit 0 means presentation completed, including for a native refusal. Exit 2
means diagnostic-only output or argument error. Exit 1 means publication
failed. The presenter is independent of SENTRIX and the operational runtime.
