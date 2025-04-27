from typing import Union


def get_mask_card_number(number_card: Union[str, int]) -> Union[str]:
    """маскируем номер карты пользователя"""

    number_card = str(number_card)
    mask_card_number_list = []
    for i in range(len(number_card)):
        if i < 6 or i > 11:
            if i == 4 or i == 12:
                mask_card_number_list.append(" ")
            mask_card_number_list.append(number_card[i])
        else:
            if i == 8:
                mask_card_number_list.append(" ")
            mask_card_number_list.append("*")
    mask_card_number = "".join(mask_card_number_list)
    return mask_card_number


def get_mask_account(number_account: Union[str, int]) -> Union[str]:
    """Маскируем номер счета пользователя"""

    number_account = str(number_account)
    mask_account_list = []
    for i in range(len(number_account)):
        if i > len(number_account) - 5:
            mask_account_list.append(number_account[i])
        elif i > len(number_account) - 7:
            mask_account_list.append("*")
        else:
            continue
    mask_account = "".join(mask_account_list)
    return mask_account
