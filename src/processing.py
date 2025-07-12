from typing import Dict, List


def filter_by_state(operations_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает список со словарями, у которых ключ 'state' соответствует указанному значению"""
    return [i for i in operations_list if i["state"] == state]


def sort_by_date(operations_list: List[Dict], descending: bool = True) -> List[Dict]:
    """Функция сортирует список словарей по дате"""
    return sorted(operations_list, key=lambda x: x["date"], reverse=descending)
