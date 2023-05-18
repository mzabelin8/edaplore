from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats, boolean_stats
from stats import categorical_stats
from images.make_plot import dis_plot


import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO

from jinja2 import Environment, Template, FileSystemLoader


class Categorical(Type):
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('categorical_template.html').render(cat=self)
        return template

    def count_categ_names_len(self):
        c = self.data.cat.categories
        res = 0
        for el in c:
            res += len(el)
        return res

    def make_plot(self):
        if self.names_length > 30:
            return None
        self.isPlot = True

        return dis_plot(self.data)

    def __init__(self, data, column_name):
        super().__init__(data, column_name)

        self.data = data.astype('category')
        self.type_name = names.categorical
        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)

        self.categories = categorical_stats.get_value_counts(data)
        self.count_categories = len(self.categories)

        self.isPlot = False
        self.names_length = self.count_categ_names_len()
        self.categ_names = list(self.categories.index)

        self.dist_plot = self.make_plot()
        self.rendered = self.render()

