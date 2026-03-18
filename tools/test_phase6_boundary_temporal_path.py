from core.spectre.boundary import evaluate_execution_boundary


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_true(value, label: str) -> None:
    if not value:
        raise RuntimeError(f"{label}: expected truthy value, got {value!r}")


def main() -> int:
    boundary_result = evaluate_execution_boundary(
        authority_result={"ok": True, "execution_state": "ALLOW", "reason": "admissible"},
        canonical_current_state={"state": "ok"},
        system_state={"policy": "ok"},
        canonical_transition={"action": "execute", "expires_at": "2030-01-01T00:00:00"},
        canonical_policy_state_hash="abc123",
        execution_intent="demo.intent",
        authority_hash="deadbeef",
        crypto_profile="ed25519+sha256+canonical_json_v1",
    )

    assert_true(boundary_result["ok"], "boundary_result.ok")
    assert_equal(boundary_result["execution_state"], "ALLOW", "boundary_result.execution_state")
    assert_equal(boundary_result["reason"], "BOUNDARY_ALLOW", "boundary_result.reason")

    temporal_result = boundary_result.get("temporal_invariant_result")
    if not isinstance(temporal_result, dict):
        raise RuntimeError("boundary_result missing temporal_invariant_result")

    assert_true(temporal_result["ok"], "temporal_result.ok")
    assert_equal(
        temporal_result["reason"],
        "TEMPORAL_INVARIANTS_SATISFIED",
        "temporal_result.reason",
    )

    print("PASS: phase6 boundary temporal path verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
