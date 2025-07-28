from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        curr = op_amount.get("currency", {}).get("code")
        if curr == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict[Any, Any]]) -> Generator:
    for transaction in transactions:
        yield transaction.get("description", "У операции отсутствует описание!")


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> str:
    pass
