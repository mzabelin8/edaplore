from types_clases.type_boolean import *
from types_clases.type_numeric import *
from types_clases.type_categorical import *

from separator.combine import *

import images.make_plot as plot

from jinja2 import Environment, Template, FileSystemLoader


class CatCat:
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, cat1, cat2):
        self.plots = []
        self.name = f'{cat1.column_name} vs {cat2.column_name}'
        comb = Combiner(x=cat1, hue=cat2)

        count_plt = plot.count_plot_combiner(comb)
        self.plots.append(count_plt)

        self.rendered = self.render()

