"""
Модуль для настройки логирования в проекте.
"""

import logging
import os

# Создаём папку logs, если её нет
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def setup_logger(name: str, log_file: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    Настраивает и возвращает логгер с указанным именем.

    Args:
        name: Имя логгера (обычно __name__)
        log_file: Имя файла для логов (например, 'utils.log')
        level: Уровень логирования (по умолчанию DEBUG)

    Returns:
        Настроенный объект логгера
    """
    # Создаём логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Если у логгера уже есть обработчики — не добавляем новые
    if logger.handlers:
        return logger

    # Полный путь к файлу лога
    log_path = os.path.join(LOG_DIR, log_file)

    # Создаём файловый обработчик (перезаписывает файл при каждом запуске)
    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    file_handler.setLevel(level)

    # Создаём форматер
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Привязываем форматер к обработчику
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
