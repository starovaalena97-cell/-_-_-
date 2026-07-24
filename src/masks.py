"""
Модуль для маскировки номеров карт и счетов.
"""

import re
from src.logger_config import setup_logger

logger = setup_logger(__name__, 'masks.log')


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX."""
    if not card_number or not isinstance(card_number, str):
        logger.error("Номер карты отсутствует или не является строкой")
        return "Неверный номер карты"

    cleaned = re.sub(r'\s+', '', card_number)

    if not cleaned.isdigit():
        logger.error("Номер карты содержит не цифры")
        return "Неверный номер карты"

    if len(cleaned) != 16:
        logger.error(f"Некорректная длина: {len(cleaned)} (ожидается 16)")
        return "Неверный номер карты"

    masked = f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[12:]}"
    logger.info(f"Номер карты успешно замаскирован: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта в формате **XXXX (последние 4 цифры)."""
    if not account_number or not isinstance(account_number, str):
        logger.error("Номер счёта отсутствует или не является строкой")
        return "Неверный номер счёта"

    cleaned = re.sub(r'\s+', '', account_number)

    if not cleaned.isdigit():
        logger.error("Номер счёта содержит не цифры")
        return "Неверный номер счёта"

    if len(cleaned) < 4:
        logger.error(f"Номер счёта слишком короткий: {len(cleaned)}")
        return "Неверный номер счёта"

    masked = f"**{cleaned[-4:]}"
    logger.info(f"Номер счёта успешно замаскирован: {masked}")
    return masked
