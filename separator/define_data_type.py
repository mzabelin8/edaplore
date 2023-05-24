import pandas as pd
from types_clases import names


def is_data_frame(data):
    """
    is data pd.dataframe

    :param data:
    :return: bool
    """
    return isinstance(data, pd.DataFrame)


def is_series(data):
    """
    is object pandas series (column)

    :param data: object
    :return: bool
    """
    return isinstance(data, pd.Series)


def is_categorical_type(data):
    return pd.api.types.is_categorical_dtype(data.dtype)


def is_numeric_type(data):
    if pd.api.types.is_numeric_dtype(data.dtype):
        if set(data.unique()).issubset({0, 1}):
            return False
        return True
    return False


def is_bool_type(data):
    if pd.api.types.is_bool_dtype(data.dtype):
        return True
    if pd.api.types.is_numeric_dtype(data.dtype):
        if set(data.unique()).issubset({0, 1}):
            return True
    return False


def define_type_of_series(data):
    """
    return type (in my classification) of column
    :param data: object
    :return: string or None(if not series)
    """
    if not is_series(data):
        return None

    if is_categorical_type(data):
        return names.categorical

    if is_numeric_type(data):
        return names.numeric

    if is_bool_type(data):
        return names.bolean
