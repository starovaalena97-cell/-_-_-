"""
Модуль с декораторами для логирования.
"""

import functools
import os
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Аргументы:
        filename: Имя файла для записи логов. Если не указан, логи выводятся в консоль.

    Возвращает:
        Декоратор, который оборачивает функцию и логирует её выполнение.

    Примеры:
        @log(filename="mylog.txt")
        def my_function(x, y):
            return x + y

        my_function(1, 2)  # Запишет "my_function ok" в mylog.txt

        @log()
        def my_function(x, y):
            raise ValueError("Ошибка")

        my_function(1, 2)  # Выведет в консоль
        # "my_function error: ValueError. Inputs: (1, 2), {}"
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                error_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(error_message, filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str] = None) -> None:
    """
    Записывает сообщение в файл или выводит в консоль.

    Аргументы:
        message: Сообщение для записи.
        filename: Имя файла для записи. Если не указан, выводит в консоль.
    """
    if filename:
        dir_name = os.path.dirname(filename) if os.path.dirname(filename) else "."
        os.makedirs(dir_name, exist_ok=True)
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
