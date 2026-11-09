from __future__ import annotations


def log(message: str, *, level: str = "info") -> None:
    """Minimal console logger; TUI-safe logging can replace this later."""
    prefix = {
        "info": "[info]",
        "warn": "[warn]",
        "error": "[error]",
        "debug": "[debug]",
    }.get(level, "[info]")
    print(f"{prefix} {message}")
