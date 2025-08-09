import json
import logging
import os

os.makedirs('logs', exist_ok=True)

utils_logger = logging.getLogger('app.utils')
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join('logs', 'utils.log'), 'w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
utils_logger.addHandler(file_handler)

def read_operations_from_json(path: str) -> None | list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        utils_logger.info(f'Открывается файл по пути {path}')
        with open(path, encoding="utf-8") as p:
            transactions = json.load(p)
            if isinstance(transactions, list):
                utils_logger.info('Успешно выводится список транзакций')
                return transactions
            utils_logger.warning('Предоставлены данные некорректного формата')
            return []
    except (FileNotFoundError, PermissionError) as e:
        utils_logger.error(f'Произошла ошибка: {e}', exc_info=True)
        return []
