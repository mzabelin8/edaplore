from separator.define_data_type import is_series


def get_value_counts(data):
    """

    :param data:
    :return: pd series
    """
    if not is_series(data):
        return None
    return data.value_counts()