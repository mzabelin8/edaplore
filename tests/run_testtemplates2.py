import pandas as pd
import seaborn as sns
from overview.overview_class import Overview
from separator.data_separator import Separator
from jinja2 import Environment, Template, FileSystemLoader
import random

a1 = []
a2 = []
a3 = []

for _ in range(100):
    a1.append(random.randint(-10, 100))
    a2.append(random.randint(-10, 100))
    a3.append(random.randint(-10, 100))

d = {'col 1': a1, 'col 2': a2, 'col 3': a3}
df = pd.DataFrame(d)

S = Separator(df)
S.separate()
O = Overview(S.data_classes)

env = Environment(loader=FileSystemLoader('../html_templates/test_tempates2'))

template = env.get_template('main.html')

rendered_template = template.render(overview_object=O, numerics=S.data_classes)

with open('/Users/maximzabelin/desktop/ovnums.html', 'w') as f:
    f.write(rendered_template)
