"""
Тесты для модуля masks.
"""

import pytest
from src.masks import get_mask_card_number, get_mask_account


class TestMaskCardNumber:
    """Тесты для функции get_mask_card_number."""

    def test_valid_card(self):
        """Тест валидного номера карты."""
        result = get_mask_card_number("1234567812345678")
        assert result == "1234 56** **** 5678"

    def test_card_with_spaces(self):
        """Тест номера карты с пробелами."""
        result = get_mask_card_number("1234 5678 1234 5678")
        assert result == "1234 56** **** 5678"

    def test_invalid_length(self):
        """Тест некорректной длины."""
        result = get_mask_card_number("123456789")
        assert result == "Неверный номер карты"

    def test_not_digit(self):
        """Тест с буквами."""
        result = get_mask_card_number("1234abcd5678efgh")
        assert result == "Неверный номер карты"

    def test_empty_string(self):
        """Тест пустой строки."""
        result = get_mask_card_number("")
        assert result == "Неверный номер карты"

    def test_none_value(self):
        """Тест None."""
        result = get_mask_card_number(None)
        assert result == "Неверный номер карты"


class TestMaskAccount:
    """Тесты для функции get_mask_account."""

    def test_valid_account(self):
        """Тест валидного номера счёта."""
        result = get_mask_account("12345678901234567890")
        assert result == "**7890"

    def test_account_with_spaces(self):
        """Тест номера счёта с пробелами."""
        result = get_mask_account("1234 5678 9012 3456 7890")
        assert result == "**7890"

    def test_short_account(self):
        """Тест короткого номера счёта."""
        result = get_mask_account("123")
        assert result == "Неверный номер счёта"

    def test_not_digit(self):
        """Тест с буквами."""
        result = get_mask_account("abcd")
        assert result == "Неверный номер счёта"

    def test_empty_string(self):
        """Тест пустой строки."""
        result = get_mask_account("")
        assert result == "Неверный номер счёта"

    def test_none_value(self):
        """Тест None."""
        result = get_mask_account(None)
        assert result == "Неверный номер счёта"
