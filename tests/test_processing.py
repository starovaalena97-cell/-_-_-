"""
Тесты для модуля processing.
"""

from typing import Dict, List

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default() -> None:
    """Тестирует фильтрацию по умолчанию (EXECUTED)."""
    test_data: List[Dict[str, str | int]] = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'},
    ]

    expected: List[Dict[str, str | int]] = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'},
    ]

    result = filter_by_state(test_data)
    assert result == expected


def test_filter_by_state_canceled() -> None:
    """Тестирует фильтрацию по статусу CANCELED."""
    test_data: List[Dict[str, str | int]] = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'},
    ]

    expected: List[Dict[str, str | int]] = [
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'},
    ]

    result = filter_by_state(test_data, 'CANCELED')
    assert result == expected


def test_filter_by_state_empty() -> None:
    """Тестирует фильтрацию на пустом списке."""
    test_data: List[Dict[str, str | int]] = []
    result = filter_by_state(test_data)
    assert result == []


def test_sort_by_date_descending() -> None:
    """Тестирует сортировку по убыванию (сначала новые)."""
    test_data: List[Dict[str, str | int]] = [
        {'id': 1, 'date': '2023-01-01T10:00:00'},
        {'id': 2, 'date': '2023-01-02T08:00:00'},
        {'id': 3, 'date': '2022-12-31T23:59:59'},
    ]

    result = sort_by_date(test_data)
    assert result[0]['date'] == '2023-01-02T08:00:00'
    assert result[1]['date'] == '2023-01-01T10:00:00'
    assert result[2]['date'] == '2022-12-31T23:59:59'


def test_sort_by_date_ascending() -> None:
    """Тестирует сортировку по возрастанию (сначала старые)."""
    test_data: List[Dict[str, str | int]] = [
        {'id': 1, 'date': '2023-01-01T10:00:00'},
        {'id': 2, 'date': '2023-01-02T08:00:00'},
        {'id': 3, 'date': '2022-12-31T23:59:59'},
    ]

    result = sort_by_date(test_data, False)
    assert result[0]['date'] == '2022-12-31T23:59:59'
    assert result[1]['date'] == '2023-01-01T10:00:00'
    assert result[2]['date'] == '2023-01-02T08:00:00'


def test_sort_by_date_empty() -> None:
    """Тестирует сортировку на пустом списке."""
    test_data: List[Dict[str, str | int]] = []
    result = sort_by_date(test_data)
    assert result == []


if __name__ == "__main__":
    test_filter_by_state_default()
    test_filter_by_state_canceled()
    test_filter_by_state_empty()
    test_sort_by_date_descending()
    test_sort_by_date_ascending()
    test_sort_by_date_empty()
    print("Все тесты для processing пройдены успешно!")
