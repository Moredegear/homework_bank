import re
from collections import defaultdict, Counter
import collections


def search_string(transaction, string):
    """функция сортировки по описанию транзакции"""
    result = []
    if len(string) == 0:
        return result
    for i in transaction:
        if re.search(string, i["description"], flags=re.IGNORECASE):
            result.append(i)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """функция подсчета описаний транзакций"""
    result_list = []
    if len(categories) == 0:
         return []
    for transaction in data:
        for category in categories:
            if re.search(category, transaction["description"]):
                result_list.append(transaction['description'])
                result = Counter(result_list)
    return result
