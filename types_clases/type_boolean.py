from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats, boolean_stats


class Boolean(Type):
    def __init__(self, data, column_name):
        super().__init__(data, column_name)

        self.type_name = names.bolean
        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)
        self.ratio = boolean_stats.count_ration(data)
