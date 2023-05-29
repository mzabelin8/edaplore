import edaplore.separator.define_data_type


def count_miss_vals(data):
    if not edaplore.separator.define_data_type.is_series(data):
        return 0
    return data.isna().sum()
