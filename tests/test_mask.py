from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import mask_account_card
from src.widget import get_date

date = "2024-03-11T02:26:18.671407"
card_1 = 1234123412341234
account_1 = 12344567789434485836456
card_2 = "Visa Platinum 7000792289606361"
account_2 = "Счет 73654108430135874305"
print(get_mask_card_number(card_1))
print(get_mask_account(account_1))
print(mask_account_card(account_2))
print(mask_account_card(card_2))
print(get_date(date))