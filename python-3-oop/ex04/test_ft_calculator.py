import unittest
import numpy as np
from .ft_calculator import Calculator
from io import StringIO
from contextlib import redirect_stdout


class TestFtCalculator(unittest.TestCase):

    def setUp(self):
        self.a = [5, 10, 2]
        self.b = [2, 4, 3]
        self.a_np = np.array(self.a, dtype=float)
        self.b_np = np.array(self.b, dtype=float)

    def _dotproduct(self):
        return sum([a * b for a, b in zip(self.a, self.b)])

    def _add_vec(self):
        return [a + b for a, b in zip(self.a, self.b)]

    def _sous_vec(self):
        return [a - b for a, b in zip(self.a, self.b)]

    def test_dot_product(self):
        self.assertEqual(np.dot(self.a_np, self.b_np), self._dotproduct())

        with StringIO() as buf, redirect_stdout(buf):
            Calculator.dotproduct(self.a, self.b)
            output = buf.getvalue().strip()
        self.assertEqual('Dot product is: 56', output)

    def test_add_vec(self):
        self.assertEqual((self.a_np + self.b_np).tolist(), self._add_vec())

        with StringIO() as buf, redirect_stdout(buf):
            Calculator.add_vec(self.a, self.b)
            output = buf.getvalue().strip()
        self.assertEqual('Add Vector is: [7, 14, 5]', output)

    def test_sous_vec(self):
        self.assertEqual((self.a_np - self.b_np).tolist(), self._sous_vec())

        with StringIO() as buf, redirect_stdout(buf):
            Calculator.sous_vec(self.a, self.b)
            output = buf.getvalue().strip()
        self.assertEqual('Sous Vector is: [3, 6, -1]', output)
