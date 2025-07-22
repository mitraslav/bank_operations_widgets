def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    card_number_str = str(card_number)

    if not card_number_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    if len(card_number_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"



def get_mask_account(account_number: int) -> str:
    """Функция принимает номер карты и возвращает маску номера по правилу **XXXX"""
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"
