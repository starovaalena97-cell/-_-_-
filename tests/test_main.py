"""
Тесты для модуля main (только функции отображения).
"""

from src.main import display_transactions


def test_display_empty(capsys):
    display_transactions([])
    captured = capsys.readouterr()
    assert "Не найдено ни одной транзакции" in captured.out
