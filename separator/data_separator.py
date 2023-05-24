from separator import define_data_type
from types_clases import type_categorical
from types_clases import type_boolean
from types_clases import type_numeric


class Separator:
    def fill_mis_values(self):
        self.data.fillna(self.data.mean(), inplace=True)
        self.data.fillna('missing', inplace=True)

    def drop_outlier(self):
        pass

    def __init__(self, data, fill_mis=False):
        if define_data_type.is_data_frame(data):
            self.data = data
            if fill_mis:
                self.fill_mis_values()

            self.col_names = list(data.columns)

            self.numeric = {}
            self.boolean = {}
            self.categorical = {}

            self.data_classes = []

            self.separate()

            self.numeric_list = list(self.numeric.values())
            self.categorical_list = list(self.categorical.values())
            self.boolean_list = list(self.boolean.values())

    def separate(self):
        for col in self.col_names:
            if define_data_type.is_bool_type(self.data[col]):
                C = type_boolean.Boolean(self.data[col], col)
                self.boolean[col] = C
                self.data_classes.append(C)
                continue

            if define_data_type.is_numeric_type(self.data[col]):
                C = type_numeric.Numeric(self.data[col], col)
                self.numeric[col] = C
                self.data_classes.append(C)
                continue

            if define_data_type.is_categorical_type(self.data[col]):
                C = type_categorical.Categorical(self.data[col], col)
                self.categorical[col] = C
                self.data_classes.append(C)
                continue
