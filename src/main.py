"""
Главный модуль для взаимодействия с пользователем.
"""

from typing import List, Dict, Any

from src.utils import read_json_file
from src.file_reader import read_csv_transactions, read_excel_transactions
from src.search_utils import search_transactions, count_operations_by_category


def display_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Выводит транзакции в удобочитаемом формате."""
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши "
              "условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

    for tx in transactions:
        date = tx.get('date', 'Нет даты')[:10].replace('-', '.')
        description = tx.get('description', 'Без описания')
        amount = tx.get('operationAmount', {}).get('amount', '0')
        currency = (
            tx.get('operationAmount', {})
            .get('currency', {})
            .get('code', '')
        )
        from_account = tx.get('from', 'Неизвестно')
        to_account = tx.get('to', 'Неизвестно')

        print(f"{date} {description}")
        if from_account and to_account:
            print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}\n")


def get_user_choice(prompt: str, options: List[str]) -> str:
    """Запрашивает у пользователя выбор из доступных вариантов."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in options:
            return choice
        print(f'Статус операции "{choice}" недоступен.')


def main() -> None:
    """Основная логика программы."""
    print("Привет! Добро пожаловать в программу работы с "
          "банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()

    transactions: List[Dict[str, Any]] = []
    if choice == '1':
        print("Для обработки выбран JSON-файл.")
        transactions = read_json_file('data/operations.json')
    elif choice == '2':
        print("Для обработки выбран CSV-файл.")
        transactions = read_csv_transactions('data/transactions.csv')
    elif choice == '3':
        print("Для обработки выбран XLSX-файл.")
        transactions = read_excel_transactions('data/transactions_excel.xlsx')
    else:
        print("Неверный выбор.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    status = get_user_choice(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n",
        ['EXECUTED', 'CANCELED', 'PENDING']
    )

    filtered_by_status = [
        tx for tx in transactions if tx.get('state', '').upper() == status
    ]
    print(f"Операции отфильтрованы по статусу \"{status}\"")

    if not filtered_by_status:
        print("Не найдено ни одной транзакции с таким статусом.")
        return

    sort_choice = input(
        "Отсортировать операции по дате? Да/Нет\n"
    ).strip().lower()

    if sort_choice in ['да', 'yes']:
        order = input(
            "Отсортировать по возрастанию или по убыванию?\n"
        ).strip().lower()
        reverse = order in ['убыванию', 'desc']
        filtered_by_status.sort(
            key=lambda x: x.get('date', ''), reverse=reverse
        )

    rub_choice = input(
        "Выводить только рублевые транзакции? Да/Нет\n"
    ).strip().lower()

    if rub_choice in ['да', 'yes']:
        filtered_by_status = [
            tx for tx in filtered_by_status
            if (
                tx.get('operationAmount', {})
                .get('currency', {})
                .get('code', '') == 'RUB'
            )
        ]

    search_choice = input(
        "Отфильтровать список транзакций по определенному слову в описании? "
        "Да/Нет\n"
    ).strip().lower()

    if search_choice in ['да', 'yes']:
        search_word = input("Введите слово для поиска:\n").strip()
        filtered_by_status = search_transactions(
            filtered_by_status, search_word
        )

    print("Распечатываю итоговый список транзакций...")
    display_transactions(filtered_by_status)

    print("\nПодсчёт операций по категориям:")
    categories = [
        'Перевод организации',
        'Перевод с карты на карту',
        'Открытие вклада'
    ]
    category_counts = count_operations_by_category(
        filtered_by_status, categories
    )
    for cat, count in category_counts.items():
        print(f"{cat}: {count}")


if __name__ == "__main__":
    main()
