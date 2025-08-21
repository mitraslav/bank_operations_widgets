import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Фильтрует список банковских операций по строке поиска в описании"""
    if not data or not search:
        raise ValueError("Data or search parameter is absent")
    try:
        filtered_operations = []
        pattern = re.compile(re.escape(search), re.IGNORECASE)

        for operation in data:
            description = operation.get("description", "")
            if pattern.search(description):
                filtered_operations.append(operation)
        return filtered_operations
    except Exception as e:
        raise Exception(f"Ошибка при чтении данных: {e}")


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей и список категорий и возвращает словарь с количеством операций каждой категории"""
    if not data or not categories:
        raise ValueError("Data or categories parameter is absent")
    try:
        data_categories_list = [operation.get("description", "") for operation in data]

        categories_dict = Counter(data_categories_list)
        result_dict = {c: categories_dict.get(c) for c in categories_dict if c in categories}
        return result_dict

    except Exception as e:
        raise Exception(f"Ошибка при чтении данных: {e}")
