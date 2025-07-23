from typing import Any, Dict, List, Optional


def filter_by_state(operations_list: Optional[List[Dict[str, Any]]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует операции по состоянию."""
    if not operations_list:
        return []

    result = []
    for operation in operations_list:
        # Пропускаем всё, что не является словарем
        if not isinstance(operation, dict):
            continue

        # Проверяем наличие state и что он строковый
        if not isinstance(operation.get("state"), str):
            continue

        # Если state совпадает с искомым - добавляем
        if operation["state"] == state:
            # Дополнительно проверяем наличие даты в правильном формате
            date = operation.get("date")
            if isinstance(date, str) and date.strip():
                result.append(operation)

    return result


def sort_by_date(operations_list: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список операций по дате."""
    return sorted(operations_list, key=lambda x: x["date"], reverse=descending)
