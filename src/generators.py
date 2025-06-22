

def filter_by_currency(transaction_data: list, currency: str = "USD"):
    """фильтрует и выдает транзакции по заданной валюте"""
    if len(transaction_data) == 0:
        yield "Нет вводных данных"
    counter = 0
    for i in transaction_data:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i
        else:
            counter += 1
            if counter == len(transaction_data):
                yield "Нет транзакций в заданной валюте"
            continue


def transaction_descriptions(transaction_data: list):
    """возвращает описание операций"""
    if len(transaction_data) == 0:
        yield "Нет входных данных"
    for i in transaction_data:
        yield i["description"]


def card_number_generator(start: int, stop: int = None):
    """Генерирует номера карт в заданном интервале"""
    if stop is None:
        stop = start
    card_numbers = []
    result = []
    i = start
    while i <= stop:
        i = str(i)
        while len(i) + len(card_numbers) != 16:
            card_numbers.append("0")
        for a in i:
            card_numbers.append(a)
        card_numbers.insert(4, " ")
        card_numbers.insert(9, " ")
        card_numbers.insert(14, " ")

        result.append(''.join(card_numbers))
        card_numbers = []
        i = int(i) + 1
    yield result

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
descriptions = transaction_descriptions(transactions)
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))
