from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator
import pytest


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


@pytest.fixture
def currency():
    return transactions


def test_filter_by_currency_2(currency):
    result = []
    data = filter_by_currency(currency)
    for _ in range(2):
        result.append(next(data))
    assert result == [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
     {
     "id": 142264268,
     "state": "EXECUTED",
     "date": "2019-04-04T23:20:05.206878",
     "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
     "description": "Перевод со счета на счет",
     "from": "Счет 19708645243227258542",
     "to": "Счет 75651667383060284188",
    }]
    assert next(filter_by_currency(currency, currency="EUR")) == "Нет транзакций в заданной валюте"
    assert next(filter_by_currency([])) == "Нет вводных данных"
    assert next(filter_by_currency(currency, currency="RUB")) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


@pytest.mark.parametrize("x, expected", [(transactions, ["Перевод организации", "Перевод со счета на счет",
                                                         "Перевод со счета на счет"])])
def test_transaction_descriptions(x, expected):
    result = []
    descriptions = transaction_descriptions(x)
    for _ in range(3):
        result.append(next(descriptions))
    assert result == expected
    assert next(transaction_descriptions([])) == "Нет входных данных"


@pytest.mark.parametrize("x,y,expected", [(1, None, ["0000 0000 0000 0001"]), (7, None, ["0000 0000 0000 0007"]),
                                          (123456, 123458,
                                          ["0000 0000 0012 3456", "0000 0000 0012 3457", "0000 0000 0012 3458"])])
def test_card_number_generator(x, y, expected):
    assert next(card_number_generator(x, y)) == expected
