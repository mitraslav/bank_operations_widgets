import csv
from typing import Any


def get_data_from_csv(file_path: str) -> list[dict[str, Any]]:
    """Читает финансовые операции из CSV-файла и возвращает список словарей"""
    if not file_path:
        raise ValueError("Путь к файлу не указан")

    transactions = []
    try:
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions.append(row)
            return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла: {e}")


def get_data_from_excel(file_path: str) -> list[dict[str, Any]]:
    pass