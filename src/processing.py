"""
Модуль для обработки данных банковских операций.
Содержит функции фильтрации и сортировки операций.
"""

from typing import Dict, List, Union  # Убрали Any, т.к. не используется


def filter_by_state(
    operations: List[Dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[str, int]]]:
    """
    Фильтрует список операций по значению ключа 'state'.

    Аргументы:
        operations: Список словарей с данными об операциях.
        state: Значение для фильтрации по ключу 'state'. По умолчанию 'EXECUTED'.

    Возвращает:
        Новый список словарей, содержащий только операции с указанным статусом.

    Примеры:
        >>> ops = [
        ...     {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        ...     {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}
        ... ]
        >>> filter_by_state(ops)
        [{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'}]
        >>> filter_by_state(ops, 'CANCELED')
        [{'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}]
    """
    result = []
    for operation in operations:
        if operation.get("state") == state:
            result.append(operation)
    return result


def sort_by_date(
    operations: List[Dict[str, Union[str, int]]], descending: bool = True
) -> List[Dict[str, Union[str, int]]]:
    """
    Сортирует список операций по дате.

    Аргументы:
        operations: Список словарей с данными об операциях.
        descending: Порядок сортировки. True - по убыванию (сначала новые),
                   False - по возрастанию (сначала старые). По умолчанию True.

    Возвращает:
        Новый список словарей, отсортированных по дате.

    Примеры:
        >>> ops = [
        ...     {'date': '2023-01-01T10:00:00'},
        ...     {'date': '2023-01-02T08:00:00'},
        ...     {'date': '2022-12-31T23:59:59'}
        ... ]
        >>> sort_by_date(ops)
        [
            {'date': '2023-01-02T08:00:00'},
            {'date': '2023-01-01T10:00:00'},
            {'date': '2022-12-31T23:59:59'}
        ]
    """
    return sorted(operations, key=lambda x: x.get("date", ""), reverse=descending)
