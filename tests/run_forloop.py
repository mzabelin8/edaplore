import pandas as pd
import seaborn as sns
from overview.overview_class import Overview
from separator.data_separator import Separator
from jinja2 import Environment, Template, FileSystemLoader
import random
from images.make_plot import MakePlot

from overview.overview_class import Overview
from types_clases.type_numeric import Numeric
from types_clases.type_categorical import Categorical
from types_clases.type_boolean import Boolean

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
data = pd.Series(a)
N1 = Numeric(data, 'colonka 1')

a2 = []
for i in range(10):
    a2.append(random.randint(-10, 10))
data2 = pd.Series(a2)
N2 = Numeric(data2, 'colonka 2')

a3 = []
for i in range(10):
    a3.append(random.randint(-10, 10))
data3 = pd.Series(a3)
N3 = Numeric(data3, 'colonka 3')

nums = [N1, N2, N3]

b = ['asdf', 'fdas', 'qwer', 'asdf']
df = pd.Series(b)
C = Categorical(df, 'categ')

c = [True, True, False]
dt = pd.Series(c)
B = Boolean(dt, 'boole')

all = [N1, N2, N3, C, B]
nums = [N1, N2, N3]
categs = [C]
bools = [B]

O = Overview(all)

env = Environment(loader=FileSystemLoader('../html_templates/templates_for_typeclasses'))
t = env.get_template('report.html').render(over=O, nums=nums, categs=categs, bools=bools)

with open('/Users/maximzabelin/desktop/report_res.html', 'w') as f:
    f.write(t)

print(t)
