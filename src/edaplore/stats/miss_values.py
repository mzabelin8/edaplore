from src.edaplore.separator.define_data_type import is_series


def count_miss_vals(data):
    if not is_series(data):
        return 0
    return data.isna().sum()
