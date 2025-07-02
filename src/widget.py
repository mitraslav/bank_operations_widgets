from masks import get_mask_account, get_mask_card_number

def mask_account_card(user_data : str) -> str:
    if 'Счет' in user_data:
        return get_mask_account(int(user_data[user_data.find(' ')+1:]))
    return get_mask_card_number(int(user_data[user_data.find(' ')+1:]))

