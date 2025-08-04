from unittest.mock import mock_open, patch

from src.utils import read_operations_from_json


def test_read_operations_from_json(utils_data):
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("json.load", return_value=utils_data):
            result = read_operations_from_json("small_path.json")
            assert result == utils_data
            mock_file.assert_called_once_with("small_path.json", encoding="utf-8")


def test_read_operations_from_json_wrong_input():
    assert read_operations_from_json(("")) == []

    with patch("builtins.open", mock_open()):
        with patch("json.load", return_value={"key": "value"}):
            assert read_operations_from_json("{invalid json}") == []

    with patch("builtins.open", side_effect=FileNotFoundError):
        assert read_operations_from_json("i_do_not_exist.json") == []

    with patch("builtins.open", side_effect=PermissionError):
        assert read_operations_from_json("not_permitted_file.json") == []
