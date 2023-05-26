import seaborn as sns
from interactions.genmap import GenMap
from jinja2 import Environment, Template, FileSystemLoader, PackageLoader
import pandas as pd


df = pd.read_csv('/Users/maximzabelin/Desktop/titanic/train.csv')
env = Environment(loader=FileSystemLoader('.'))
genmap = GenMap(df)
template = env.get_template('temp_6.html').render(gm=genmap)

with open('/Users/maximzabelin/desktop/gm_1_1.html', 'w') as f:
    f.write(template)
