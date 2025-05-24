

def filter_by_currency(transaction_data: list, currency: str = "USD"):
    """фильтрует и выдает транзакции по заданной валюте"""
    if len(list) == 0:
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


def card_number_generator(begin: int, end: int = None):
    """Генерирует номера карт в заданном интервале"""
    if end is None:
        end = begin
    card_numbers = []
    result = []
    i = begin
    while i <= end:
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
