import pytest

from sql_harness.shared.safety import assert_readonly_sql


def test_allows_select() -> None:
    assert assert_readonly_sql("SELECT 1") == "SELECT 1"


def test_rejects_drop() -> None:
    with pytest.raises(ValueError, match="blocked"):
        assert_readonly_sql("DROP TABLE customers")


def test_rejects_multi_statement() -> None:
    with pytest.raises(ValueError, match="Multiple"):
        assert_readonly_sql("SELECT 1; SELECT 2")
