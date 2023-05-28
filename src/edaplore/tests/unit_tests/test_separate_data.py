import unittest
import pandas as pd
from src.edaplore.separator.data_separator import Separator


class TestSeparate(unittest.TestCase):
    def fill(self):
        num_int = [1, 2, 3]
        num_float = [1.23, 4.32, 9.99]
        num_binary = [1, 0, 1]
        binary = [False, True, True]
        categ_2 = ['a', 'a', 'b']
        categ_3 = ['ab', 'a', 'b']

        all_types = {'num_int': num_int,
                     'num_float': num_float,
                     'num_binary': num_binary,
                     'binary': binary,
                     'categ_2': categ_2,
                     'categ_3': categ_3
                     }
        self.all_types_df = pd.DataFrame(all_types)

        numeric = {'num_int': num_int,
                   'num_float': num_float,
                   'num_binary': num_binary}
        self.num_df = pd.DataFrame(numeric)

    def test_separate_numeric(self):
        self.fill()
        S = Separator(self.num_df)
        S.separate()

        self.assertEqual(2, len(S.numeric))
        self.assertEqual(1, len(S.boolean))
        self.assertEqual(0, len(S.categorical))
        self.assertEqual(3, len(S.data_classes))

    def test_separete_all_types(self):
        self.fill()
        S = Separator(self.all_types_df)
        S.separate()

        self.assertEqual(2, len(S.numeric))
        self.assertEqual(2, len(S.boolean))
        self.assertEqual(2, len(S.categorical))
        self.assertEqual(6, len(S.data_classes))


if __name__ == '__main__':
    unittest.main()
