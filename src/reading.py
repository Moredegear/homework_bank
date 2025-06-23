import pandas as pd
import csv
import os

def reading_csv(filename):
    result_list = []
    if filename.endswith(".csv"):
        if os.path.isfile(filename):
            if os.stat(filename).st_size == 0:
                with open(filename) as file:
                    reader = csv.reader(file)
                    for row in reader:
                       result_list.append(row)
    return result_list


def reading_excel(filename):
    result_list = []
    if filename.endswith(".csv"):
        if os.path.isfile(filename):
            if os.stat(filename).st_size == 0:
                excel_data = pd.read_excel(filename)
                for row in excel_data:
                    result_list.append(row)
    return result_list
