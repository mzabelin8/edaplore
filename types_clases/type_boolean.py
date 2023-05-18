from types_clases.type_father import Type
from types_clases import names
from stats.miss_values import count_miss_vals
from stats import numeric_stats, boolean_stats
from stats import categorical_stats
from images.make_plot import count_plot
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO

from jinja2 import Environment, Template, FileSystemLoader


class Boolean(Type):
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('boolean_template.html').render(boolean=self)
        return template

    def __init__(self, data, column_name):
        super().__init__(data, column_name)

        self.type_name = names.bolean
        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)
        self.ratio = boolean_stats.count_ration(data)

        self.dist_plot = count_plot(self.data)
        self.rendered = self.render()
