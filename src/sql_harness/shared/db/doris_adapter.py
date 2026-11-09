from __future__ import annotations

from typing import Any


class DorisAdapter:
    """Doris (MySQL protocol) adapter stub — wire up in db-layer milestone."""

    def __init__(
        self,
        *,
        host: str,
        port: int,
        user: str,
        password: str,
        database: str,
    ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def list_databases(self) -> list[str]:
        raise NotImplementedError

    def list_tables(self, database: str | None = None) -> list[str]:
        raise NotImplementedError

    def describe_table(self, table: str, database: str | None = None) -> list[dict[str, Any]]:
        raise NotImplementedError

    def sample_rows(
        self, table: str, database: str | None = None, limit: int = 5
    ) -> dict[str, Any]:
        raise NotImplementedError

    def execute(self, sql: str, *, max_rows: int, timeout_sec: int) -> dict[str, Any]:
        raise NotImplementedError

    def explain(self, sql: str) -> dict[str, Any]:
        raise NotImplementedError

    def close(self) -> None:
        return None
