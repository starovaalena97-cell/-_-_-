"""
Тесты для модуля widget с использованием параметризации
"""

import pytest
from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    """Тесты для функции mask_account_card."""

    @pytest.mark.parametrize("input_str, expected", [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ])
    def test_valid_inputs(self, input_str: str, expected: str) -> None:
        """Тестирует корректные входные данные."""
        assert mask_account_card(input_str) == expected

    @pytest.mark.parametrize("invalid_input, expected", [
        ("Visa Platinum", "Visa Platinum"),
        ("123", "123"),
        ("", ""),
        ("Счет abc", "Счет abc"),
        ("Visa Platinum 700079228960636a", "Visa Platinum 700079228960636a"),
    ])
    def test_invalid_inputs(self, invalid_input: str, expected: str) -> None:
        """Тестирует некорректные входные данные."""
        assert mask_account_card(invalid_input) == expected


class TestGetDate:
    """Тесты для функции get_date."""

    @pytest.mark.parametrize("input_date, expected", [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-12-25T15:30:00.123456", "25.12.2024"),
        ("2023-01-01T00:00:00.000000", "01.01.2023"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2025-07-04T08:15:30.000000", "04.07.2025"),
    ])
    def test_valid_dates(self, input_date: str, expected: str) -> None:
        """Тестирует корректные даты."""
        assert get_date(input_date) == expected
