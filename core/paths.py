from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
IDENTITIES_DIR = DATA_DIR / "identities"
KEYS_DIR = DATA_DIR / "keys"
POLICY_DIR = DATA_DIR / "policy"