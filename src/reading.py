import pandas as pd
import csv

def reading_csv(filename):
    result_list = []
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        result_list = list(reader)
    return result_list


def reading_excel(filename):
     excel_data = pd.read_excel(filename)
     result_list = excel_data.to_dict('records')
     return result_list



re = reading_csv('/Users/ulialevina/PycharmProjects/homework/data/transactions.csv')
for row in re:
    print(row)
    break


rt = reading_excel('/Users/ulialevina/PycharmProjects/homework/data/transactions_excel.xlsx')
for row in rt:
    print(row)
    break