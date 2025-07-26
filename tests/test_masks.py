import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234567812345678", "1234 56** **** 5678"),
    ],
)
def test_valid_card_numbers(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "1234",
        "",
        "123456789012345",  # 15 цифр
        "abcdefghijklmnop",  # буквы
    ],
)
def test_invalid_card_numbers(invalid_card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("12345678", "**5678"),  # Короткий номер
        ("12", "**12"),  # Очень короткий номер
        ("", "**"),  # Пустая строка
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
