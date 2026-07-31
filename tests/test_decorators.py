"""
Тесты для модуля decorators.
"""

import os
from typing import Any

import pytest

from src.decorators import log


class TestLogDecorator:
    """Тесты для декоратора log."""

    def test_log_success_console(self, capsys: Any) -> None:
        """Тестирует логирование успешного выполнения в консоль."""

        @log()
        def add(a: int, b: int) -> int:
            return a + b

        result = add(1, 2)
        assert result == 3
        captured = capsys.readouterr()
        assert "add ok" in captured.out

    def test_log_error_console(self, capsys: Any) -> None:
        """Тестирует логирование ошибки в консоль."""

        @log()
        def error_func(a: int, b: int) -> None:
            raise ValueError("Тестовая ошибка")

        with pytest.raises(ValueError, match="Тестовая ошибка"):
            error_func(1, 2)
        captured = capsys.readouterr()
        assert "error_func error: ValueError" in captured.out
        assert "Inputs: (1, 2), {}" in captured.out

    def test_log_success_file(self) -> None:
        """Тестирует логирование успешного выполнения в файл."""
        test_file = "test_log.txt"
        # Удаляем файл, если он существует
        if os.path.exists(test_file):
            os.remove(test_file)

        @log(filename=test_file)
        def add(a: int, b: int) -> int:
            return a + b

        result = add(3, 4)
        assert result == 7

        assert os.path.exists(test_file)
        with open(test_file, "r", encoding="utf-8") as f:
            content = f.read()
            assert "add ok" in content

        # Очистка
        os.remove(test_file)

    def test_log_error_file(self) -> None:
        """Тестирует логирование ошибки в файл."""
        test_file = "test_log.txt"
        # Удаляем файл, если он существует
        if os.path.exists(test_file):
            os.remove(test_file)

        @log(filename=test_file)
        def error_func(a: int, b: int) -> None:
            raise ValueError("Тестовая ошибка")

        with pytest.raises(ValueError, match="Тестовая ошибка"):
            error_func(5, 6)

        assert os.path.exists(test_file)
        with open(test_file, "r", encoding="utf-8") as f:
            content = f.read()
            assert "error_func error: ValueError" in content
            assert "Inputs: (5, 6), {}" in content

        # Очистка
        os.remove(test_file)

    def test_log_with_different_args(self, capsys: Any) -> None:
        """Тестирует логирование с разными аргументами."""

        @log()
        def multiply(x: int, y: int, z: int = 1) -> int:
            return x * y * z

        result = multiply(2, 3, z=4)
        assert result == 24
        captured = capsys.readouterr()
        assert "multiply ok" in captured.out

    def test_log_with_kwargs(self, capsys: Any) -> None:
        """Тестирует логирование с именованными аргументами."""

        @log()
        def greet(name: str, greeting: str = "Hello") -> str:
            return f"{greeting}, {name}!"

        result = greet("Alice", greeting="Hi")
        assert result == "Hi, Alice!"
        captured = capsys.readouterr()
        assert "greet ok" in captured.out

    def test_log_error_with_kwargs(self, capsys: Any) -> None:
        """Тестирует логирование ошибки с именованными аргументами."""

        @log()
        def divide(a: int, b: int) -> float:
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

        captured = capsys.readouterr()
        assert "divide error: ZeroDivisionError" in captured.out
        assert "Inputs: (10, 0), {}" in captured.out

    def test_log_multiple_calls(self, capsys: Any) -> None:
        """Тестирует логирование нескольких вызовов."""

        @log()
        def increment(x: int) -> int:
            return x + 1

        for i in range(3):
            result = increment(i)
            assert result == i + 1

        captured = capsys.readouterr()
        # Проверяем, что было 3 записи в лог
        assert captured.out.count("increment ok") == 3

    def test_log_without_filename(self, capsys: Any) -> None:
        """Тестирует логирование без указания имени файла (в консоль)."""

        @log()
        def hello(name: str) -> str:
            return f"Hello, {name}!"

        result = hello("World")
        assert result == "Hello, World!"
        captured = capsys.readouterr()
        assert "hello ok" in captured.out

    def test_log_with_filename_empty_string(self) -> None:
        """Тестирует логирование с пустым именем файла."""
        test_file = ""

        @log(filename=test_file)
        def empty_filename_func(x: int) -> int:
            return x * 2

        # При пустом имени файла логи должны выводиться в консоль
        result = empty_filename_func(5)
        assert result == 10
        # Файл не должен создаваться
        assert not os.path.exists(test_file)
