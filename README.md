# Banking Widget

Виджет для банковских операций.

## Описание

Проект содержит функции для маскировки номеров банковских карт и счетов.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/banking_widget.git
cd banking_widget

##  Декоратор для логирования

Модуль `decorators` предоставляет декоратор `log` для автоматического логирования выполнения функций.

## Работа с CSV и Excel

Модуль `file_reader` позволяет загружать транзакции из разных форматов:

```python
from src.file_reader import read_csv_transactions, read_excel_transactions

transactions_csv = read_csv_transactions('data/transactions.csv')
transactions_excel = read_excel_transactions('data/transactions_excel.xlsx')
