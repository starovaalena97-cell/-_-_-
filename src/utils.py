"""
Модуль для работы с файлами JSON.
"""

import json
import os
from typing import Any, Dict, List

from src.logger_config import setup_logger

logger = setup_logger(__name__, 'utils.log')


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей."""
    logger.debug(f"Попытка открыть файл: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info(f"Файл прочитан: {file_path}, записей: {len(data)}")
            return data

        logger.error(
            f"Файл {file_path} содержит не список, а {type(data).__name__}"
        )
        return []

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
        return []
    except OSError as e:
        logger.error(f"Ошибка при открытии файла: {e}")
        return []
