import os
from unittest.mock import patch

import pytest

from src.work_with_csv_excel import get_data_from_csv


def test_empty_path():
    with pytest.raises(ValueError, match="Путь к файлу не указан"):
        get_data_from_csv("")


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        get_data_from_csv("non_existent_file.csv")


def test_corrupted_csv():
    with patch("builtins.open", side_effect=UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")):
        with pytest.raises(Exception, match="Ошибка при чтении файла"):
            get_data_from_csv("fake_corrupted.csv")


def test_valid_csv():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "transactions.csv")
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
