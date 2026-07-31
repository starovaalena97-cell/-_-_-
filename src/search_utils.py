"""
Модуль для поиска по описанию и подсчёта категорий операций.
"""

import re
from collections import Counter
from typing import Any, Dict, List


def search_transactions(
    transactions: List[Dict[str, Any]], search_string: str
) -> List[Dict[str, Any]]:
    """
    Ищет транзакции, в которых описание содержит заданную строку
    (регистронезависимо).
    """
    if not search_string:
        return transactions

    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    result = []

    for transaction in transactions:
        description = transaction.get('description', '')
        if pattern.search(description):
            result.append(transaction)

    return result


def count_operations_by_category(
    transactions: List[Dict[str, Any]], categories: List[str]
) -> Dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям на основе поля
    description.
    """
    if not transactions or not categories:
        return {category: 0 for category in categories}

    counter = Counter()

    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                counter[category] += 1
                break

    for category in categories:
        if category not in counter:
            counter[category] = 0

    return dict(counter)
