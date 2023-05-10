from separator import define_data_type
import types_clases.names as names

class Overview:
    def __init__(self, data):
        self.count_columns = len(data)
        self.count_rows = data[0].count_values

        self.miss_vals = 0
        self.count_numeric = 0
        self.count_boolean = 0
        self.count_categorical = 0
        for el in data:
            self.miss_vals += el.miss_values

            if names.numeric == el.type_name:
                self.count_numeric += 1

            if names.bolean == el.type_name:
                self.count_boolean += 1

            if names.categorical == el.type_name:
                self.count_categorical += 1

