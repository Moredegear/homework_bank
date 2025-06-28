from unittest.mock import patch
from src.reading import reading_csv
from src.reading import reading_excel
import os


@patch('csv.reader')
def test_reading_csv(mock_get):
    mock_get.return_value.csv.return_value = [{'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'USD'}}, 'amount': '23423', 'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165', 'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}]
    assert reading_csv('/Users/ulialevina/Documents/transactions.csv') ==[{'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'USD'}}, 'amount': '23423', 'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165', 'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}]
    mock_get.assert_called_once_with()


@patch('pandas.read_excel')
def test_reading_excel(mock_get):
    mock_get.return_value.pandas.return_volue = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}]
    assert reading_excel('/Users/ulialevina/Documents/transactions_excel.xlsx') == {'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}
    mock_get.assert_called_once_with()

