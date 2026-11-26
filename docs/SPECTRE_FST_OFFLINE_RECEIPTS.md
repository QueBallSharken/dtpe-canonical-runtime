# Present a fictional saved SPECTRE-FST receipt

From the DTPE Canonical Runtime root with Python 3.10 or later:

```powershell
python -B -m core.spectre.fst.present --intake tests/fixtures/fst_receipt_v1 --native partial.json --origin fixture --output new-fst-view
```

Use a portable relative input path and a fresh output directory under an existing local parent. This pilot accepts one bare fictional paper-token receipt with the nine fields emitted by the pinned minimal profile at `b0cceb4702768f2057df1d92d25de7f61a8297bb`. The pinned rule profile permits `PARTIAL`, `UNVERIFIABLE`, and `CONTRADICTION_EXPOSED`. Supported input is bounded to 1 MiB, strict UTF-8 JSON and depth 32.

The view contains the recorded fields, local checks and unassessed evidence-validity status. `native.json` preserves safely readable input bytes even on a diagnostic. The raw SHA-256 covers the file, and the native canonical SHA-256 covers DTPE canonical receipt bytes. Supply `--expected-native-sha256` with an independently obtained expected raw digest to compare file bytes. Fixture origin is a caller declaration.

Exit 0 indicates completed presentation. Exit 2 indicates diagnostics or argument errors. Exit 1 indicates publication failure. The presenter requires only the DTPE checkout and local files.
