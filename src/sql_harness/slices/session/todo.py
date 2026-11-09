from __future__ import annotations

from typing import Any


_TODOS: list[dict[str, Any]] = []


def write_todos(todos: list[dict[str, Any]]) -> str:
    global _TODOS
    _TODOS = list(todos)
    return f"Updated {len(_TODOS)} todo(s)."


def list_todos() -> list[dict[str, Any]]:
    return list(_TODOS)
