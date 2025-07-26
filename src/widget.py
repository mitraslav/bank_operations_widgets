from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """Функция маскирует счета и карты пользователя"""
    if not user_data.strip():
        return ""

    user_data_list = user_data.split()

    if not user_data_list:
        return ""

    if len(user_data_list) == 1 and user_data_list[0] == "Счет":
        return "Счет **"

    try:
        numbers_from_data = user_data_list[-1]

        if not numbers_from_data.isdigit():
            return user_data

        if "Счет" in user_data_list:
            if len(numbers_from_data) >= 4:
                masked_account = get_mask_account(int(numbers_from_data))
                return "Счет " + masked_account
            return "Счет **"

        if len(numbers_from_data) == 16:
            masked_card = get_mask_card_number(int(numbers_from_data))
            card_name = " ".join(user_data_list[:-1])
            return f"{card_name} {masked_card}"

        return user_data
    except (IndexError, ValueError):
        return user_data


def get_date(date_info: str) -> str:
    """Функция возвращает строку с датой в формате ДД.ММ.ГГГГ

    Args:
        date_info: Строка с датой в формате ГГГГ-ММ-ДДTHH:MM:SS или ГГГГ-ММ-ДД

    Returns:
        Строка с датой в формате ДД.ММ.ГГГГ или пустую строку при ошибке
    """
    if not date_info:
        return ""

    # Разделяем дату и время (если есть)
    parts = date_info.split("T")
    date_part = parts[0]

    # Проверяем базовый формат даты
    if len(date_part) != 10 or date_part[4] != "-" or date_part[7] != "-":
        return ""

    # Если есть часть с временем, проверяем её формат
    if len(parts) > 1:
        time_part = parts[1]
        if len(time_part.split(":")) != 3:
            return ""

    # Специальная обработка для года 0000
    if date_part.startswith("0000-"):
        day = date_part[8:10]
        month = date_part[5:7]
        year = date_part[:4]
        return f"{day}.{month}.{year}"

    try:
        # Пробуем распарсить всю дату с временем (если есть)
        datetime.strptime(date_info, "%Y-%m-%dT%H:%M:%S" if "T" in date_info else "%Y-%m-%d")
        day = date_part[8:10]
        month = date_part[5:7]
        year = date_part[:4]
        return f"{day}.{month}.{year}"
    except ValueError:
        return ""
