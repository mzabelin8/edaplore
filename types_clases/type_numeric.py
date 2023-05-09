from type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats


class Numeric(Type):
    def __init__(self, data, column_name):
        self.column_name = column_name
        self.type_name = names.numeric

        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)
        self.dublicates = numeric_stats.count_dublicates(data)

        self.max = numeric_stats.count_max(data)
        self.min = numeric_stats.count_min(data)
        self.mean = numeric_stats.count_mean(data)
        self.std = numeric_stats.count_std(data)
