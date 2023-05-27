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
        self.name = f'{num1.column_name}_{num2.column_name}'
        comb = Combiner(x=num1, y=num2)

        line_plot = plot.line_plot(comb)
        self.plots.append(line_plot)

        joint_plot = plot.joint_plot(comb)
        self.plots.append(joint_plot)

        kde_plot = plot.kde_plot(comb)
        self.plots.append(kde_plot)

        self.rendered = self.render()


class NumCat:
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, num1, cat1):
        self.plots = []
        self.name = f'{num1.column_name}_{cat1.column_name}'
        comb = Combiner(x=cat1, y=num1)

        bar_plot = plot.bar_plot(comb)
        self.plots.append(bar_plot)

        violin_plot = plot.violin_plot(comb)
        self.plots.append(violin_plot)

        strip_plot = plot.strip_plot(comb)
        self.plots.append(strip_plot)

        self.rendered = self.render()


class CatCat:
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, cat1, cat2):
        self.plots = []
        self.name = f'{cat1.column_name}_{cat2.column_name}'
        comb = Combiner(x=cat1, hue=cat2)

        count_plt = plot.count_plot_combiner(comb)
        self.plots.append(count_plt)

        self.rendered = self.render()


class Num2Cat:
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, num1, num2, cat1):
        self.plots = []
        self.name = f'{num1.column_name}_{num2.column_name}_{cat1.column_name}'
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


class NumCat2:
    def render(self):
        path_to_template = '/Users/maximzabelin/Programming/hse2/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, num1, cat1, cat2):
        self.plots = []
        self.name = f'{num1.column_name}_{cat1.column_name}_{cat2.column_name}'
        comb = Combiner(x=cat1, y=num1, hue=cat2)

        bar = plot.bar_plot(comb)
        self.plots.append(bar)

        violin = plot.violin_plot(comb)
        self.plots.append(violin)

        heatmap = plot.heat_map(comb)
        self.plots.append(heatmap)

        self.rendered = self.render()
