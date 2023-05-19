import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from jinja2 import Environment, Template, FileSystemLoader

from separator.data_separator import Separator
from overview.overview_class import Overview


df = sns.load_dataset('titanic')

separ = Separator(data=df)
ov = Overview(separ.data_classes)

envs = Environment(loader=FileSystemLoader('/Users/maximzabelin/Programming/hse2/html_templates'))
t = envs.get_template('report_for_separator.html').render(over=ov, sep=separ)

with open('/Users/maximzabelin/Programming/hse2/html_templates/separ_1.html', 'w') as f:
    f.write(t)
