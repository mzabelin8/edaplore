from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats
from images.make_plot import dis_plot, count_plot
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO

from jinja2 import Environment, Template, FileSystemLoader


class Numeric(Type):
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('numeric_template.html').render(num=self)
        return template

    def __init__(self, data, column_name):
        super().__init__(data, column_name)

        self.type_name = names.numeric

        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)
        self.duplicates = numeric_stats.count_duplicates(data)

        self.max = numeric_stats.count_max(data)
        self.min = numeric_stats.count_min(data)
        self.mean = round(numeric_stats.count_mean(data), 3)
        self.std = round(numeric_stats.count_std(data), 3)

        self.dist_plot = dis_plot(self.data)
        self.rendered = self.render()
