import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def valid_operations():
    """Фикстура с валидными данными операций"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-12T10:30:00"},
        {"id": 2, "state": "PENDING", "date": "2023-03-15T08:45:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-05-20T14:15:00"},
        {"id": 4, "state": "CANCELED", "date": "2023-01-05T09:10:00"},
        {"id": 5, "state": "EXECUTED", "date": "2022-12-31T23:59:59"},
    ]


@pytest.fixture
def edge_case_operations():
    """Фикстура с пограничными случаями"""
    return [
        {"id": 6, "date": "2023-01-01"},  # Нет state
        {"id": 7, "state": "EXECUTED"},  # Нет date
        {"id": 8, "state": "EXECUTED", "date": None},
        {"id": 9, "state": "EXECUTED", "date": ""},
        {"id": 10, "state": "EXECUTED", "date": 123},
        "not_a_dict",  # Не словарь
        None,  # None вместо словаря
    ]


@pytest.fixture
def mixed_operations(valid_operations, edge_case_operations):
    """Фикстура с смешанными валидными и невалидными данными"""
    return valid_operations + edge_case_operations


def test_filter_by_state_with_valid_data(valid_operations):
    """Тест фильтрации с валидными данными"""
    result = filter_by_state(valid_operations, "EXECUTED")
    assert len(result) == 3
    assert all(op["state"] == "EXECUTED" for op in result)
    assert {op["id"] for op in result} == {1, 3, 5}


def test_filter_by_state_with_edge_cases(edge_case_operations):
    """Тест фильтрации с пограничными случаями"""
    assert filter_by_state(edge_case_operations, "EXECUTED") == []


def test_filter_by_state_with_mixed_data(mixed_operations):
    """Тест фильтрации со смешанными данными"""
    result = filter_by_state(mixed_operations, "EXECUTED")
    assert len(result) == 3
    assert all(op["state"] == "EXECUTED" for op in result)
    assert {op["id"] for op in result} == {1, 3, 5}


@pytest.fixture
def sample_operations():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def empty_operations():
    return []


@pytest.mark.parametrize(
    "descending, expected_order",
    [(True, [41428829, 615064591, 594226727, 939719570]), (False, [939719570, 594226727, 615064591, 41428829])],
)
def test_sort_operations(sample_operations, descending, expected_order):
    """Параметризованный тест для сортировки по дате."""
    sorted_ops = sort_by_date(sample_operations, descending)
    assert [op["id"] for op in sorted_ops] == expected_order


# Тест для пустого списка
def test_empty_list(empty_operations):
    """Тест обработки пустого списка."""
    assert sort_by_date(empty_operations) == []
