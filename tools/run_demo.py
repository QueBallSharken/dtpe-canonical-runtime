from core.phase4.pipeline import execute_request
from tools.verify_ledger import verify_ledger
from core.paths import DATA_DIR

print("Running DTPE runtime demonstration")

result = execute_request(
    policy_filename="default.json",
    identity_id="alice",
    owner_id="alice",
    intent="demo.intent",
    action="execute",
    expires_at="2030-01-01T00:00:00",
)

print("\nExecution result:")
print(result)

print("\nVerifying ledger evidence...\n")

verify_ledger(DATA_DIR / "ledger.log")

print("\nDemo complete.")
