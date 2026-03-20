from core.spectre.temporal_guard import evaluate_temporal_invariant


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise RuntimeError(f"{label}: expected {expected!r}, got {actual!r}")


def main() -> int:
    # VALID case
    result = evaluate_temporal_invariant(
        canonical_transition={"expires_at": "2030-01-01T00:00:00"},
        execution_time="2029-01-01T00:00:00",
    )
    assert_equal(result["ok"], True, "valid.ok")
    assert_equal(result["reason"], "VALID", "valid.reason")

    # EXPIRED case
    result = evaluate_temporal_invariant(
        canonical_transition={"expires_at": "2020-01-01T00:00:00"},
        execution_time="2025-01-01T00:00:00",
    )
    assert_equal(result["ok"], False, "expired.ok")
    assert_equal(result["reason"], "EXPIRED", "expired.reason")

    # MISSING_EXECUTION_TIME
    result = evaluate_temporal_invariant(
        canonical_transition={"expires_at": "2030-01-01T00:00:00"},
        execution_time="",
    )
    assert_equal(result["ok"], False, "missing_exec.ok")
    assert_equal(result["reason"], "MISSING_EXECUTION_TIME", "missing_exec.reason")

    # MISSING_EXPIRES_AT
    result = evaluate_temporal_invariant(
        canonical_transition={},
        execution_time="2025-01-01T00:00:00",
    )
    assert_equal(result["ok"], False, "missing_exp.ok")
    assert_equal(result["reason"], "MISSING_EXPIRES_AT", "missing_exp.reason")

    print("PASS: phase6 temporal guard verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
