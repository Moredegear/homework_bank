from src.widget import mask_account_card
from src.widget import get_date
import pytest


@pytest.mark.parametrize("x,expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("", "Время не введено")])
def test_get_date(x, expected):
    assert get_date(x) == expected


@pytest.mark.parametrize(
    "x,expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        (0, "Вы ввели недостаточно символов"),
        ("Visa Platinum 7000df54g", "Вы ввели неверные символы в номере карты или счета"),
        ("Visa Platinum 70007922896063612", "Вы ввели лишние символы в номере карты"),
        ("Счет 7365410843013587430556", "Вы ввели слишком много символов"),
        ("", "Вы не ввели данные карты или счета"),
    ],
)
def test_mask_account_card(x, expected):
    assert mask_account_card(x) == expected
