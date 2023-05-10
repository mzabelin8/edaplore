from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats, boolean_stats
from stats import categorical_stats

class Categorical(Type):
    def __init__(self, data, column_name):
        self.column_name = column_name
        self.type_name = names.categorical
        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)

        self.categ_size = categorical_stats.get_value_counts(data)
        self.count_categories = len(self.categ_size)

