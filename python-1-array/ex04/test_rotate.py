import unittest
import numpy as np
from rotate import ft_rotate


class TestRotate(unittest.TestCase):

    def setUp(self):
        self.arr = np.arange(1, 21).reshape(2, 10)

    def test_failed_with_wrong_dimension_3(self):
        a = np.arange(10).reshape(2, 5)
        b = np.arange(10).reshape(5, 2)
        self.assertFalse(np.array_equal(a, b))

    def test_expected_shape_after_transpose(self):
        arr_2_d = np.empty((2, 3))
        self.assertEqual(arr_2_d.T.shape, (3, 2))

        arr_3_d = np.empty((2, 3, 4))
        self.assertEqual(arr_3_d.T.shape, (4, 3, 2))

        arr_4_d = np.empty((2, 3, 4, 5))
        self.assertEqual(arr_4_d.T.shape, (5, 4, 3, 2))

        arr_5_d = np.empty((2, 3, 4, 5, 6))
        self.assertEqual(arr_5_d.T.shape, (6, 5, 4, 3, 2))

        arr_6_d = np.empty((2, 3, 4, 5, 6, 7))
        self.assertEqual(arr_6_d.T.shape, (7, 6, 5, 4, 3, 2))

    def test_success_with_equal_element_and_dimension(self):
        a = np.arange(10).reshape(5, 2)
        b = np.arange(10).reshape(5, 2)
        self.assertTrue(np.array_equal(a, b))

    def test_rotate_success_2_dimension(self):
        self.assertTrue(np.array_equal(self.arr.T, ft_rotate(self.arr)))

    def test_rotate_success_3_dimension(self):
        three_dimension = self.arr.reshape(2, 2, 5)
        # print(three_dimension.T.shape)
        self.assertTrue(
            np.array_equal(three_dimension.T, ft_rotate(three_dimension)))
