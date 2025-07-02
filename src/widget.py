from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
 """Функция маскирует счета и карты пользователя"""
    if "Счет" in user_data:
        return get_mask_account(int(user_data[user_data.find(" ") + 1 :]))
    return get_mask_card_number(int(user_data[user_data.find(" ") + 1 :]))


def get_date(date_info: str) -> str:
 """Функция возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return f"{date_info[8:10]}.{date_info[5:7]}.{date_info[:4]}"
