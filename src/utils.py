import json
from src.external_api import conversion
import os


def get_list_of_transactions(file_path: str):
    transactions = []
    if os.path.isfile(file_path):
        if os.stat(file_path).st_size != 0:
            with open(file_path) as json_file:
                data = json.load(json_file)
                for transaction in data:
                    transactions.append(transaction)
    return transactions


trans = get_list_of_transactions("/Users/ulialevina/PycharmProjects/homework/tests/operations.json")
print(trans)


def get_transaction_amount(transaction):
    result = None
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        result = conversion(
            transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
        )
    else:
        result = transaction["amount"]
    return result
