from __future__ import annotations

from sql_harness.shared.config import get_settings


def handle_slash(line: str) -> str | None:
    parts = line.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd in {"/quit", "/exit", "/q"}:
        return "quit"
    if cmd == "/help":
        return (
            "Commands:\n"
            "  /help              Show this help\n"
            "  /db                Show current DB settings\n"
            "  /clear             Clear conversation (stub)\n"
            "  /schema            Refresh schema snapshot (stub)\n"
            "  /tables [db]       List tables (stub)\n"
            "  /sql <query>       Run read-only SQL (stub)\n"
            "  /quit              Exit"
        )
    if cmd == "/db":
        s = get_settings()
        if s.db_type == "sqlite":
            return f"type=sqlite path={s.db_path}"
        return (
            f"type={s.db_type} host={s.db_host}:{s.db_port} "
            f"database={s.db_database} user={s.db_user}"
        )
    if cmd == "/clear":
        return "Conversation cleared (stub — no history yet)."
    if cmd in {"/schema", "/tables", "/sql"}:
        return f"{cmd} is stubbed; implement in schema/query slices. arg={arg!r}"
    return f"Unknown command: {cmd}. Try /help."
