"""
Тесты для модуля file_reader.
"""

import pytest
import pandas as pd
from unittest.mock import patch, Mock
from src.file_reader import read_csv_transactions, read_excel_transactions


class TestReadCsvTransactions:
    """Тесты для функции read_csv_transactions."""

    @patch('src.file_reader.pd.read_csv')
    def test_read_csv_success(self, mock_read_csv):
        """Тест успешного чтения CSV."""
        mock_df = Mock()
        mock_df.to_dict.return_value = [
            {'id': 1, 'amount': 100},
            {'id': 2, 'amount': 200}
        ]
        mock_read_csv.return_value = mock_df

        result = read_csv_transactions('test.csv')
        assert result == [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]

    @patch('src.file_reader.pd.read_csv')
    def test_read_csv_error(self, mock_read_csv):
        """Тест ошибки при чтении CSV."""
        mock_read_csv.side_effect = Exception('File not found')

        result = read_csv_transactions('test.csv')
        assert result == []


class TestReadExcelTransactions:
    """Тесты для функции read_excel_transactions."""

    @patch('src.file_reader.pd.read_excel')
    def test_read_excel_success(self, mock_read_excel):
        """Тест успешного чтения Excel."""
        mock_df = Mock()
        mock_df.to_dict.return_value = [
            {'id': 1, 'amount': 100},
            {'id': 2, 'amount': 200}
        ]
        mock_read_excel.return_value = mock_df

        result = read_excel_transactions('test.xlsx')
        assert result == [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]

    @patch('src.file_reader.pd.read_excel')
    def test_read_excel_error(self, mock_read_excel):
        """Тест ошибки при чтении Excel."""
        mock_read_excel.side_effect = Exception('File not found')

        result = read_excel_transactions('test.xlsx')
        assert result == []
