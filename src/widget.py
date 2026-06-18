"""
Модуль для работы с виджетом банковских операций.
Содержит функции для маскировки данных и форматирования дат.
"""

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в строке.

    Аргументы:
        account_info (str): Строка с типом и номером карты/счета.
                            Например: "Visa Platinum 7000792289606361"
                            или "Счет 73654108430135874305"

    Возвращает:
        str: Строка с замаскированным номером.
             Для карт: "Visa Platinum 7000 79** **** 6361"
             Для счетов: "Счет **4305"

    Примеры:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    # Разделяем строку на части
    parts = account_info.split()

    # Если меньше 2 частей - возвращаем как есть
    if len(parts) < 2:
        return account_info

    # Последняя часть - это номер
    number = parts[-1]
    # Всё остальное - это тип (первые parts[:-1])
    card_type = " ".join(parts[:-1])

    # Проверяем, что номер состоит только из цифр
    if not number.isdigit():
        return account_info

    # Определяем, что это: счет или карта
    if "Счет" in card_type or "счет" in card_type:
        # Это счет
        masked_number = get_mask_account(number)
    else:
        # Это карта
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из ISO-формата в формат ДД.ММ.ГГГГ.

    Аргументы:
        date_string (str): Дата в формате "2024-03-11T02:26:18.671407"

    Возвращает:
        str: Дата в формате "ДД.ММ.ГГГГ" (например, "11.03.2024")

    Пример:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    # Парсим строку в объект datetime
    dt = datetime.fromisoformat(date_string)

    # Форматируем в нужный вид
    return dt.strftime("%d.%m.%Y")

# Версия
