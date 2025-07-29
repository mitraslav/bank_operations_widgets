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


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_empty_list():
    empty_transactions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(empty_transactions)


def test_transaction_descriptions_no_description(incomplete_transactions):
    no_descriptions = transaction_descriptions(incomplete_transactions)
    assert next(no_descriptions) == "У операции отсутствует описание!"
    assert next(no_descriptions) == "У операции отсутствует описание!"
    assert next(no_descriptions) == "У операции отсутствует описание!"
    assert next(no_descriptions) == "У операции отсутствует описание!"
    assert next(no_descriptions) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(no_descriptions)


def test_card_number_generator_limit_5():
    card_number = card_number_generator(1, 5)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(card_number)


def test_card_number_generator_formatting():
    generator = card_number_generator(1234567890123456, 1234567890123456)
    card_number = next(generator)
    assert card_number == "1234 5678 9012 3456"
    assert len(card_number.replace(" ", "")) == 16
    assert card_number.count(" ") == 3
    with pytest.raises(ValueError, match="Число не должно превышать 16 цифр!"):
        next(card_number_generator(10000000000000000, 10000000000000000))
    with pytest.raises(ValueError, match="Число должно быть положительным!"):
        next(card_number_generator(-1, -1))


def test_card_number_generator_boundaries():
    first = next(card_number_generator(0, 9999999999999999))
    assert first == "0000 0000 0000 0000"

    last = next(card_number_generator(9999999999999999, 9999999999999999))
    assert last == "9999 9999 9999 9999"
