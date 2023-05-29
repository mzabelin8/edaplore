from src.edaplore import Report
import pandas as pd

# df = pd.read_csv('/Users/maximzabelin/Desktop/titanic/train.csv')
#
# df = df.head(100)


# s = Separator(df,
#               fill_mis=False,
#               drop_outliers=False,
#               ohe=False)
# print(s.col_names)

# data = sns.load_dataset('tips')
data = pd.read_csv('/Users/maximzabelin/Desktop/titanic/train.csv')
path = '/Users/maximzabelin/desktop/tdreop_1.html'
R = Report(data,
           path,
           fill_mis=False,
           drop_outliers=False,
           ohe=False)
