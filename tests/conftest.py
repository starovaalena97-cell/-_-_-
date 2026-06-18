"""
Фикстуры для тестов проекта.
"""

import pytest
from typing import Dict, List, Any


@pytest.fixture
def card_numbers() -> List[str]:
    """Фикстура с номерами карт для тестирования."""
    return [
        "7000792289606361",
        "1234567890123456",
        "0000000000000000",
        "9999999999999999",
    ]


@pytest.fixture
def invalid_card_numbers() -> List[str]:
    """Фикстура с некорректными номерами карт."""
    return [
        "1234",  # слишком короткий
        "700079228960636a",  # с буквами
        "",  # пустая строка
        "12345678901234567",  # слишком длинный
    ]


@pytest.fixture
def account_numbers() -> List[str]:
    """Фикстура с номерами счетов для тестирования."""
    return [
        "73654108430135874305",
        "1234567890",
        "1234",
    ]


@pytest.fixture
def invalid_account_numbers() -> List[str]:
    """Фикстура с некорректными номерами счетов."""
    return [
        "123",  # слишком короткий
        "",  # пустая строка
    ]


@pytest.fixture
def operations_list() -> List[Dict[str, Any]]:
    """Фикстура со списком операций для тестирования."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-03-02T11:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-03T12:00:00"},
        {"id": 4, "state": "CANCELED", "date": "2024-03-04T13:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2024-03-05T14:00:00"},
    ]


@pytest.fixture
def operations_with_same_date() -> List[Dict[str, Any]]:
    """Фикстура с операциями, у которых одинаковые даты."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-03-01T11:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-01T12:00:00"},
    ]


@pytest.fixture
def card_account_strings() -> List[str]:
    """Фикстура со строками для функции mask_account_card."""
    return [
        "Visa Platinum 7000792289606361",
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758",
        "Счет 73654108430135874305",
        "Счет 64686473678894779589",
    ]


@pytest.fixture
def invalid_card_account_strings() -> List[str]:
    """Фикстура с некорректными строками для mask_account_card."""
    return [
        "Visa Platinum",  # без номера
        "123",  # только номер
        "",  # пустая строка
        "Счет abc",  # номер с буквами
    ]


@pytest.fixture
def date_strings() -> List[str]:
    """Фикстура с датами в ISO-формате."""
    return [
        "2024-03-11T02:26:18.671407",
        "2024-12-25T15:30:00.123456",
        "2023-01-01T00:00:00.000000",
        "1999-12-31T23:59:59.999999",
    ]
