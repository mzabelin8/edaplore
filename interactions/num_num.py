from types_clases.type_boolean import *
from types_clases.type_numeric import *
from types_clases.type_categorical import *

from separator.combine import *

import images.make_plot as plot

from jinja2 import Environment, Template, FileSystemLoader


class NumNum:
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, num1, num2):
        self.plots = []
        self.name = f'{num1.column_name} vs {num2.column_name}'
        comb = Combiner(x=num1, y=num2)

        line_plot = plot.line_plot(comb)
        self.plots.append(line_plot)

        joint_plot = plot.joint_plot(comb)
        self.plots.append(joint_plot)

        kde_plot = plot.kde_plot(comb)
        self.plots.append(kde_plot)

        self.rendered = self.render()
