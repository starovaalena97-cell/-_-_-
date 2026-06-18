"""
Фикстуры для тестов проекта.
"""

import pytest
from typing import Any, Dict, List


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
        "1234",
        "700079228960636a",
        "",
        "12345678901234567",
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
        "123",
        "",
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
        "Visa Platinum",
        "123",
        "",
        "Счет abc",
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


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с транзакциями для тестирования генераторов."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture
def empty_transactions() -> List[Dict[str, Any]]:
    """Фикстура с пустым списком транзакций."""
    return []
