import re

def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Фильтрует список банковских операций по строке поиска в описании"""
    if not data or not search:
        raise ValueError('Data or search parameter is absent')
    try:
        filtered_operations = []
        pattern = re.compile(re.escape(search), re.IGNORECASE)

        for operation in data:
            description = operation.get('description', "")
            if pattern.search(description):
                filtered_operations.append(operation)
        return filtered_operations
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла: {e}")


def process_bank_operations(data:list[dict], categories:list)->dict:
    pass