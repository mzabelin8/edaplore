from separator.data_separator import Separator
from overview.overview_class import Overview
from interactions.inter_main import Comparator

from html_templates.template_loader import find_template


class Report:

    def render(self):
        template = find_template('report_for_separator.html').render(over=self.overview,
                                                                     sep=self.separ,
                                                                     comp=self.compar)
        return template

    def save_html(self, path):
        with open(path + '/report2.html', 'w') as f:
            f.write(self.rendered)

    def __init__(self, df, path, fill_mis=False):
        self.separ = Separator(df, fill_mis=fill_mis)
        self.overview = Overview(self.separ.data_classes)
        self.compar = Comparator(self.separ)

        self.rendered = self.render()
        self.save_html(path)
