import json


def read_operations_from_json(path: str) -> None|list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as p:
                transactions = json.load(p)
                if isinstance(transactions, list):
                    return transactions
                return []
    except (FileNotFoundError, PermissionError):
        return []
