from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        curr = op_amount.get("currency", {}).get("code")
        if curr == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict[Any, Any]]) -> Generator:
    """Возвращает описания банковских операций, поданных на вход"""
    for transaction in transactions:
        yield transaction.get("description", "У операции отсутствует описание!")


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Generator:
    """Генерирует номера карт в заданном диапазоне"""
    if start > 9999999999999999 or end > 9999999999999999:
        raise ValueError("Число не должно превышать 16 цифр!")
    if start < 0 or end < 0:
        raise ValueError("Число должно быть положительным!")
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        formatted_number = " ".join(card_number[i : i + 4] for i in range(0, 16, 4))
        yield formatted_number
