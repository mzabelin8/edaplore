import pandas as pd
from types_clases import names


def is_data_frame(data):
    """
    is data pd.dataframe

    :param data:
    :return: bool
    """
    return type(data) == pd.core.frame.DataFrame


def is_series(data):
    """
    is object pandas series (column)

    :param data: object
    :return: bool
    """
    return type(data) == pd.core.series.Series


def is_categorical_type(data):
    col_type = data.dtypes
    return col_type in names.categorical_type


def is_numeric_type(data):
    col_type = data.dtypes
    return col_type in names.numeric_types


def is_bool_type(data):
    res = True
    if data.dtypes in names.bool_type:
        return res
    if is_numeric_type(data):
        set_vals = set(data)
        if len(set_vals) != 2:
            res = False
        else:
            for el in set_vals:
                if el not in {0, 1}:
                    res = False
                    break

    return res


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





