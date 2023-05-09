from separator import define_data_type
from types_clases import type_categorical
from types_clases import type_boolean
from types_clases import type_numeric


class Separator:
    def __init__(self, data):
        if define_data_type.is_data_frame(data):
            self.data = data
            self.col_names = list(data.columns)

            self.numeric = {}
            self.boolean = {}
            self.categorical = {}
            # self.date_or_time = {}

    def separate(self):
        for col in self.col_names:
            if define_data_type.is_numeric_type(self.data[col]):
                C = type_numeric.Numeric(self.data[col], col)
                self.numeric[col] = C
            if define_data_type.is_bool_type(self.data[col]):
                C = type_boolean.Boolean(self.data[col], col)
                self.numeric[col] = C
            if define_data_type.is_categorical_type(self.data[col]):
                C = type_categorical.Categorical(self.data[col], col)
                self.numeric[col] = C
