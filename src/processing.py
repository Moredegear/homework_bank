def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """функция фильтрования данных по их состоянию"""
    result = []
    for d in data_list:
        if d["state"] == state:
            result.append(d)
        else:
            continue
    return result


def sort_by_date(data_list: list, reverse: bool = True) -> list:
    """функция сорировки данных по дате"""
    sorted_data_list = sorted(data_list, key=lambda d: d["date"], reverse=reverse)
    return sorted_data_list
