def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(card_number: int) -> str:
    """Функция принимает номер карты и возвращает маску номера по правилу **XXXX"""
    card_number_str = str(card_number)
    return f"**{card_number_str[-4:]}"
