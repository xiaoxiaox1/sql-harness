from __future__ import annotations

from typing import Any, Callable

from sql_harness.shared.safety import assert_readonly_sql

ToolHandler = Callable[[dict[str, Any]], str]

TOOL_SCHEMAS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "execute_sql",
            "description": "Execute a read-only SQL query with row/time limits.",
            "parameters": {
                "type": "object",
                "properties": {"sql": {"type": "string"}},
                "required": ["sql"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "explain_sql",
            "description": "Explain a SQL query plan.",
            "parameters": {
                "type": "object",
                "properties": {"sql": {"type": "string"}},
                "required": ["sql"],
                "additionalProperties": False,
            },
        },
    },
]


def run_execute_sql(args: dict[str, Any]) -> str:
    sql = assert_readonly_sql(str(args.get("sql", "")))
    return f"[stub] execute_sql accepted: {sql}"


def run_explain_sql(args: dict[str, Any]) -> str:
    sql = assert_readonly_sql(str(args.get("sql", "")))
    return f"[stub] explain_sql accepted: {sql}"


TOOL_HANDLERS: dict[str, ToolHandler] = {
    "execute_sql": run_execute_sql,
    "explain_sql": run_explain_sql,
}
