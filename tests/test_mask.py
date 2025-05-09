from src.masks import get_mask_card_number
from src.masks import get_mask_account
import pytest


@pytest.mark.parametrize("x,expected",[("7000792289606361","7000 79** **** 6361"),
                                       (0,"Вы ввели недостаточно символов"),
                                       ("12345678901234567","Вы ввели слишком много символов"),
                                       ("","Номер карты не введен")])
def test_get_mask_card_number(x,expected):
    assert get_mask_card_number(x) == expected

@pytest.mark.parametrize("x,expected",[("73654108430135874305","**4305"),
                                       (0,"Вы ввели недостаточно символов"),
                                       ("1234567890123456789012","Вы ввели слишком много символов"),
                                       ("","Номер счета не введен")])
def test_get_mask_account(x,expected):
    assert get_mask_account(x) == expected