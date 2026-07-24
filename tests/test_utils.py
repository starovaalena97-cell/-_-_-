"""
Тесты для модуля utils.
"""

import pytest
import json
import os
from unittest.mock import mock_open, patch
from src.utils import read_json_file


class TestReadJsonFile:
    """Тесты для функции read_json_file."""

    def test_read_valid_json(self):
        """Тест чтения валидного JSON-файла."""
        mock_data = [
            {"id": 1, "description": "Test 1"},
            {"id": 2, "description": "Test 2"}
        ]

        with patch('builtins.open', mock_open(read_data=json.dumps(mock_data))):
            with patch('os.path.exists', return_value=True):
                result = read_json_file('test.json')
                assert result == mock_data
                assert len(result) == 2

    def test_file_not_found(self):
        """Тест когда файл не найден."""
        with patch('os.path.exists', return_value=False):
            result = read_json_file('not_exist.json')
            assert result == []

    def test_empty_file(self):
        """Тест пустого файла."""
        with patch('builtins.open', mock_open(read_data='')):
            with patch('os.path.exists', return_value=True):
                result = read_json_file('empty.json')
                assert result == []

    def test_invalid_json(self):
        """Тест невалидного JSON."""
        with patch('builtins.open', mock_open(read_data='{invalid json}')):
            with patch('os.path.exists', return_value=True):
                result = read_json_file('invalid.json')
                assert result == []

    def test_not_list_json(self):
        """Тест когда JSON не список."""
        with patch('builtins.open', mock_open(read_data='{"key": "value"}')):
            with patch('os.path.exists', return_value=True):
                result = read_json_file('not_list.json')
                assert result == []
