from typing import Dict, List


def filter_by_state(operations_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает список со словарями, у которых ключ 'state' соответствует указанному значению"""
    return [i for i in operations_list if i["state"] == state]
