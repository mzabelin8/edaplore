from report.report import Report
import seaborn as sns
import pandas as pd
from separator.data_separator import Separator
from interactions.interaction_comb import ComparatorU
from jinja2 import Environment, Template, FileSystemLoader, PackageLoader
import warnings
import time

start_time = time.time()

warnings.filterwarnings("ignore")

# data = sns.load_dataset('tips')
data = pd.read_csv('/Users/maximzabelin/Desktop/titanic/train.csv')

separ = Separator(data.head(50))
comparator = ComparatorU(separ, cols=separ.col_names)
print(f'done {time.time() - start_time}')
env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('just_inter.html').render(comp=comparator)
with open('/Users/maximzabelin/desktop/AAB.html', 'w') as f:
    f.write(template)

print(comparator.storage.keys())
