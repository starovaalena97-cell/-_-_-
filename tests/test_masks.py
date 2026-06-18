"""
Тесты для модуля masks с использованием параметризации
"""

import pytest
from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    """Тесты для функции get_mask_card_number."""

    @pytest.mark.parametrize("card_number, expected", [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("0000000000000000", "0000 00** **** 0000"),
        ("9999999999999999", "9999 99** **** 9999"),
    ])
    def test_valid_card_numbers(self, card_number: str, expected: str) -> None:
        """Тестирует корректные номера карт."""
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize("invalid_input, expected", [
        ("1234", "1234"),
        ("700079228960636a", "700079228960636a"),
        ("", ""),
        ("12345678901234567", "12345678901234567"),
    ])
    def test_invalid_card_numbers(self, invalid_input: str, expected: str) -> None:
        """Тестирует некорректные номера карт."""
        assert get_mask_card_number(invalid_input) == expected


class TestGetMaskAccount:
    """Тесты для функции get_mask_account."""

    @pytest.mark.parametrize("account_number, expected", [
        ("73654108430135874305", "**4305"),
        ("1234567890", "**7890"),
        ("1234", "**1234"),
        ("0000", "**0000"),
    ])
    def test_valid_account_numbers(self, account_number: str, expected: str) -> None:
        """Тестирует корректные номера счетов."""
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize("invalid_input, expected", [
        ("123", "123"),
        ("", ""),
        ("abc", "abc"),
    ])
    def test_invalid_account_numbers(self, invalid_input: str, expected: str) -> None:
        """Тестирует некорректные номера счетов."""
        assert get_mask_account(invalid_input) == expected
