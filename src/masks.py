"""
Модуль для маскировки номеров карт и счетов.
"""


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Принимает номер карты (16 цифр) и возвращает маску
    в формате XXXX XX** **** XXXX.

    Args:
        card_number: Номер карты в виде строки из 16 цифр

    Returns:
        Замаскированный номер карты с пробелами каждые 4 цифры

    Example:
        >>> get_mask_card_number("7000792289606361")
        '7000 79** **** 6361'
    """
    if len(card_number) != 16 or not card_number.isdigit():
        return card_number

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Принимает номер счета и возвращает маску в формате **XXXX,
    где XXXX - последние 4 цифры номера.

    Args:
        account_number: Номер счета в виде строки

    Returns:
        Замаскированный номер счета

    Example:
        >>> get_mask_account("73654108430135874305")
        '**4305'
    """
    if len(account_number) < 4:
        return account_number

    masked = f"**{account_number[-4:]}"
    return masked
