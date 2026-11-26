"""Read a bounded, fictional DTPE runtime boundary receipt without runtime imports."""

import hashlib
import json
import re


SOURCE_REVISION = "7ee51f421529bf1a33d14800b151d01b3e4be711"
PROFILE = "dtpe.runtime-boundary.pinned.1"
CRYPTO_PROFILE = "ed25519+sha256+canonical_json_v1"
DIGEST = re.compile(r"[0-9a-f]{64}")
OUTCOMES = {"ALLOW": "BOUNDARY_ALLOW", "REFUSED_NON_BINDING": "BOUNDARY_REFUSED_NON_BINDING"}
OBJECT_FIELDS = (
    "authority_result", "canonical_current_state", "canonical_transition", "decision_space",
    "evaluator_trace", "frame_continuity_result", "signal_profile", "stability_result",
    "state_admissibility_result", "system_state", "temporal_invariant_result",
)
TEXT_FIELDS = (
    "constraint_profile", "continuity_mode", "crypto_profile", "current_execution_time",
    "execution_intent", "execution_state", "execution_time", "reason", "receipt_canonical",
    "sequence_id", "temporal_rule_profile",
)
HASH_FIELDS = ("authority_hash", "invariant_frame_hash", "policy_state_hash", "receipt_hash")
REQUIRED = set(OBJECT_FIELDS + TEXT_FIELDS + HASH_FIELDS) | {"continuity_required"}
OPTIONAL = {"authority_canonical", "authority_signature_b64", "prior_invariant_frame_hash",
            "prior_execution_time"}
AUTHORITY_FIELDS = {"identity_id", "owner_id", "intent", "action", "expires_at",
                    "policy_version", "policy_state_hash", "crypto_profile"}


class ReceiptError(ValueError):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def native_text(document):
    return json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                      allow_nan=False)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def digest(value):
    return isinstance(value, str) and DIGEST.fullmatch(value) is not None


def require(condition, message):
    if not condition:
        raise ReceiptError("MALFORMED", message)


def unique_pairs(pairs):
    document = {}
    for key, value in pairs:
        require(key not in document, "Duplicate JSON key.")
        document[key] = value
    return document


def reject_number(_token):
    raise ReceiptError("UNSUPPORTED", "The fixture profile accepts only bounded JSON integers.")


def integer(token):
    if token == "-0" or len(token.lstrip("-")) > 16 or abs(int(token)) > 9007199254740991:
        reject_number(token)
    return int(token)


def check_tree(value, depth=0):
    require(depth <= 24, "JSON nesting exceeds the fixture limit.")
    if isinstance(value, str):
        value.encode("utf-8", "strict")
    elif isinstance(value, dict):
        for key, item in value.items():
            key.encode("utf-8", "strict")
            check_tree(item, depth + 1)
    elif isinstance(value, list):
        for item in value:
            check_tree(item, depth + 1)


def load_object(source):
    try:
        value = json.loads(source, object_pairs_hook=unique_pairs, parse_int=integer,
                           parse_float=reject_number, parse_constant=reject_number)
        require(isinstance(value, dict), "Expected a JSON object.")
        check_tree(value)
        return value
    except (UnicodeError, json.JSONDecodeError, RecursionError) as error:
        raise ReceiptError("MALFORMED", "Invalid JSON, Unicode or nesting.") from error


def parse_receipt(raw):
    try:
        document = load_object(raw.decode("utf-8-sig"))
    except UnicodeError as error:
        raise ReceiptError("MALFORMED", "Invalid UTF-8.") from error
    fields = document.keys()
    if not REQUIRED <= fields or not fields <= REQUIRED | OPTIONAL:
        raise ReceiptError("UNSUPPORTED", "Expected the pinned bare runtime boundary receipt shape.")
    require(all(isinstance(document[key], dict) for key in OBJECT_FIELDS),
            "Invalid native object field.")
    require(all(text(document[key]) for key in TEXT_FIELDS) and
            all(digest(document[key]) for key in HASH_FIELDS) and
            type(document["continuity_required"]) is bool, "Invalid native scalar field.")
    for key in OPTIONAL & fields:
        validator = digest if key == "prior_invariant_frame_hash" else text
        require(validator(document[key]), "Invalid optional native field: " + key)
    if document["crypto_profile"] != CRYPTO_PROFILE:
        raise ReceiptError("UNSUPPORTED", "The declared crypto profile is outside this pilot.")
    boundary_state = document["execution_state"]
    if boundary_state not in OUTCOMES:
        raise ReceiptError("UNSUPPORTED", "Unknown boundary execution state.")
    authority = document["authority_result"]
    require(authority.keys() == {"ok", "execution_state", "reason"} and type(authority["ok"]) is bool
            and text(authority["execution_state"]) and text(authority["reason"]),
            "Invalid authority-stage result.")
    if authority["execution_state"] not in OUTCOMES:
        raise ReceiptError("UNSUPPORTED", "Unknown authority execution state.")

    authority_source = document.get("authority_canonical")
    require(authority_source is not None or "authority_signature_b64" not in document,
            "Authority signature metadata requires an authority preimage.")
    claims = None
    if authority_source is not None:
        claims = load_object(authority_source)
        require(claims.keys() == AUTHORITY_FIELDS and all(text(item) for item in claims.values())
                and digest(claims["policy_state_hash"]), "Invalid authority preimage fields.")
    return document, claims


