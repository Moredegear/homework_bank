import json
from src.external_api import conversion
import os
import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_list_of_transactions(file_path: str) -> list:
    """функция возвращающая список транзакций принимая путь к json_файлу"""
    transactions = []
    logger.debug("приняли путь к файлу")
    if os.path.isfile(file_path):
        logger.debug("проверяем наличие файла")
        if os.stat(file_path).st_size != 0:
            logger.debug("проверяем наличие содерживого в файле")
            with open(file_path) as json_file:
                data = json.load(json_file)
                for transaction in data:
                    transactions.append(transaction)
            logger.debug("извлекаем список транзакций из jsonfile и возвращаем результат")
        else:
            logger.warning("файл пустой возвращаем пустой список")
    else:
        logger.warning("файл не найден возвращаем пустой список")
    return transactions


def get_transaction_amount(transaction: dict) -> float:
    """функция принимающая транзакцию и выдающая сумму операции в рублях"""
    logger.debug("проверяем в какой валюте была произведена транзакция")
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        logger.debug("конвертируем валюты в рубли с помощью функции conversion, передаем ей сумму и сод валюты")
        result = conversion(
            transaction["operationAmount"]["amount"], transaction["operationAmount"]["currency"]["code"]
        )
    else:
        logger.debug("валюта - RUB поэтому просто выводим сумму")
        result = transaction["amount"]
    return result
