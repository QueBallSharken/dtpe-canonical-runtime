from core.spectre.state_guard import evaluate_state_admissibility
from core.spectre.stability_guard import evaluate_system_stability


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_true(value, label: str) -> None:
    if not value:
        raise RuntimeError(f"{label}: expected truthy value, got {value!r}")


def main() -> int:
    missing_state = evaluate_state_admissibility(
        canonical_current_state=None,
        canonical_transition={},
        canonical_policy_state_hash="abc123",
        execution_intent="demo.intent",
        authority_hash="deadbeef",
        crypto_profile="ed25519+sha256+canonical_json_v1",
    )
    assert_equal(missing_state["ok"], False, "missing_state.ok")
    assert_equal(
        missing_state["reason"],
        "MISSING_CANONICAL_CURRENT_STATE",
        "missing_state.reason",
    )

    invalid_transition = evaluate_state_admissibility(
        canonical_current_state={"state": "ok"},
        canonical_transition="bad",
        canonical_policy_state_hash="abc123",
        execution_intent="demo.intent",
        authority_hash="deadbeef",
        crypto_profile="ed25519+sha256+canonical_json_v1",
    )
    assert_equal(invalid_transition["ok"], False, "invalid_transition.ok")
    assert_equal(
        invalid_transition["reason"],
        "INVALID_CANONICAL_TRANSITION",
        "invalid_transition.reason",
    )

    admissible = evaluate_state_admissibility(
        canonical_current_state={"state": "ok"},
        canonical_transition={"action": "execute", "expires_at": "2030-01-01T00:00:00"},
        canonical_policy_state_hash="abc123",
        execution_intent="demo.intent",
        authority_hash="deadbeef",
        crypto_profile="ed25519+sha256+canonical_json_v1",
    )
    assert_true(admissible["ok"], "admissible.ok")
    assert_equal(admissible["reason"], "STATE_ADMISSIBLE", "admissible.reason")

    missing_action = evaluate_system_stability(
        system_state={"policy": "ok"},
        proposed_transition={"expires_at": "2030-01-01T00:00:00"},
    )
    assert_equal(missing_action["ok"], False, "missing_action.ok")
    assert_equal(
        missing_action["reason"],
        "MISSING_TRANSITION_ACTION",
        "missing_action.reason",
    )

    stable = evaluate_system_stability(
        system_state={"policy": "ok"},
        proposed_transition={"action": "execute", "expires_at": "2030-01-01T00:00:00"},
    )
    assert_true(stable["ok"], "stable.ok")
    assert_equal(stable["reason"], "SYSTEM_STABLE", "stable.reason")

    print("PASS: phase5 guard hardening verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
