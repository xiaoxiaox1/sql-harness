# SQL Harness — Agent Startup Notes

## Profile

- **Name**: sql-harness
- **Version**: 0.1.0
- **Stack**: Python 3.12 + uv
- **Architecture**: vertical slices (feature packages) + shared kernel

## Quick start

```bash
uv sync
cp .env.example .env   # fill LLM_API_KEY (and DB_* if needed)
uv run sql-harness
# or
uv run python -m sql_harness
```

## Vertical slices

| Slice | Path | Responsibility |
|-------|------|----------------|
| `chat` | `src/sql_harness/slices/chat/` | REPL entry, slash commands |
| `agent_runtime` | `src/sql_harness/slices/agent_runtime/` | ReAct loop, prompts, compaction |
| `schema` | `src/sql_harness/slices/schema/` | list/describe/sample tools |
| `query` | `src/sql_harness/slices/query/` | execute/explain tools |
| `session` | `src/sql_harness/slices/session/` | todos, schema snapshot |

Shared kernel under `src/sql_harness/shared/` (`config`, `db`, `llm`, `safety`, `logging`).

## Planned tools

1. `list_databases`
2. `list_tables`
3. `describe_table`
4. `sample_rows`
5. `execute_sql` (read-only + limits)
6. `explain_sql`
7. `todo_write`

## Slash commands (planned)

- `/help` `/clear` `/db` `/tables` `/schema` `/sql <query>` `/quit`

## Environment

See `.env.example`. Default DB is local SQLite demo under `data/demo.db`.
