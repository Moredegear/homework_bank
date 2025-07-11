from src.processing import filter_by_state
from src.processing import sort_by_date
from src.search import search_string
from src.generators import filter_by_currency
from src.utils import get_list_of_transactions
from src.reading import reading_csv
from src.reading import reading_excel
from src.widget import get_date
from src.widget import mask_account_card


def main() -> None:
    """функция основной логики проекта общение с пользователем"""
    while True:
        data = None
        answer = input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
                   Выберите необходимый пункт меню:
                   1. Получить информацию о транзакциях из JSON-файла
                   2. Получить информацию о транзакциях из CSV-файла
                   3. Получить информацию о транзакциях из XLSX-файла\n""")
        if str(answer) == "1":
            print("Для обработки выбран JSON-файл.")
            data = get_list_of_transactions('/Users/ulialevina/PycharmProjects/homework/data/operations.json')
            break
        elif str(answer) == "2":
            print("Для обработки выбран CSV-файл.")
            data = reading_csv("/Users/ulialevina/PycharmProjects/homework/data/transactions.csv")
            break
        elif str(answer) == "3":
            print("Для обработки выбран XLSX-файл.")
            data = reading_excel("Users/ulialevina/PycharmProjects/homework/data/transactions_excel.xlsx")
            break
        else:
            print("данная обработка не доступна")
            continue
    while True:
        if data is None or data == 1 or len(data) == 0:
            break
        answer = input("""Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")
        if str(answer).upper() == "EXECUTED":
            print(" Операции отфильтрованы по статусу 'EXECUTED'")
            data_status = filter_by_state(data, "EXECUTED")
            break
        elif str(answer).upper() == "CANCELED":
            print(" Операции отфильтрованы по статусу 'CANCELED'")
            data_status = filter_by_state(data, "CANCELED")
            break
        elif str(answer).upper() == "PENDING":
            print(" Операции отфильтрованы по статусу 'PENDING'")
            data_status = filter_by_state(data, "PENDING")
            break
        else:
            print(f" Статус операции {answer} недоступен.")
            continue
    while True:
        if data is None or data == 1 or len(data_status) == 0:
            break
        answer = input("""Отсортировать операции по дате? Да/Нет\n""")
        if str(answer).lower() == "да":
            answer = input("""Отсортировать по возрастанию или по убыванию?\n""")
            if str(answer).lower() == "по убыванию":
                data_time = sort_by_date(data_status)
                break
            elif str(answer).lower() == "по возрастанию":
                data_time = sort_by_date(data_status, reverse=False)
                break
            else:
                print("Данная сортировка не найдена")
                continue
        elif str(answer).lower() == "нет":
            data_time = data_status
            break
        else:
            print("Данная сортировка не найдена")
            continue
    while True:
        if data is None or data == 1 or len(data_time) == 0:
            break
        answer = input("""хотите отсортировать транзакции по валютам?Да/Нет\n""")
        if str(answer).lower() == "да":
            answer = input("""Транзакции в каких валютах вы хотите вывести?\n""")
            answer = answer.upper()
            answer_list = answer.split()
            data_currency = []
            for currency in answer_list:
                iter_currency = filter_by_currency(data_time, currency)
            for currency in iter_currency:
                data_currency.append(currency)
            break
        elif str(answer).lower() == "нет":
            data_currency = data_time
            break
        else:
            print("Данная сортировка не найдена")
            continue
    while True:
        if data is None or data == 1 or len(data_currency) == 0:
            break
        answer = input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n""")
        if str(answer).lower() == "да":
            answer = input("по какoму слову в описании фильтруем?")
            result = search_string(data_currency, answer)
            break
        elif str(answer).lower() == "нет":
            result = data_currency
            break
        else:
            print("не понял")
            continue
    if data is None:
        print("указан неправильный путь")
    elif data == 1:
        print('файл пуст')
    elif len(result) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(result)}')
        for i in result:
            if 'currency_code' in i:
                if i['from'] == '':
                    print(f'''{get_date(i['date'])} {i["description"]}
                {mask_account_card(i['to'])}
                Сумма: {i['amount']} {i['currency_code']}.''')
                else:
                    print(f'''{get_date(i['date'])} {i['description']}
                {mask_account_card(i['from'])} -> {mask_account_card(i['to'])}
                Сумма: {i['amount']} {i['currency_code']}.''')
            else:
                if i['from'] == '':
                    print(f'''{get_date(i['date'])} {i["description"]}
                {mask_account_card(i['to'])}
                Сумма: {i['operationAmount']['amount']} {i['operationAmount']['amount']['currency_code']}.''')
                else:
                    print(f'''{get_date(i['date'])} {i['description']}
                {mask_account_card(i['from'])} -> {mask_account_card(i['to'])}
                Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['code']}.''')


main()
