"""
Тесты для модуля widget.
"""

from src.widget import get_date, mask_account_card


def test_mask_account_card_card() -> None:
    """Тестирует маскировку номера карты."""
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result == "Visa Platinum 7000 79** **** 6361"

    result = mask_account_card("Maestro 1596837868705199")
    assert result == "Maestro 1596 83** **** 5199"

    result = mask_account_card("MasterCard 7158300734726758")
    assert result == "MasterCard 7158 30** **** 6758"


def test_mask_account_card_account() -> None:
    """Тестирует маскировку номера счета."""
    result = mask_account_card("Счет 73654108430135874305")
    assert result == "Счет **4305"

    result = mask_account_card("Счет 64686473678894779589")
    assert result == "Счет **9589"


def test_mask_account_card_invalid() -> None:
    """Тестирует некорректные входные данные."""
    # Меньше 2 частей
    result = mask_account_card("123")
    assert result == "123"

    # Номер с буквами
    result = mask_account_card("Visa Platinum 700079228960636a")
    assert result == "Visa Platinum 700079228960636a"

    # Пустая строка
    result = mask_account_card("")
    assert result == ""


def test_get_date() -> None:
    """Тестирует преобразование даты."""
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"

    result = get_date("2025-12-25T15:30:00.123456")
    assert result == "25.12.2025"

    result = get_date("2023-01-01T00:00:00.000000")
    assert result == "01.01.2023"


if __name__ == "__main__":
    test_mask_account_card_card()
    test_mask_account_card_account()
    test_mask_account_card_invalid()
    test_get_date()
    print("Все тесты пройдены успешно!")
