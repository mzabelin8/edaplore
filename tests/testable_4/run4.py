from report.report import Report
import seaborn as sns
import pandas as pd


df = sns.load_dataset('tips')
path = '/Users/maximzabelin/desktop'


R = Report(df, path)

