from typing import Any, Dict, List


def filter_by_state(operations_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает список со словарями, у которых ключ 'state' соответствует указанному значению"""
    return [i for i in operations_list if i["state"] == state]


def sort_by_date(operations_list: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортирует список словарей по дате"""
    return sorted(operations_list, key=lambda x: x["date"], reverse=descending)
