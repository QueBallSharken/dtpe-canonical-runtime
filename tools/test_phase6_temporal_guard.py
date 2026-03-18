from core.spectre.temporal_guard import evaluate_temporal_invariants


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def assert_true(value, label: str) -> None:
    if not value:
        raise RuntimeError(f"{label}: expected truthy value, got {value!r}")


def main() -> int:
    missing_transition = evaluate_temporal_invariants(
        canonical_transition=None,
    )
    assert_equal(missing_transition["ok"], False, "missing_transition.ok")
    assert_equal(
        missing_transition["reason"],
        "MISSING_CANONICAL_TRANSITION",
        "missing_transition.reason",
    )

    invalid_transition = evaluate_temporal_invariants(
        canonical_transition="bad",
    )
    assert_equal(invalid_transition["ok"], False, "invalid_transition.ok")
    assert_equal(
        invalid_transition["reason"],
        "INVALID_CANONICAL_TRANSITION",
        "invalid_transition.reason",
    )

    empty_transition = evaluate_temporal_invariants(
        canonical_transition={},
    )
    assert_equal(empty_transition["ok"], False, "empty_transition.ok")
    assert_equal(
        empty_transition["reason"],
        "EMPTY_CANONICAL_TRANSITION",
        "empty_transition.reason",
    )

    missing_expiry = evaluate_temporal_invariants(
        canonical_transition={"action": "execute"},
    )
    assert_equal(missing_expiry["ok"], False, "missing_expiry.ok")
    assert_equal(
        missing_expiry["reason"],
        "MISSING_TRANSITION_EXPIRY",
        "missing_expiry.reason",
    )

    temporal_ok = evaluate_temporal_invariants(
        canonical_transition={"action": "execute", "expires_at": "2030-01-01T00:00:00"},
    )
    assert_true(temporal_ok["ok"], "temporal_ok.ok")
    assert_equal(
        temporal_ok["reason"],
        "TEMPORAL_INVARIANTS_SATISFIED",
        "temporal_ok.reason",
    )

    print("PASS: phase6 temporal guard scaffold verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
