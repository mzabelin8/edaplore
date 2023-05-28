import unittest
import pandas as pd
from edaplore.types_clases.type_boolean import Boolean
from edaplore.types_clases.type_numeric import Numeric
from edaplore.types_clases.type_categorical import Categorical


class TestTypeclasses(unittest.TestCase):
    def fill(self):
        self.numeric_sr = pd.Series([1, 2, 3, 4])
        self.boolead_sr = pd.Series([True, True, True, False])
        self.categorical_sr = pd.Series(['a', 'a', 'd', 'c'])

    def test_inheritance(self):
        self.fill()
        N = Numeric(self.numeric_sr, 'num')
        B = Boolean(self.boolead_sr, 'bool')
        C = Categorical(self.categorical_sr, 'categ')

        self.assertEqual(N.column_name, 'num')
        self.assertNotEqual(N.column_name, 'not num')
        # self.assertEqual(N.data, self.numeric_sr)
        print(N.data == self.numeric_sr)

        self.assertEqual(B.column_name, 'bool')
        self.assertNotEqual(B.column_name, 'not bool')
        # self.assertEqual(B.data, self.boolead_sr)
        print(B.data == self.boolead_sr)

        self.assertEqual(C.column_name, 'categ')
        self.assertNotEqual(C.column_name, 'not categ')
        # self.assertEqual(C.data, self.categorical_sr)
        print(C.data == self.categorical_sr)

    def test_stats(self):
        self.fill()

        N = Numeric(self.numeric_sr, 'num')
        B = Boolean(self.boolead_sr, 'bool')
        C = Categorical(self.categorical_sr, 'categ')

        min_val = self.numeric_sr.min()
        max_val = self.numeric_sr.max()
        mean_val = self.numeric_sr.mean()
        std_val = self.numeric_sr.std()

        ratio = sum(self.boolead_sr) / len(self.boolead_sr)

        self.assertEqual(N.max, max_val)
        self.assertEqual(N.min, min_val)
        self.assertEqual(N.mean, mean_val)
        self.assertEqual(N.std, std_val)
        self.assertEqual(N.count_values, len(self.numeric_sr))

        self.assertEqual(B.ratio, ratio)
        self.assertEqual(B.count_values, len(self.boolead_sr))

        self.assertEqual(C.count_categories, len(set(self.categorical_sr)))
        self.assertEqual(C.count_values, len(self.categorical_sr))


if __name__ == '__main__':
    unittest.main()
