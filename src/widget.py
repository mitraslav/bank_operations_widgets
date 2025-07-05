from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """Функция маскирует счета и карты пользователя"""
    user_data_list = user_data.split()
    numbers_from_data = int(user_data_list[-1])
    if "Счет" in user_data_list:
        masked_account = get_mask_account(numbers_from_data)
        return "Счет " + masked_account
    card_name = ' '.join(user_data_list[:-1])
    masked_card = get_mask_card_number(numbers_from_data)
    return f'{card_name} {masked_card}'


def get_date(date_info: str) -> str:
    """Функция возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    day = date_info[8:10]
    month = date_info[5:7]
    year = date_info[:4]
    return f"{day}.{month}.{year}"
