import json
from src.external_api import conversion

def get_list_of_transactions(file_path):
    transactions = []
    with open(file_path) as json_file:
        data = json.load(json_file)
        for transaction in data:
            transactions.append(transaction)
    return transactions

trans = get_list_of_transactions('/Users/ulialevina/PycharmProjects/homework/data/operations.json')
print(trans)

def get_transaction_amount(transaction):
    result = None
    for i in transaction:
        if i["currency"]["cod"] != "RUB":
            result = conversion(i["amount"], i["currency"]["cod"])
        else:
            result = i["amount"]
    return result

