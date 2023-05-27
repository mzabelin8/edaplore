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
from html_templates.template_loader import find_template


class Boolean(Type):
    def render(self):
        template = find_template('boolean_template.html').render(boolean=self)
        return template


    def __init__(self, data, column_name):
        super().__init__(data, column_name)

        self.type_name = names.bolean
        self.count_values = len(data)
        self.miss_values = count_miss_vals(data)
        self.ratio = boolean_stats.count_ration(data)
        self.count_categories = 2

        self.dist_plot = count_plot(self.data)
        self.rendered = self.render()
