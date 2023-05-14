from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats, boolean_stats
from stats import categorical_stats
from images.make_plot import MakePlot
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO

from jinja2 import Environment, Template, FileSystemLoader


class Boolean(Type):
    def render(self):
        path_to_template = '../html_templates/templates_for_typeclasses'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('boolean_template.html').render(boolean=self)
        return template

    def make_plot(self):
        M = MakePlot()
        return M.sns_count_plot(self.data)

    def __init__(self, data, column_name):
        super().__init__(data, column_name)

        self.type_name = names.bolean
        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)
        self.ratio = boolean_stats.count_ration(data)

        self.dist_plot = self.make_plot()
        self.rendered = self.render()
