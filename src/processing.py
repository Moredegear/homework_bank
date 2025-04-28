def filter_by_state(data_list: list, state: str ="EXECUTED" ) -> list:
    """функция фильтрования данных по их состоянию"""
    result = []
    for d in data_list:
        if d["state"] == state:
            result.append(d)
        else:
            continue
    return result

