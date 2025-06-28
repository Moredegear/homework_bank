import pandas as pd
import csv
import os

from tests.test_utils import transaction


def reading_csv(filename):
    result_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        key = next(csv_reader)
        for row in csv_reader:
            for i in range(len(row)):
                transaction[key[i]] = row[i]
            result_list.append(transaction)
    return result_list


def reading_excel(filename):
     excel_data = pd.read_excel(filename)
     result_list = excel_data.to_dict('records')
     return result_list



re = reading_csv('/Users/ulialevina/Documents/transactions.csv')
for row in re:
    print(row)
    break


rt = reading_excel('/Users/ulialevina/Documents/transactions_excel.xlsx')
for row in rt:
    print(row)
    break