def observation(state, declared=None, calculated=None):
    return dict(state=state, declared=declared, calculated=calculated)


def comparison(declared, calculated):
    return observation("MATCH" if declared == calculated else "MISMATCH", declared, calculated)


def raw_observation(raw, expected):
    if raw is None:
        return observation("UNAVAILABLE", expected)
    actual = sha256(raw)
    return comparison(expected, actual) if expected is not None else observation("NOT_CHECKED", None, actual)


def assess(raw, expected):
    """Return parsed fixture material, distinct observations and publication diagnostics."""
    checks = {
        "raw_bytes": raw_observation(raw, expected),
        "outer_material": observation("NOT_CHECKED"),
        "receipt_hash": observation("NOT_CHECKED"),
        "authority_hash": observation("NOT_CHECKED"),
        "signature_validity": "NOT_CHECKED",
        "trusted_key_binding": "NOT_CHECKED",
        "authenticity": "NOT_CHECKED",
        "source_execution": "NOT_CHECKED",
        "ledger_continuity": "NOT_CHECKED",
        "replay": "NOT_CHECKED",
        "protected_effects": "NOT_CHECKED",
    }
    diagnostics = []
    if raw is None:
        return None, None, checks, [
            ("native-unavailable", "UNAVAILABLE", "Supplied file could not be read safely."),
        ]
    if checks["raw_bytes"]["state"] == "MISMATCH":
        diagnostics.append(("native-digest-rejected", "REJECTED", "Expected raw SHA-256 differs."))
    try:
        document, claims = parse_receipt(raw)
    except ReceiptError as error:
        diagnostics.append(("native-" + error.status.lower(), error.status, str(error)))
        return None, None, checks, diagnostics
    embedded = document["receipt_canonical"]
    material = {key: value for key, value in document.items()
                if key not in {"receipt_canonical", "receipt_hash"}}
    stored_digest = sha256(embedded.encode("utf-8"))
    reconstructed = native_text(material)
    checks["outer_material"] = observation("MATCH" if embedded == reconstructed else "MISMATCH",
                                          stored_digest, sha256(reconstructed.encode("utf-8")))
    checks["receipt_hash"] = comparison(document["receipt_hash"], stored_digest)
    authority_text = document.get("authority_canonical")
    checks["authority_hash"] = (observation("UNAVAILABLE", document["authority_hash"])
                                if authority_text is None else comparison(
                                    document["authority_hash"], sha256(authority_text.encode("utf-8"))))
    for key in ("outer_material", "receipt_hash", "authority_hash"):
        if checks[key]["state"] == "MISMATCH":
            diagnostics.append((key.replace("_", "-") + "-rejected", "REJECTED",
                                "Saved DTPE receipt failed the " + key.replace("_", " ") + " comparison."))
    if OUTCOMES[document["execution_state"]] != document["reason"]:
        diagnostics.append(("boundary-pair-unsupported", "UNSUPPORTED",
                            "Unregistered boundary state and reason pair."))
    return document, claims, checks, diagnostics


def result_fields(document, claims, checks):
    signature = document.get("authority_signature_b64")
    return {
        "authority_result": document["authority_result"],
        "execution_state": document["execution_state"],
        "reason": document["reason"],
        "authority_hash": document["authority_hash"],
        "policy_state_hash": document["policy_state_hash"],
        "execution_time": document["execution_time"],
        "signature": {
            "state": "ABSENT" if signature is None else "PRESENT_UNVERIFIED",
            "authority_signature_b64": signature,
            "crypto_profile": document["crypto_profile"],
            "subject": "authority_canonical",
            "identity_id": None if claims is None else claims["identity_id"],
        },
        "integrity": checks,
    }
