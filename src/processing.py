from typing import Union

def filter_by_state(data_list: list, state: str = "EXECUTED") -> Union[list, str]:
    """функция фильтрования данных по их состоянию"""
    if data_list == []:
        return "Список пусой"
    for i in data_list:
        if "state" in i:
            continue
        else:
            return "В списке нет ключа 'state'"
    result = []
    for d in data_list:
        if d["state"] == state:
            result.append(d)
        else:
            continue
    return result


def sort_by_date(data_list: list, reverse: bool = True) -> list:
    """функция сорировки данных по дате"""
    for i in data_list:
        if 'date' in i:
            continue
        else:
            return "В списке не указаны даты"
    sorted_data_list = sorted(data_list, key=lambda d: d["date"], reverse=reverse)
    return sorted_data_list
