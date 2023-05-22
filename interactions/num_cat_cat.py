from types_clases.type_boolean import *
from types_clases.type_numeric import *
from types_clases.type_categorical import *

from separator.combine import *

import images.make_plot as plot

from jinja2 import Environment, Template, FileSystemLoader


class NumCat2:
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, num1, cat1, cat2):
        self.plots = []
        self.name = f'{num1.column_name} vs {cat1.column_name} vs {cat2.column_name}'
        comb = Combiner(x=cat1, y=num1, hue=cat2)

        bar = plot.bar_plot(comb)
        self.plots.append(bar)

        violin = plot.violin_plot(comb)
        self.plots.append(violin)

        heatmap = plot.heat_map(comb)
        self.plots.append(heatmap)

        self.rendered = self.render()
