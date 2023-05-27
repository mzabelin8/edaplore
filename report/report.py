from separator.data_separator import Separator
from overview.overview_class import Overview
from interactions.inter_main import Comparator
from interactions.interaction_comb import ComparatorU
from html_templates.template_loader import find_template
from interactions.genmap import GenMap
import time


class Report:

    def render(self):
        template = find_template('report_dreop.html').render(over=self.overview,
                                                                     sep=self.separ,
                                                                     comp=self.compar,
                                                                     gm=self.genmap)
        return template

    def save_html(self, path):
        with open(path, 'w') as f:
            f.write(self.rendered)

    def __init__(self, df, path, fill_mis=False, drop_outliers=False, threshold=0.95, ohe=False):
        start_time = time.time()
        full_time = time.time()
        self.separ = Separator(data=df,
                               fill_mis=fill_mis,
                               drop_outliers=drop_outliers,
                               threshold=threshold,
                               ohe=ohe)
        print(f'separ done {time.time() - start_time}')
        start_time = time.time()

        self.overview = Overview(self.separ.data_classes)
        print(f'overview done {time.time() - start_time}')
        start_time = time.time()
        self.compar = ComparatorU(self.separ, cols=self.separ.col_names)
        print(f'compU done {time.time() - start_time}')
        start_time = time.time()
        self.genmap = GenMap(self.separ.data)
        print(f'genmap done {time.time() - start_time}')
        start_time = time.time()

        self.rendered = self.render()
        self.save_html(path)
        print(f'full done {time.time() - full_time}')

