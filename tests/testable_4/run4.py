from report.report import Report
import seaborn as sns
import pandas as pd
from separator.data_separator import Separator

# df = sns.load_dataset('tips')
df = pd.read_csv('/Users/maximzabelin/Desktop/titanic/train.csv')

df = df.head(100)
path = '/Users/maximzabelin/desktop'

# s = Separator(df,
#               fill_mis=True,
#               drop_outliers=True,
#               ohe=True)
# print(s.col_names)
R = Report(df,
           path,
           fill_mis=False,
           drop_outliers=False,
           ohe=False)
