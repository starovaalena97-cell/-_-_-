"""
Модуль для работы с внешним API конвертации валют.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert'


def get_exchange_rate(from_currency: str, to_currency: str = 'RUB'):
    """Получает курс обмена валюты через внешнее API."""
    if not API_KEY:
        return None

    params = {'from': from_currency, 'to': to_currency, 'amount': 1}
    headers = {'apikey': API_KEY}

    try:
        response = requests.get(
            BASE_URL, params=params, headers=headers, timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get('result') if data.get('success') else None
    except Exception:
        return None


def convert_to_rubles(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли."""
    try:
        amount_str = transaction.get('operationAmount', {}).get('amount', '0')
        currency_code = transaction.get(
            'operationAmount', {}
        ).get('currency', {}).get('code', 'RUB')
        amount = float(amount_str)

        if currency_code == 'RUB':
            return amount

        rate = get_exchange_rate(currency_code)
        return round(amount * rate, 2) if rate else 0.0

    except (ValueError, TypeError, AttributeError):
        return 0.0
