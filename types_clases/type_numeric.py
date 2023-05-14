from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats
from images.make_plot import MakePlot
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO

from jinja2 import Environment, Template, FileSystemLoader


class Numeric(Type):
    def render(self):
        path_to_template = '../html_templates/templates_for_typeclasses'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('numeric_template.html').render(num=self)
        return template

    def make_plot(self):
        M = MakePlot()
        return M.sns_dis_plot(self.data)

    def __init__(self, data, column_name):
        super().__init__(data, column_name)

        self.type_name = names.numeric

        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)
        self.duplicates = numeric_stats.count_duplicates(data)

        self.max = numeric_stats.count_max(data)
        self.min = numeric_stats.count_min(data)
        self.mean = numeric_stats.count_mean(data)
        self.std = numeric_stats.count_std(data)

        self.dist_plot = self.make_plot()
        self.rendered = self.render()
