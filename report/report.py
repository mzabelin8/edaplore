from separator.data_separator import Separator
from overview.overview_class import Overview
from interactions.inter_main import Comparator
from html_templates.template_loader import find_template
from interactions.genmap import GenMap


class Report:

    def render(self):
        template = find_template('report_for_separator.html').render(over=self.overview,
                                                                     sep=self.separ,
                                                                     comp=self.compar,
                                                                     gm=self.genmap)
        return template

    def save_html(self, path):
        with open(path, 'w') as f:
            f.write(self.rendered)

    def __init__(self, df, path, fill_mis=False, drop_outliers=False, threshold=0.95, ohe=False):
        self.separ = Separator(data=df,
                               fill_mis=fill_mis,
                               drop_outliers=drop_outliers,
                               threshold=threshold,
                               ohe=ohe)

        self.overview = Overview(self.separ.data_classes)
        self.compar = Comparator(self.separ)
        self.genmap = GenMap(self.separ.data)

        self.rendered = self.render()
        self.save_html(path)
