"""
Модуль для чтения финансовых транзакций из CSV и Excel-файлов.
"""

from typing import Any, Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с транзакциями.

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список словарей с данными транзакций.
        При ошибке возвращает пустой список.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient='records')
    except Exception:
        return []


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл (XLSX) и возвращает список словарей с транзакциями.

    Args:
        file_path: Путь к Excel-файлу

    Returns:
        Список словарей с данными транзакций.
        При ошибке возвращает пустой список.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df.to_dict(orient='records')
    except Exception:
        return []
