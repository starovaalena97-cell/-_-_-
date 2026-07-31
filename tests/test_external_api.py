"""
Тесты для модуля external_api.
"""

from unittest.mock import Mock, patch

from src.external_api import convert_to_rubles, get_exchange_rate


class TestGetExchangeRate:
    """Тесты для функции get_exchange_rate."""

    @patch('src.external_api.requests.get')
    def test_successful_request(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'success': True, 'result': 92.50}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        rate = get_exchange_rate('USD')
        assert rate == 92.50

    @patch('src.external_api.requests.get')
    def test_api_error(self, mock_get):
        mock_get.side_effect = Exception('API Error')
        rate = get_exchange_rate('USD')
        assert rate is None

    def test_no_api_key(self):
        with patch('src.external_api.API_KEY', None):
            rate = get_exchange_rate('USD')
            assert rate is None


class TestConvertToRubles:
    """Тесты для функции convert_to_rubles."""

    def test_convert_usd_to_rub(self):
        transaction = {
            'operationAmount': {'amount': '100.00', 'currency': {'code': 'USD'}}
        }
        with patch('src.external_api.get_exchange_rate', return_value=92.50):
            result = convert_to_rubles(transaction)
            assert result == 9250.00

    def test_convert_eur_to_rub(self):
        transaction = {
            'operationAmount': {'amount': '50.00', 'currency': {'code': 'EUR'}}
        }
        with patch('src.external_api.get_exchange_rate', return_value=101.20):
            result = convert_to_rubles(transaction)
            assert result == 5060.00

    def test_already_rub(self):
        transaction = {
            'operationAmount': {'amount': '5000.00', 'currency': {'code': 'RUB'}}
        }
        result = convert_to_rubles(transaction)
        assert result == 5000.00

    def test_api_failure(self):
        transaction = {
            'operationAmount': {'amount': '100.00', 'currency': {'code': 'USD'}}
        }
        with patch('src.external_api.get_exchange_rate', return_value=None):
            result = convert_to_rubles(transaction)
            assert result == 0.0

    def test_invalid_transaction(self):
        result = convert_to_rubles({})
        assert result == 0.0
