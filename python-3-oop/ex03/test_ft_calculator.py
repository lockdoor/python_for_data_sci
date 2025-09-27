import unittest
from .ft_calculator import Calculator
from io import StringIO
from contextlib import redirect_stdout


class TestCalculator(unittest.TestCase):

    def test_add(self):
        ori_arr = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        cal_arr = Calculator(ori_arr)

        with StringIO() as buf, redirect_stdout(buf):
            cal_arr + 5
            output = buf.getvalue().strip()

        expect_arr = [5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0]
        self.assertEqual(output, str(expect_arr))

    def test_mul(self):
        ori_arr = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        cal_arr = Calculator(ori_arr)

        with StringIO() as buf, redirect_stdout(buf):
            cal_arr * 5
            output = buf.getvalue().strip()

        expect_arr = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
        self.assertEqual(output, str(expect_arr))

    def test_sub_and_devide(self):
        ori_arr = [10.0, 15.0, 20.0]
        cal_arr = Calculator(ori_arr)

        with StringIO() as buf, redirect_stdout(buf):
            cal_arr - 5
            output = buf.getvalue().strip()

        expect_arr = [5.0, 10.0, 15.0]
        self.assertEqual(output, str(expect_arr))

        with StringIO() as buf, redirect_stdout(buf):
            cal_arr / 5
            output = buf.getvalue().strip()

        expect_arr = [1.0, 2.0, 3.0]
        self.assertEqual(output, str(expect_arr))

    def test_div_by_zero(self):
        ori_arr = [10.0, 15.0, 20.0]
        cal_arr = Calculator(ori_arr)

        with StringIO() as buf, redirect_stdout(buf):
            cal_arr / 0
            output = buf.getvalue().strip()

        self.assertIn('ZeroDivisionError', output)
