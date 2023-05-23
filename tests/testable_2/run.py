import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from jinja2 import Environment, Template, FileSystemLoader

from separator.data_separator import Separator
from overview.overview_class import Overview
from interactions.inter_main import Comparator

df = sns.load_dataset('titanic')

separ = Separator(data=df)
ov = Overview(separ.data_classes)
compar = Comparator(separ)


envs = Environment(loader=FileSystemLoader('/Users/maximzabelin/Programming/hse2/html_templates'))
t = envs.get_template('report_for_separator.html').render(over=ov, sep=separ, comp=compar)

with open('/Users/maximzabelin/desktop/T1.html', 'w') as f:
    f.write(t)
