from separator.define_data_type import is_series


def count_ration(data):
    if not is_series(data) or len(data) == 0:
        return 0
    return int(data.sum()) / int(len(data))
