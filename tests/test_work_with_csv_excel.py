import os
from unittest.mock import patch

import pytest

from src.work_with_csv_excel import get_data_from_csv, get_data_from_excel


def test_csv_empty_path():
    with pytest.raises(ValueError, match="Путь к файлу не указан"):
        get_data_from_csv("")


def test_csv_missing_file():
    with pytest.raises(FileNotFoundError):
        get_data_from_csv("non_existent_file.csv")


def test_corrupted_csv():
    with patch("builtins.open", side_effect=UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")):
        with pytest.raises(Exception, match="Ошибка при чтении файла"):
            get_data_from_csv("fake_corrupted.csv")


def test_valid_csv():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "files\\transactions.csv")
    expected_result = {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
    assert get_data_from_csv(file_path)[0] == expected_result


def test_excel_empty_path():
    with pytest.raises(ValueError, match="Путь к файлу не указан"):
        get_data_from_excel("")


def test_excel_missing_file():
    with pytest.raises(FileNotFoundError, match="Файл не найден: missing_file.xlsx"):
        get_data_from_excel("missing_file.xlsx")


@patch("builtins.open")
def test_corrupted_excel(mock_open):
    mock_open.side_effect = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")
    with pytest.raises(Exception, match="Ошибка при чтении файла"):
        get_data_from_excel("corrupted_file.xlsx")


def test_valid_xlsx():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "files\\transactions_excel.xlsx")
    expected_result = [
        {
            "id": "650703.0",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210.0",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919.0",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740.0",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    result = get_data_from_excel(file_path)
    str_result = [{k: str(v) for k, v in row.items()} for row in result]
    assert str_result[0:2] == expected_result
