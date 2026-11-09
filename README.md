# sql-harness

Interactive **SQL Agent** harness: natural language → explore schema → write SQL → execute (read-only) → explain results.

Architecture mirrors the runtime ideas in [ts_agent](https://github.com/xiaoxiaox1/ts_agent) (ReAct loop, tool registry, intent gates, compaction), implemented in **Python** with **uv**, organized by **vertical slices**.

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)

## Setup

```bash
uv sync
cp .env.example .env
# edit .env — at least LLM_API_KEY for the agent loop
uv run sql-harness
```

## Layout

```
src/sql_harness/
  shared/          # config, db adapters, llm client, sql guard, logging
  slices/
    chat/          # CLI / REPL (entry)
    agent_runtime/ # ReAct loop + prompts
    schema/        # schema exploration tools
    query/         # SQL execute / explain tools
    session/       # todos + schema snapshot
  fixtures/        # demo SQL for SQLite
tests/
```

## Status

Scaffold only — slice modules are stubs ready for implementation.
