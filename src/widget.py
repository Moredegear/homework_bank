from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(card: str) -> str:
    """функция редактирования данных карты или счета"""
    card = str(card)
    card_list = card.split(" ")
    result_list = []
    for i in card_list:
        if i.isdigit():
            if len(i) == 12:
                i = get_mask_card_number(i)
                result_list.append(i)
            else:
                i = get_mask_account(i)
                result_list.append(i)
        else:
            result_list.append(i)
    result = " ".join(result_list)
    return result


def get_date(date: str) -> str:
    """функция редактирования даты"""
    result_list = []
    for i in range(len(date)):
        if date[i] != "T":
            result_list.append(date[i])
        else:
            break
    result_strinr = "".join(result_list)
    result_list = result_strinr.split("-")
    reversed_result_list = result_list[::-1]
    result = ".".join(reversed_result_list)
    return result
