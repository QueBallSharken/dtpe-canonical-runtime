"""Bounded JSON and local file intake for saved FST presentations."""
import hashlib
import json
import re

MAX_DEPTH = 32
MAX_INT = 9007199254740991
DIGEST = re.compile(r"[a-f0-9]{64}")

class FormatError(ValueError):
    """Input fails the selected format."""


class Unsupported(FormatError):
    """Input needs a different profile."""


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(condition, message):
    if not condition:
        raise FormatError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key.")
        result[key] = value
    return result


def integer(token):
    require(token != "-0" and len(token.lstrip("-")) <= 16, "Integer outside profile.")
    value = int(token)
    require(abs(value) <= MAX_INT, "Integer outside profile.")
    return value


def reject_number(_token):
    raise FormatError("Only profile integers are supported.")


def decode(raw):
    try:
        value = json.loads(
            raw.decode("utf-8", "strict"), object_pairs_hook=unique_object,
            parse_int=integer, parse_float=reject_number, parse_constant=reject_number,
        )
        require(isinstance(value, dict), "Expected exactly one JSON object.")
        pending = [(value, 0)]
        while pending:
            item, depth = pending.pop()
            if isinstance(item, str):
                item.encode("utf-8", "strict")
            elif isinstance(item, (dict, list)):
                require(depth < MAX_DEPTH, "JSON nesting exceeds the pilot bound.")
                children = (*item.keys(), *item.values()) if isinstance(item, dict) else item
                pending.extend((child, depth + 1) for child in children)
    except (UnicodeError, RecursionError, json.JSONDecodeError) as error:
        raise FormatError("Invalid JSON, Unicode or nesting.") from error
    return value
