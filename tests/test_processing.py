"""
Тесты для модуля processing с использованием фикстур и параметризации.
"""

import pytest
from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    """Тесты для функции filter_by_state."""

    @pytest.mark.parametrize(
        "state, expected_count",
        [("EXECUTED", 3), ("CANCELED", 2)]
    )
    def test_filter_by_state(
            self,
            operations_list: list,
            state: str,
            expected_count: int
    ) -> None:
        """Тестирует фильтрацию по статусу."""
        result = filter_by_state(operations_list, state)
        assert len(result) == expected_count
        assert all(op["state"] == state for op in result)

    def test_filter_by_state_default(self, operations_list: list) -> None:
        """Тестирует фильтрацию со статусом по умолчанию."""
        result = filter_by_state(operations_list)
        assert len(result) == 3
        assert all(op["state"] == "EXECUTED" for op in result)

    def test_filter_by_state_empty_list(self) -> None:
        """Тестирует фильтрацию на пустом списке."""
        result = filter_by_state([])
        assert result == []

    def test_filter_by_state_no_match(self, operations_list: list) -> None:
        """Тестирует фильтрацию, когда нет совпадений."""
        result = filter_by_state(operations_list, "PENDING")
        assert result == []


class TestSortByDate:
    """Тесты для функции sort_by_date."""

    def test_sort_by_date_descending(self, operations_list: list) -> None:
        """Тестирует сортировку по убыванию (сначала новые)."""
        result = sort_by_date(operations_list)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_by_date_ascending(self, operations_list: list) -> None:
        """Тестирует сортировку по возрастанию (сначала старые)."""
        result = sort_by_date(operations_list, descending=False)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates)

    def test_sort_by_date_same_dates(self, operations_with_same_date: list) -> None:
        """Тестирует сортировку при одинаковых датах."""
        result = sort_by_date(operations_with_same_date)
        assert len(result) == 3
        for op in result:
            assert op["date"].startswith("2024-03-01")
        dates = [op["date"] for op in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_by_date_empty_list(self) -> None:
        """Тестирует сортировку на пустом списке."""
        result = sort_by_date([])
        assert result == []
