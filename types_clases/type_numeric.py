from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats


# class Numeric(Type):
#     def __init__(self, data, column_name):
#         self.column_name = column_name
#         self.type_name = names.numeric
#
#         self.count_values = len(data)
#         self.miss_values = count_miss_vals(data)
#         self.dublicates = numeric_stats.count_dublicates(data)
#
#         self.max = numeric_stats.count_max(data)
#         self.min = numeric_stats.count_min(data)
#         self.mean = numeric_stats.count_mean(data)
#         self.std = numeric_stats.count_std(data)

import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO

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

        plt.figure(figsize=(10, 6))
        sns.displot(data)
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        self.dist_plot = base64.b64encode(img.read()).decode('utf-8')


