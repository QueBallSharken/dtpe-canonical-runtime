"""Run the exact presenter entry point with repository and I/O auditing enabled."""
import importlib.abc
from importlib.machinery import PathFinder
from pathlib import Path
import runpy
import sys



def main():
    root = Path.cwd().resolve()
    scratch, target, *args = sys.argv[1:]
    scratch = Path(scratch).resolve()
    allowed = {
        "core", "core.canonical", "core.hashing", "core.spectre", "core.spectre.fst",
        "core.spectre.fst.offline_input", "core.spectre.fst.offline_profile",
        "core.spectre.fst.present", "core.spectre.fst.receipt_schema",
        "core.spectre.fst.result_vocabulary", "core.spectre.fst.rule_profiles",
        "core.spectre.fst.scenarios", "dtpe_offline_receipts", "dtpe_offline_receipts.present",
        "dtpe_offline_receipts.profile",
    }
    prefixes = {"core", "integrations", "dtpe_offline_receipts", "tools", "tests"}


    class Guard(importlib.abc.MetaPathFinder):
        def find_spec(self, fullname, path=None, target=None):
            if fullname.split(".")[0] in prefixes:
                if fullname not in allowed:
                    raise AssertionError(f"Unexpected repository import: {fullname}")
                spec = PathFinder.find_spec(fullname, path)
                if spec is None:
                    raise AssertionError(f"Missing repository module: {fullname}")
                locations = list(spec.submodule_search_locations or ())
                if spec.origin is not None:
                    locations.append(spec.origin)
                if not locations or any(not Path(p).resolve().is_relative_to(root) for p in locations):
                    raise AssertionError(f"Repository module resolved outside candidate: {fullname}")
                print(f"IMPORT {fullname} ({'namespace' if spec.origin is None else 'local file'})")
                return spec


    def audit(event, args):
        if event.startswith(("socket.", "subprocess.")) or event in {"os.system", "os.startfile"}:
            raise AssertionError(f"Forbidden audit event: {event}")
        if event == "open" and isinstance(args[0], (str, bytes)):
            if isinstance(args[0], bytes):
                return
            path = Path(args[0]).absolute()
            if not any(path.is_relative_to(directory) for directory in (
                root, scratch, Path(sys.base_prefix).resolve(),
            )):
                raise AssertionError(f"Unexpected file access: {path.name}")
            if {"data", ".ssh", "keystore", "ledger", "keys"} & {part.lower() for part in path.parts}:
                raise AssertionError(f"Operational data access: {path.name}")


    sys.meta_path.insert(0, Guard())
    sys.addaudithook(audit)
    sys.path.insert(0, str(root))
    sys.argv[:] = [target, *args]
    runpy.run_module(target, run_name="__main__", alter_sys=True)


if __name__ == "__main__":
    main()
