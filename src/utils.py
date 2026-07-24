"""
Модуль для работы с файлами JSON.
Содержит функции для чтения данных о транзакциях.
"""

import json
import os
from typing import List, Dict, Any
from src.logger_config import setup_logger

# Настраиваем логгер для модуля utils
logger = setup_logger(__name__, 'utils.log')


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными транзакций.

    Args:
        file_path: Путь к JSON-файлу

    Returns:
        Список словарей с данными транзакций.
        Если файл не найден, пустой или содержит не список - возвращает пустой список.
    """
    logger.debug(f"Попытка открыть файл: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info(f"Файл успешно прочитан: {file_path}, количество записей: {len(data)}")
            return data
        else:
            logger.error(f"Файл {file_path} содержит не список, а {type(data).__name__}")
            return []

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON в файле {file_path}: {e}")
        return []
    except OSError as e:
        logger.error(f"Ошибка при открытии файла {file_path}: {e}")
        return []
