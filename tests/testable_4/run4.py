from report.report import Report
import seaborn as sns
import pandas as pd
from separator.data_separator import Separator


# df = pd.read_csv('/Users/maximzabelin/Desktop/titanic/train.csv')
#
# df = df.head(100)


# s = Separator(df,
#               fill_mis=False,
#               drop_outliers=False,
#               ohe=False)
# print(s.col_names)

data = sns.load_dataset('tips')
path = '/Users/maximzabelin/desktop/tes_1_1.html'
R = Report(data,
           path,
           fill_mis=True,
           drop_outliers=False,
           ohe=True)
