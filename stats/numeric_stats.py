from separator.define_data_type import is_series


def count_max(data):
    if not is_series(data):
        return 0
    return data.max()


def count_min(data):
    if not is_series(data):
        return 0
    return data.min()


def count_mean(data):
    if not is_series(data):
        return 0
    return data.mean()


def count_std(data):
    if not is_series(data):
        return 0
    return data.std()


def count_duplicates(data):
    if not is_series(data):
        return 0
    return data.duplicated().sum()
