from __future__ import annotations

from sql_harness.shared.config import get_settings
from sql_harness.shared.db.base import DbAdapter
from sql_harness.shared.db.doris_adapter import DorisAdapter
from sql_harness.shared.db.sqlite_adapter import SqliteAdapter


def create_adapter() -> DbAdapter:
    settings = get_settings()
    if settings.db_type == "sqlite":
        return SqliteAdapter(settings.db_path)
    if settings.db_type == "doris":
        return DorisAdapter(
            host=settings.db_host,
            port=settings.db_port,
            user=settings.db_user,
            password=settings.db_password,
            database=settings.db_database,
        )
    raise ValueError(f"Unsupported DB_TYPE: {settings.db_type!r} (use sqlite|doris)")
