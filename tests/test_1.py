import pandas as pd

import pandas as pd
from separator.data_separator import Separator

import test_names_1

from separator.define_data_type import is_bool_type

num_int = [1, 2, 3]
num_float = [1.23, 4.32, 9.99]
num_binary = [1, 0, 1]
binary = [False, True, True]
categ_2 = ['a', 'a', 'b']
categ_3 = ['ab', 'a', 'b']

numeric = {'num_int': num_int,
           'num_float': num_float,
           'num_binary': num_binary}
num_df = pd.DataFrame(numeric)

S = Separator(num_df)
S.separate()

print(len(S.numeric))
print(len(S.boolean))
print(len(S.categorical))
print(len(S.data_classes))
