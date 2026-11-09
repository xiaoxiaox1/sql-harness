from __future__ import annotations

from typing import Any, Callable

ToolHandler = Callable[[dict[str, Any]], str]

TOOL_SCHEMAS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "list_databases",
            "description": "List available databases / catalogs.",
            "parameters": {"type": "object", "properties": {}, "additionalProperties": False},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_tables",
            "description": "List tables in a database.",
            "parameters": {
                "type": "object",
                "properties": {"database": {"type": "string"}},
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "describe_table",
            "description": "Describe columns of a table.",
            "parameters": {
                "type": "object",
                "properties": {
                    "table": {"type": "string"},
                    "database": {"type": "string"},
                },
                "required": ["table"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "sample_rows",
            "description": "Sample a few rows from a table.",
            "parameters": {
                "type": "object",
                "properties": {
                    "table": {"type": "string"},
                    "database": {"type": "string"},
                    "limit": {"type": "integer"},
                },
                "required": ["table"],
                "additionalProperties": False,
            },
        },
    },
]


def _stub(name: str) -> ToolHandler:
    def _run(args: dict[str, Any]) -> str:
        return f"[stub] {name} called with {args}"

    return _run


TOOL_HANDLERS: dict[str, ToolHandler] = {
    "list_databases": _stub("list_databases"),
    "list_tables": _stub("list_tables"),
    "describe_table": _stub("describe_table"),
    "sample_rows": _stub("sample_rows"),
}
