from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats

import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO

class Numeric(Type):
    def make_plot(self):
        plt.figure(figsize=(10, 6))
        sns.displot(self.data)
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        return base64.b64encode(img.read()).decode('utf-8')

    def __init__(self, data, column_name):
        super().__init__(data, column_name)

        self.type_name = names.numeric

        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)
        self.dublicates = numeric_stats.count_dublicates(data)

        self.max = numeric_stats.count_max(data)
        self.min = numeric_stats.count_min(data)
        self.mean = numeric_stats.count_mean(data)
        self.std = numeric_stats.count_std(data)

        self.dist_plot = self.make_plot()
