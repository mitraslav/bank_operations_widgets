from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transaction_utils import process_bank_search
from src.utils import read_operations_from_json
from src.widget import get_date, mask_account_card
from src.work_with_csv_excel import get_data_from_csv, get_data_from_excel


def main(path: str) -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    try:
        user_input = int(input().strip())
        if user_input == 1:
            print("Для обработки выбран JSON-файл.")
            transactions = read_operations_from_json(path)
        elif user_input == 2:
            print("Для обработки выбран CSV-файл.")
            transactions = get_data_from_csv(path)
        elif user_input == 3:
            print("Для обработки выбран XLSX-файл.")
            transactions = get_data_from_excel(path)
        else:
            print("Неверный выбор. Завершение программы.")
            return
    except ValueError:
        print("Ошибка: введите число от 1 до 3.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        user_input_2 = input().strip().upper()
        valid_statuses = ("EXECUTED", "CANCELED", "PENDING")
        if user_input_2 in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{user_input_2}"')
            filtered_transactions = filter_by_state(transactions, user_input_2)
            break
        else:
            print(f"Статус операции {user_input_2} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")
    is_sorted_by_date = input().strip().lower()

    if is_sorted_by_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sort_order = input().strip().lower()
        if sort_order == "по возрастанию":
            filtered_transactions = sort_by_date(filtered_transactions, descending=False)
        else:
            filtered_transactions = sort_by_date(filtered_transactions)

    print("Выводить только рублевые транзакции? Да/Нет")
    is_only_rubles = input().strip().lower()

    if is_only_rubles == "да":
        rub_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
        filtered_transactions = rub_transactions

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    is_sorted_by_word = input().strip().lower()

    if is_sorted_by_word == "да":
        print("Введите слово для поиска в описании:")
        search_word = input().strip()
        try:
            filtered_transactions = process_bank_search(filtered_transactions, search_word)
        except Exception as e:
            print(f"Ошибка при поиске: {e}")

    print("Распечатываю итоговый список транзакций...")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")

    for transaction in filtered_transactions:
        try:
            date = get_date(transaction.get("date", ""))
            description = transaction.get("description", "")
            from_account = mask_account_card(transaction.get("from", ""))
            to_account = mask_account_card(transaction.get("to", ""))
            amount = transaction["operationAmount"].get("amount", 0)
            currency = transaction["operationAmount"]["currency"].get("name", "")

            print(f"{date} {description}")
            if from_account:
                print(f"{from_account} -> {to_account}")
            else:
                print(f"{to_account}")
            print(f"Сумма: {amount} {currency}\n")

        except Exception as e:
            print(f"Ошибка при выводе транзакции: {e}")
            continue
