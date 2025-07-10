from unittest.mock import patch, mock_open
from src.reading import reading_csv, reading_excel
import pandas as pd


@patch("builtins.open", new_callable=mock_open)
@patch("csv.DictReader")
def test_get_csv_data(mock_csv_DictReader, mock_file):
    mock_csv_data = [
        ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
        ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'Sol', 'PEN',
         'Счет 58803664561298323391', 'Счет 39745660563456619397', 'Перевод организации'],
        ['3598919', 'EXECUTED', '2020-12-06T23:00:58Z', '29740', 'Peso', 'COP',
         'Discover 3172601889670065', 'Discover 0720428384694643', 'Перевод с карты на карту'],
        ['593027', 'CANCELED', '2023-07-22T05:02:01Z', '30368', 'Shilling', 'TZS',
         'Visa 1959232722494097', 'Visa 6804119550473710', 'Перевод с карты на карту']
    ]

    mock_csv_DictReader.return_value = iter(mock_csv_data)

    with patch.dict('tests.test_utils.transaction', clear=True):
        result = reading_csv('dummy.csv')

        assert result == [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": "3598919",
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": "29740",
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
            {
                "id": "593027",
                "state": "CANCELED",
                "date": "2023-07-22T05:02:01Z",
                "amount": "30368",
                "currency_name": "Shilling",
                "currency_code": "TZS",
                "from": "Visa 1959232722494097",
                "to": "Visa 6804119550473710",
                "description": "Перевод с карты на карту",
            },
        ]

        mock_file.assert_called_once_with('dummy.csv', 'r', encoding='utf-8')


def test_reading_excel():
    test_data = [{
        'id': 650703.0,
        'state': 'EXECUTED',
        'date': '2023-09-05T11:30:32Z',
        'amount': 16210.0,
        'currency_name': 'Sol',
        'currency_code': 'PEN',
        'from': 'Счет 58803664561298323391',
        'to': 'Счет 39745660563456619397',
        'description': 'Перевод организации'
    }]

    mock_df = pd.DataFrame(test_data)

    with patch('pandas.read_excel', return_value=mock_df):
        result = reading_excel('dummy.xlsx')

        assert result == test_data
