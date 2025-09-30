import unittest
from .statistics import ft_statistics
import numpy as np


class TestFtTestArgs(unittest.TestCase):

    def test_validation(self):

        with self.assertRaises(ValueError) as e:
            ft_statistics()
        self.assertEqual(str(e.exception), 'List of Int or Float is Required')

        with self.assertRaises(ValueError) as e:
            ft_statistics(toto='mean')
        self.assertEqual(str(e.exception), 'List of Int or Float is Required')

        with self.assertRaises(ValueError) as e:
            ft_statistics('hello', 'world', toto='mean')
        self.assertEqual(str(e.exception), 'List of Int or Float is Required')

        with self.assertRaises(ValueError) as e:
            ft_statistics(1, 2, 3, ejfhhe='mean')
        self.assertEqual(
            str(e.exception), "Invalid keyword arguments: {'ejfhhe'}")

        with self.assertRaises(ValueError) as e:
            ft_statistics(1, 42, 360, 11, 64)
        self.assertEqual(str(e.exception), "Required at lease one kwargs")

    def test_first(self):
        lst = [1, 42, 360, 11, 64]
        ft_statistics(*lst, toto="mean", tutu="median", tata="quartile")
        lst_np = np.array(lst)
        print(f'mean : {np.mean(lst_np)}')
        print(f'median : {np.median(lst_np)}')
        print(f'quartile : {np.percentile(lst_np, [25, 75])}')

    def test_second(self):
        lst = [5, 75, 450, 18, 597, 27474, 48575]
        ft_statistics(*lst, hello="std", world="var")
        lst_np = np.array(lst)
        print(f'std : {np.std(lst_np)}')
        print(f'var : {np.var(lst_np)}')
