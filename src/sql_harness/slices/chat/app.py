from __future__ import annotations

from sql_harness import __version__
from sql_harness.shared.config import get_settings
from sql_harness.shared.logging import log
from sql_harness.slices.chat.commands import handle_slash


def main() -> int:
    settings = get_settings()
    print(f"sql-harness v{__version__}  (scaffold)")
    print(f"DB_TYPE={settings.db_type}  model={settings.llm_model}")
    print("Type /help for commands, /quit to exit. Agent loop not wired yet.\n")

    while True:
        try:
            line = input("sql> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not line:
            continue
        if line.startswith("/"):
            result = handle_slash(line)
            if result == "quit":
                return 0
            if result:
                print(result)
            continue
        log(
            "Agent loop not implemented yet. Use /help. "
            "Natural-language questions will be handled in a later milestone.",
            level="warn",
        )


if __name__ == "__main__":
    raise SystemExit(main())
