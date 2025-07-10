import pandas as pd
import csv
import os

def reading_csv(filename):
    result_list = []
    if os.path.isfile(filename):
        if os.stat(filename).st_size != 0:
            with open(filename) as csv_file:
                reader = csv.DictReader(csv_file, delimiter=';')
                result_list = list(reader)
        else:
            result_list = 1
    else:
        result_list = None

    return result_list


def reading_excel(filename):
    if os.path.isfile(filename):
        if os.stat(filename).st_size != 0:
            excel_data = pd.read_excel(filename)
            result_list = excel_data.to_dict('records')
        else:
            result_list = 1
    else:
        result_list = None
    return result_list



re = reading_csv('/Users/ulialevina/PycharmProjects/homework/data/transactions.csv')


rt = reading_excel('/Users/ulialevina/PycharmProjects/homework/data/transactions_excel.xlsx')