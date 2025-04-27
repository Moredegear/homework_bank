from src.masks import get_mask_card_number
from src.masks import get_mask_account
card = 1234123412341234
account = 12344567789434485836456
print(get_mask_card_number(card))
print(get_mask_account(account))