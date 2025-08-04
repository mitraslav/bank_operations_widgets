import json
from unittest.mock import Mock, patch

import pytest

from src.external_api import get_amount


def test_get_amount(convert_eur, single_transaction):
    mock_response = Mock()
    mock_response.json.return_value = json.loads(convert_eur)

    with patch("requests.get", return_value=mock_response):
        result = get_amount(single_transaction)

        expected_result = json.loads(convert_eur)["result"]
        assert result == expected_result


def test_get_amount_errors():
    with pytest.raises(KeyError) as exc_info:
        get_amount({"operationAmount": {}})

    assert "'currency'" in str(exc_info.value)

    with pytest.raises(Exception) as exc_info:
        get_amount({"operationAmount": {"amount": "not_a_number", "currency": {"code": "RUB"}}})

    assert "could not convert string to float" in str(exc_info.value)
