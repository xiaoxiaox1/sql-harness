from __future__ import annotations

from typing import Any, Callable

from sql_harness.slices.query import tools as query_tools
from sql_harness.slices.schema import tools as schema_tools
from sql_harness.slices.session.todo import write_todos

ToolHandler = Callable[[dict[str, Any]], str]

TODO_SCHEMA: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "todo_write",
        "description": "Replace the current todo list for multi-step analysis.",
        "parameters": {
            "type": "object",
            "properties": {
                "todos": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "content": {"type": "string"},
                            "status": {"type": "string"},
                        },
                        "required": ["id", "content", "status"],
                    },
                }
            },
            "required": ["todos"],
            "additionalProperties": False,
        },
    },
}


def all_tool_schemas() -> list[dict[str, Any]]:
    return [
        *schema_tools.TOOL_SCHEMAS,
        *query_tools.TOOL_SCHEMAS,
        TODO_SCHEMA,
    ]


def all_tool_handlers() -> dict[str, ToolHandler]:
    handlers: dict[str, ToolHandler] = {}
    handlers.update(schema_tools.TOOL_HANDLERS)
    handlers.update(query_tools.TOOL_HANDLERS)
    handlers["todo_write"] = lambda args: write_todos(list(args.get("todos") or []))
    return handlers
