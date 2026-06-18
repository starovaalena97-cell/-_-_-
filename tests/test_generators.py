"""
Тесты для модуля generators.
"""

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


class TestFilterByCurrency:
    """Тесты для функции filter_by_currency."""

    def test_filter_by_currency_usd(self, sample_transactions: list) -> None:
        """Тестирует фильтрацию по валюте USD."""
        usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
        assert len(usd_transactions) == 3
        for transaction in usd_transactions:
            amount = transaction.get("operationAmount")
            if isinstance(amount, dict):
                currency = amount.get("currency")
                if isinstance(currency, dict):
                    assert currency.get("code") == "USD"

    def test_filter_by_currency_rub(self, sample_transactions: list) -> None:
        """Тестирует фильтрацию по валюте RUB."""
        rub_transactions = list(filter_by_currency(sample_transactions, "RUB"))
        assert len(rub_transactions) == 2
        for transaction in rub_transactions:
            amount = transaction.get("operationAmount")
            if isinstance(amount, dict):
                currency = amount.get("currency")
                if isinstance(currency, dict):
                    assert currency.get("code") == "RUB"

    def test_filter_by_currency_no_match(self, sample_transactions: list) -> None:
        """Тестирует фильтрацию, когда нет совпадений."""
        result = list(filter_by_currency(sample_transactions, "EUR"))
        assert result == []

    def test_filter_by_currency_empty_list(self, empty_transactions: list) -> None:
        """Тестирует фильтрацию на пустом списке."""
        result = list(filter_by_currency(empty_transactions, "USD"))
        assert result == []

    def test_filter_by_currency_invalid_data(self) -> None:
        """Тестирует фильтрацию с некорректными данными."""
        transactions: list = [
            {"operationAmount": None},
            {"operationAmount": {"currency": {}}},
            {"operationAmount": {"currency": {"code": None}}},
            {"amount": "100", "currency": "USD"},
        ]
        result = list(filter_by_currency(transactions, "USD"))
        assert result == []


class TestTransactionDescriptions:
    """Тесты для функции transaction_descriptions."""

    def test_transaction_descriptions(self, sample_transactions: list) -> None:
        """Тестирует получение описаний транзакций."""
        descriptions = list(transaction_descriptions(sample_transactions))
        expected = [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
        assert descriptions == expected

    def test_transaction_descriptions_empty(self, empty_transactions: list) -> None:
        """Тестирует получение описаний из пустого списка."""
        descriptions = list(transaction_descriptions(empty_transactions))
        assert descriptions == []

    def test_transaction_descriptions_missing_description(self) -> None:
        """Тестирует транзакции без описания."""
        transactions: list = [
            {"id": 1, "amount": "100"},
            {"id": 2, "description": ""},
            {"id": 3, "description": None},
        ]
        descriptions = list(transaction_descriptions(transactions))
        assert descriptions == []

    def test_transaction_descriptions_generator(
        self, sample_transactions: list
    ) -> None:
        """Тестирует, что функция возвращает итератор."""
        descriptions = transaction_descriptions(sample_transactions)
        assert hasattr(descriptions, "__iter__")
        assert hasattr(descriptions, "__next__")


class TestCardNumberGenerator:
    """Тесты для функции card_number_generator."""

    @pytest.mark.parametrize(
        "start, stop, expected",
        [
            (
                1,
                5,
                [
                    "0000 0000 0000 0001",
                    "0000 0000 0000 0002",
                    "0000 0000 0000 0003",
                    "0000 0000 0000 0004",
                    "0000 0000 0000 0005",
                ],
            ),
            (
                0,
                3,
                [
                    "0000 0000 0000 0000",
                    "0000 0000 0000 0001",
                    "0000 0000 0000 0002",
                    "0000 0000 0000 0003",
                ],
            ),
            (
                9999999999999998,
                9999999999999999,
                ["9999 9999 9999 9998", "9999 9999 9999 9999"],
            ),
        ],
    )
    def test_card_number_generator(self, start: int, stop: int, expected: list) -> None:
        """Тестирует генератор номеров карт."""
        result = list(card_number_generator(start, stop))
        assert result == expected

    def test_card_number_generator_single(self) -> None:
        """Тестирует генератор с одним номером."""
        result = list(card_number_generator(42, 42))
        assert result == ["0000 0000 0000 0042"]

    def test_card_number_generator_format(self) -> None:
        """Тестирует формат номеров карт."""
        result = list(card_number_generator(1, 3))
        for card in result:
            parts = card.split()
            assert len(parts) == 4
            for part in parts:
                assert len(part) == 4
                assert part.isdigit()

    def test_card_number_generator_out_of_range(self) -> None:
        """Тестирует генератор с невалидными значениями."""
        result = list(card_number_generator(-1, 0))
        assert result == []
        result = list(card_number_generator(9999999999999999, 10000000000000000))
        assert result == ["9999 9999 9999 9999"]
