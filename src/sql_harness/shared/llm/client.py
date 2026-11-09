from __future__ import annotations

from typing import Any

from sql_harness.shared.config import get_settings


class LlmClient:
    """HTTP client for OpenAI-compatible chat completions. Implementation TBD."""

    def __init__(self) -> None:
        self.settings = get_settings()

    def chat(self, messages: list[dict[str, Any]], tools: list[dict[str, Any]] | None = None) -> dict[str, Any]:
        raise NotImplementedError("LLM client not implemented yet")
