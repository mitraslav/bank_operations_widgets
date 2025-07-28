from typing import Any, Dict, List


def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        curr = op_amount.get("currency", {}).get("code")
        if curr == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    pass


def card_number_generator(start=1, end=9999999999999999) -> str:
    pass
