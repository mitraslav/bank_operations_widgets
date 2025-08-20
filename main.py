from src.work_with_csv_excel import get_data_from_excel, get_data_from_csv
from src.utils import read_operations_from_json

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_input = int(input())
    if user_input == 1:
        print("Для обработки выбран JSON-файл.")
    elif user_input == 2:
        print("Для обработки выбран CSV-файл.")
    else:
        print("Для обработки выбран XLSX-файл.")

    print("Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    user_input_2 = input()

    if user_input_2.upper() == "EXECUTED":
        print('Операции отфильтрованы по статусу "EXECUTED"')
    elif user_input_2.upper() == "CANCELED":
        print('Операции отфильтрованы по статусу "CANCELED"')
    elif user_input_2.upper() == "PENDING":
        print('Операции отфильтрованы по статусу "PENDING"')
    else:


