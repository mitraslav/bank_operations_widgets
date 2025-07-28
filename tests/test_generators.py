import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == transactions[0]
    assert next(usd_transactions) == transactions[1]
    assert next(usd_transactions) == transactions[3]
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_filter_by_currency_rub(transactions):
    rub_transactions = filter_by_currency(transactions, "RUB")
    assert next(rub_transactions) == transactions[2]
    assert next(rub_transactions) == transactions[4]
    with pytest.raises(StopIteration):
        next(rub_transactions)


def test_filter_by_currency_empty_list():
    empty_transactions = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(empty_transactions)


def test_filter_by_currency_no_matching(transactions):
    eur_transactions = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(eur_transactions)
