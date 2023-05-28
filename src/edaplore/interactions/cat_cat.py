from src.edaplore.separator.combine import *
from src import edaplore as plot
from jinja2 import Environment, FileSystemLoader


class CatCat:
    def render(self):
        """
        Renders a Jinja template using the plot names.

        :return: A string containing the rendered HTML template.
        """
        path_to_template = '/edaplore/html_templates'
        env = Environment(loader=FileSystemLoader(path_to_template))
        template = env.get_template('interaction_num_num.html').render(plot_names=self.plots)
        return template

    def __init__(self, cat1, cat2):
        """
        Initializes the CatCat class, creating a plot of the interaction between two categorical variables.

        :param cat1: The first Categorical object.
        :param cat2: The second Categorical object.
        """
        self.plots = []
        self.name = f'{cat1.column_name} vs {cat2.column_name}'
        comb = Combiner(x=cat1, hue=cat2)

        count_plt = plot.count_plot_combiner(comb)
        self.plots.append(count_plt)

        self.rendered = self.render()
