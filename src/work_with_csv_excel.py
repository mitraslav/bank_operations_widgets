import csv
import os
from typing import Any, Dict, List, cast

import pandas as pd


def get_data_from_csv(path: str) -> List[Dict[str, Any]]:
    """Читает финансовые операции из CSV-файла и возвращает список словарей"""
    if not path:
        raise ValueError("Путь к файлу не указан")

    transactions: List[Dict[str, Any]] = []
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "..", path)
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions.append(row)
            return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {path}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла: {e}")


def get_data_from_excel(path: str) -> List[Dict[str, Any]]:
    """Читает финансовые операции из XLSX-файла и возвращает список словарей"""
    if not path:
        raise ValueError("Путь к файлу не указан")

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "..", path)
        data = pd.read_excel(file_path)
        df = pd.DataFrame(data)
        return cast(List[Dict[str, Any]], df.to_dict(orient="records"))

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {path}")
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла: {e}")
