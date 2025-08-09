import logging
import os

os.makedirs('logs', exist_ok=True)

masks_logger = logging.getLogger('app.masks')
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join('logs', 'masks.log'), 'w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает номер карты и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    card_number_str = str(card_number)

    if not card_number_str.isdigit():
        masks_logger.error("Произошла ошибка: номер карты должен содержать только цифры!")
        raise ValueError("Номер карты должен содержать только цифры")
    if len(card_number_str) != 16:
        masks_logger.error("Произошла ошибка: номер карты должен содержать 16 цифр!")
        raise ValueError("Номер карты должен содержать 16 цифр")
    masked_card_number =  f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    masks_logger.info(f'Успешно выведена маска карты: {masked_card_number}')
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """Функция принимает номер счета и возвращает маску номера по правилу **XXXX"""
    account_number_str = str(account_number)
    masked_account = f"**{account_number_str[-4:]}"
    masks_logger.info(f'Успешно выведена маска счета: {masked_account}')
    return masked_account
