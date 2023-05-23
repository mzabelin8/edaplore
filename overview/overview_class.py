from separator import define_data_type
import types_clases.names as names

from jinja2 import Environment, Template, FileSystemLoader
from html_templates.template_loader import find_template


class Overview:
    def count_categories_and_miss(self):
        for el in self.data:
            self.miss_vals += el.miss_values

            if names.numeric == el.type_name:
                self.count_numeric += 1

            if names.bolean == el.type_name:
                self.count_boolean += 1

            if names.categorical == el.type_name:
                self.count_categorical += 1

    def render(self):
        template = find_template('overview_template.html').render(overview=self)
        return template

    def __init__(self, data):
        self.data = data
        self.count_columns = len(data)
        self.count_rows = data[0].count_values

        self.miss_vals = 0
        self.count_numeric = 0
        self.count_boolean = 0
        self.count_categorical = 0

        self.count_categories_and_miss()
        self.rendered = self.render()
