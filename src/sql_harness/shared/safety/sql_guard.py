from __future__ import annotations

_FORBIDDEN_PREFIXES = (
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "truncate",
    "create",
    "replace",
    "grant",
    "revoke",
    "call",
    "load",
)


def assert_readonly_sql(sql: str) -> str:
    """Reject obviously dangerous / multi-statement SQL. Full rules TBD."""
    cleaned = sql.strip().rstrip(";").strip()
    if not cleaned:
        raise ValueError("SQL is empty")
    if ";" in cleaned:
        raise ValueError("Multiple statements are not allowed")
    head = cleaned.split(None, 1)[0].lower()
    if head in _FORBIDDEN_PREFIXES:
        raise ValueError(f"Statement type {head!r} is blocked (read-only mode)")
    return cleaned
