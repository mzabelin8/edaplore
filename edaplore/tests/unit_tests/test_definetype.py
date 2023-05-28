import unittest
import pandas as pd

from edaplore.separator import define_data_type


class TestTypedef(unittest.TestCase):

    def fill(self):
        self.num_int = pd.Series([1, 2, 3])
        self.num_float = pd.Series([1.0, 2.45, 5.99])
        self.num_binary = pd.Series([1, 0, 1, 0, 0])
        self.bin = pd.Series([True, True, False])
        self.bin_str = pd.Series(['True', 'False'])
        self.categ_2 = pd.Series(['a', 'b', 'a'])
        self.categ_3 = pd.Series(['a', 'b', 'ab'])
        self.mixed = pd.Series([1, 'asd', False])


    def test_numeric(self):
        self.fill()
        self.assertTrue(define_data_type.is_numeric_type(self.num_int))
        self.assertTrue(define_data_type.is_numeric_type(self.num_float))
        self.assertTrue(define_data_type.is_numeric_type(self.num_binary))
        self.assertFalse(define_data_type.is_numeric_type(self.bin))
        self.assertFalse(define_data_type.is_numeric_type(self.bin_str))
        self.assertFalse(define_data_type.is_numeric_type(self.categ_3))
        self.assertFalse(define_data_type.is_numeric_type(self.mixed))

    def test_boolean(self):
        self.fill()
        self.assertTrue(define_data_type.is_bool_type(self.bin))
        self.assertTrue(define_data_type.is_bool_type(self.num_binary))
        self.assertFalse(define_data_type.is_bool_type(self.num_int))
        self.assertFalse(define_data_type.is_bool_type(self.num_float))
        self.assertFalse(define_data_type.is_bool_type(self.bin_str))
        self.assertFalse(define_data_type.is_bool_type(self.categ_2))
        self.assertFalse(define_data_type.is_bool_type(self.categ_3))
        self.assertFalse(define_data_type.is_bool_type(self.mixed))


    def test_categorical(self):
        self.fill()
        self.assertTrue(define_data_type.is_categorical_type(self.bin_str))
        self.assertTrue(define_data_type.is_categorical_type(self.categ_2))
        self.assertTrue(define_data_type.is_categorical_type(self.categ_3))
        self.assertTrue(define_data_type.is_categorical_type(self.mixed))
        self.assertFalse(define_data_type.is_categorical_type(self.num_int))
        self.assertFalse(define_data_type.is_categorical_type(self.num_float))
        self.assertFalse(define_data_type.is_categorical_type(self.num_binary))
        self.assertFalse(define_data_type.is_categorical_type(self.bin))


if __name__ == '__main__':
    unittest.main()














