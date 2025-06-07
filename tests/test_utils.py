from unittest.mock import patch
from src.utils import get_transaction_amount
from src.utils import get_list_of_transactions

transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
}


def test_get_list_of_transactions():
    trans = get_list_of_transactions("/Users/ulialevina/PycharmProjects/homework/tests/operations.json")
    assert trans == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    trans = get_list_of_transactions("/Users/ulialevina/PycharmProjects/homework/tests/zero")
    assert trans == []
    trans = get_list_of_transactions("/Users/ulialevina/PycharmProjects/homework/tests/operations_ziro.json")
    assert trans == []


@patch("requests.get")
def test_get_transaction_amount(mock_get):
    mock_get.return_value.json.return_value = 5
    assert get_transaction_amount(transaction) == 5
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "rDFLjzn0mZaqeV8ZcFX02iCGLIHZHgMv"},
        params={"amount": "amount", "from": "RUB", "to": "USD"},
    )
