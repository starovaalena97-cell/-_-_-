"""
Модуль для маскировки номеров карт и счетов.
"""

import re
from src.logger_config import setup_logger

# Настраиваем логгер для модуля masks
logger = setup_logger(__name__, 'masks.log')


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.

    Args:
        card_number: Номер карты (строка из 16 цифр)

    Returns:
        Замаскированный номер карты или сообщение об ошибке
    """
    logger.debug(f"Маскировка номера карты: {card_number[:4]}****")

    if not card_number or not isinstance(card_number, str):
        logger.error("Номер карты отсутствует или не является строкой")
        return "Неверный номер карты"

    # Удаляем пробелы
    cleaned = re.sub(r'\s+', '', card_number)

    if not cleaned.isdigit():
        logger.error(f"Номер карты содержит не цифры: {cleaned[:4]}****")
        return "Неверный номер карты"

    if len(cleaned) != 16:
        logger.error(f"Некорректная длина номера карты: {len(cleaned)} (ожидается 16)")
        return "Неверный номер карты"

    # Маскировка: XXXX XX** **** XXXX
    masked = f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[12:]}"
    logger.info(f"Номер карты успешно замаскирован: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта в формате **XXXX (последние 4 цифры).

    Args:
        account_number: Номер счёта (строка)

    Returns:
        Замаскированный номер счёта или сообщение об ошибке
    """
    logger.debug(f"Маскировка номера счёта: ****{account_number[-4:] if account_number else 'None'}")

    if not account_number or not isinstance(account_number, str):
        logger.error("Номер счёта отсутствует или не является строкой")
        return "Неверный номер счёта"

    # Удаляем пробелы
    cleaned = re.sub(r'\s+', '', account_number)

    if not cleaned.isdigit():
        logger.error(f"Номер счёта содержит не цифры: ****{cleaned[-4:] if len(cleaned) >= 4 else cleaned}")
        return "Неверный номер счёта"

    if len(cleaned) < 4:
        logger.error(f"Номер счёта слишком короткий: {len(cleaned)} (минимум 4 символа)")
        return "Неверный номер счёта"

    masked = f"**{cleaned[-4:]}"
    logger.info(f"Номер счёта успешно замаскирован: {masked}")
    return masked
