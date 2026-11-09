from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

# src/sql_harness/shared/config/settings.py → repo root
_REPO_ROOT = Path(__file__).resolve().parents[4]


def _load_env() -> None:
    # Prefer process CWD .env; fall back to repo root next to pyproject.toml
    for candidate in (Path.cwd() / ".env", _REPO_ROOT / ".env"):
        if candidate.exists():
            load_dotenv(candidate)
            return


@dataclass(frozen=True)
class Settings:
    llm_api_key: str
    llm_base_url: str
    llm_model: str
    max_turns_per_request: int
    db_type: str
    db_path: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_database: str
    sql_max_rows: int
    sql_timeout_sec: int
    sql_max_result_chars: int


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    _load_env()
    return Settings(
        llm_api_key=os.getenv("LLM_API_KEY", ""),
        llm_base_url=os.getenv("LLM_BASE_URL", "https://api.deepseek.com/v1"),
        llm_model=os.getenv("LLM_MODEL", "deepseek-chat"),
        max_turns_per_request=int(os.getenv("MAX_TURNS_PER_REQUEST", "8")),
        db_type=os.getenv("DB_TYPE", "sqlite").lower(),
        db_path=os.getenv("DB_PATH", "./data/demo.db"),
        db_host=os.getenv("DB_HOST", "127.0.0.1"),
        db_port=int(os.getenv("DB_PORT", "9030")),
        db_user=os.getenv("DB_USER", ""),
        db_password=os.getenv("DB_PASSWORD", ""),
        db_database=os.getenv("DB_DATABASE", ""),
        sql_max_rows=int(os.getenv("SQL_MAX_ROWS", "200")),
        sql_timeout_sec=int(os.getenv("SQL_TIMEOUT_SEC", "30")),
        sql_max_result_chars=int(os.getenv("SQL_MAX_RESULT_CHARS", "12000")),
    )
