from __future__ import annotations

from typing import Any


def compact_messages(messages: list[dict[str, Any]], *, max_chars: int) -> list[dict[str, Any]]:
    """Trim oversized tool results / old turns — TBD."""
    return messages
