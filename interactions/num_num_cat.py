from types_clases.type_boolean import *
from types_clases.type_numeric import *
from types_clases.type_categorical import *

from separator.combine import *

import images.make_plot as plot

from jinja2 import Environment, Template, FileSystemLoader


class Num2Cat:
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, num1, num2, cat1):
        self.plots = []
        self.name = f'{num1.column_name} vs {num2.column_name} vs {cat1.column_name}'
        comb = Combiner(x=num1, y=num2, hue=cat1)

        scat = plot.scatter_plot(comb)
        self.plots.append(scat)

        line = plot.line_plot(comb)
        self.plots.append(line)

        pair = plot.pair_plot(comb)
        self.plots.append(pair)

        joint = plot.joint_plot(comb)
        self.plots.append(joint)


        self.rendered = self.render()

