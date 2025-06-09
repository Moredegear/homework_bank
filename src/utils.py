import json
from src.external_api import conversion
import os


def get_list_of_transactions(file_path: str) -> list:
    """функция возвращающая список транзакций принимая путь к json_файлу"""
    transactions = []
    if os.path.isfile(file_path):
        if os.stat(file_path).st_size != 0:
            with open(file_path) as json_file:
                data = json.load(json_file)
                for transaction in data:
                    transactions.append(transaction)
    return transactions


def get_transaction_amount(transaction: dict) -> float:
    """функция принимающая транзакцию и выдающая сумму операции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        result = conversion(
            transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
        )
    else:
        result = transaction["amount"]
    return result
