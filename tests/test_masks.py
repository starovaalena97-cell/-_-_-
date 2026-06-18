"""
Тесты для модуля masks.
"""

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Тестирует маскировку номера карты."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_length() -> None:
    """Тестирует номер карты неправильной длины."""
    assert get_mask_card_number("1234") == "1234"


def test_get_mask_card_number_with_letters() -> None:
    """Тестирует номер карты с буквами."""
    assert get_mask_card_number("700079228960636a") == "700079228960636a"


def test_get_mask_account() -> None:
    """Тестирует маскировку номера счета."""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_short() -> None:
    """Тестирует короткий номер счета."""
    assert get_mask_account("123") == "123"


def test_get_mask_account_four_digits() -> None:
    """Тестирует номер счета из 4 цифр."""
    assert get_mask_account("1234") == "**1234"


if __name__ == "__main__":
    test_get_mask_card_number()
    test_get_mask_card_number_invalid_length()
    test_get_mask_card_number_with_letters()
    test_get_mask_account()
    test_get_mask_account_short()
    test_get_mask_account_four_digits()
    print("Все тесты пройдены успешно!")
