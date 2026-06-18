"""
Модуль с генераторами для работы с транзакциями.
Содержит функции для фильтрации по валюте, получения описаний и генерации номеров карт.
"""

from typing import Any, Dict, Iterator, List, Union


def filter_by_currency(
    transactions: List[Dict[str, Union[str, int, Dict[str, Any]]]], currency_code: str
) -> Iterator[Dict[str, Union[str, int, Dict[str, Any]]]]:
    """
    Фильтрует транзакции по заданной валюте.

    Аргументы:
        transactions: Список словарей с данными о транзакциях.
        currency_code: Код валюты для фильтрации (например, "USD" или "RUB").

    Возвращает:
        Итератор, который поочередно выдает транзакции с указанной валютой.
    """
    for transaction in transactions:
        try:
            operation_amount = transaction.get("operationAmount")
            if isinstance(operation_amount, dict):
                currency = operation_amount.get("currency")
                if isinstance(currency, dict):
                    if currency.get("code") == currency_code:
                        yield transaction
        except (AttributeError, TypeError):
            continue


def transaction_descriptions(
    transactions: List[Dict[str, Union[str, int, Dict[str, Any]]]]
) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции по очереди.

    Аргументы:
        transactions: Список словарей с данными о транзакциях.

    Возвращает:
        Итератор строк с описаниями транзакций.
    """
    for transaction in transactions:
        try:
            description = transaction.get("description")
            if isinstance(description, str) and description:
                yield description
        except (AttributeError, TypeError):
            continue


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в заданном диапазоне.

    Аргументы:
        start: Начальное значение диапазона (включительно).
        stop: Конечное значение диапазона (включительно).

    Возвращает:
        Итератор строк с номерами карт в формате "XXXX XXXX XXXX XXXX".
    """
    if start < 0 or start > stop:
        return

    if stop > 9999999999999999:
        stop = 9999999999999999

    for number in range(start, stop + 1):
        formatted = f"{number:016d}"
        yield f"{formatted[:4]} {formatted[4:8]} {formatted[8:12]} {formatted[12:16]}"
