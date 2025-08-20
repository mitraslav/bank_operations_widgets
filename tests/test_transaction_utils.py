from src.transaction_utils import process_bank_search, process_bank_operations
import pytest

def test_process_bank_search(incomplete_transactions):
    expected_result = [{
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }]
    assert process_bank_search(incomplete_transactions, "перевод") == expected_result

def test_process_bank_search_empty():
    with pytest.raises(ValueError, match='Data or search parameter is absent'):
        process_bank_search([], 'hello')
    with pytest.raises(ValueError, match='Data or search parameter is absent'):
        process_bank_search([{'hello': '1'}], "")
    with pytest.raises(ValueError, match='Data or search parameter is absent'):
        process_bank_search([], "")


def test_process_bank_search_exception():
    invalid_data = [{"description": None}]
    with pytest.raises(Exception) as exc_info:
        process_bank_search(invalid_data, "hello")
    assert "Ошибка при чтении данных" in str(exc_info.value)

def test_process_bank_operations(transactions):
    expected_result = {"Перевод организации": 2,
                        "Перевод со счета на счет": 2
                        }
    assert process_bank_operations(transactions, ["Перевод организации", "Перевод со счета на счет"]) == expected_result


def test_process_bank_operations_empty():
    with pytest.raises(ValueError, match='Data or categories parameter is absent'):
        process_bank_operations([], ['hello'])
    with pytest.raises(ValueError, match='Data or categories parameter is absent'):
        process_bank_operations([{'hello': '1'}], [])
    with pytest.raises(ValueError, match='Data or categories parameter is absent'):
        process_bank_operations([], [])

def test_process_bank_operations_exception():
    invalid_data = {"description": None}
    with pytest.raises(Exception) as exc_info:
        process_bank_operations(invalid_data, ['hello'])
    assert "Ошибка при чтении данных" in str(exc_info.value)

