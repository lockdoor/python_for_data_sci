import unittest
from .in_out import square, pow, outer


class TestInOut(unittest.TestCase):
    def test_main(self):
        """main for in_out.py"""
        counter = outer(3, square)
        # 3 ** 2
        result = counter()
        self.assertEqual(result, 3 ** 2)
        print(result)
        # (3 ** 2) ** 2
        result = counter()
        self.assertEqual(result, 3 ** 4)
        print(result)
        # ((3 ** 2) ** 2) ** 2
        result = counter()
        self.assertEqual(result, 3 ** 8)
        print(result)

        counter = outer(1.5, pow)
        print(counter())
        print(counter())
        print(counter())
