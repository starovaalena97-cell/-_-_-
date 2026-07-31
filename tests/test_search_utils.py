"""
Тесты для модуля search_utils.
"""

from src.search_utils import search_transactions, count_operations_by_category


class TestSearchTransactions:
    """Тесты для функции search_transactions."""

    def test_search_found(self):
        transactions = [
            {'description': 'Перевод организации'},
            {'description': 'Перевод с карты на карту'},
            {'description': 'Открытие вклада'}
        ]
        result = search_transactions(transactions, 'перевод')
        assert len(result) == 2

    def test_search_not_found(self):
        transactions = [
            {'description': 'Перевод организации'},
            {'description': 'Открытие вклада'}
        ]
        result = search_transactions(transactions, 'пополнение')
        assert result == []

    def test_search_case_insensitive(self):
        transactions = [{'description': 'Перевод организации'}]
        result = search_transactions(transactions, 'ПЕРЕВОД')
        assert len(result) == 1

    def test_search_empty_string(self):
        transactions = [{'description': 'Перевод'}]
        result = search_transactions(transactions, '')
        assert result == transactions

    def test_search_empty_list(self):
        result = search_transactions([], 'перевод')
        assert result == []

    def test_search_no_description(self):
        transactions = [{'id': 1}]
        result = search_transactions(transactions, 'перевод')
        assert result == []


class TestCountOperationsByCategory:
    """Тесты для функции count_operations_by_category."""

    def test_count_categories(self):
        transactions = [
            {'description': 'Перевод организации'},
            {'description': 'Перевод с карты на карту'},
            {'description': 'Открытие вклада'},
            {'description': 'Перевод организации'}
        ]
        categories = ['Перевод', 'Вклад']
        result = count_operations_by_category(transactions, categories)
        assert result == {'Перевод': 3, 'Вклад': 1}

    def test_empty_transactions(self):
        categories = ['Перевод', 'Вклад']
        result = count_operations_by_category([], categories)
        assert result == {'Перевод': 0, 'Вклад': 0}

    def test_empty_categories(self):
        transactions = [{'description': 'Перевод'}]
        result = count_operations_by_category(transactions, [])
        assert result == {}

    def test_case_insensitive(self):
        transactions = [{'description': 'ПЕРЕВОД организации'}]
        categories = ['перевод', 'вклад']
        result = count_operations_by_category(transactions, categories)
        assert result == {'перевод': 1, 'вклад': 0}
