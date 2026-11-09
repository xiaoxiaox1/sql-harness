from sql_harness.slices.session.registry import all_tool_handlers, all_tool_schemas


def test_tool_registry_names() -> None:
    schemas = all_tool_schemas()
    names = {s["function"]["name"] for s in schemas}
    assert names == {
        "list_databases",
        "list_tables",
        "describe_table",
        "sample_rows",
        "execute_sql",
        "explain_sql",
        "todo_write",
    }
    handlers = all_tool_handlers()
    assert set(handlers) == names
