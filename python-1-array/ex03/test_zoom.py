import unittest
import numpy as np
from PIL import Image
from load_image import ft_load
from zoom import ft_zoom


class TestZoom(unittest.TestCase):

    def setUp(self):
        self.original = ft_load("../resources/animal.jpeg")

    def _show_image(self, arr: np.ndarray):
        img = Image.fromarray(arr)
        img.show()

    def test_success_grayscale(self):
        z = ft_zoom(self.original, x=450, y=100, size=400, mode='L')
        self.assertEqual(z.shape, (400, 400))

    def test_success_RGB(self):
        z = ft_zoom(self.original, x=450, y=100, size=400)
        self.assertEqual(z.shape, (400, 400, 3))

    def test_nagative_value(self):
        with self.assertRaises(ValueError):
            ft_zoom(self.original, x=-450, y=100, size=400)

        with self.assertRaises(ValueError):
            ft_zoom(self.original, x=450, y=-100, size=400)

        with self.assertRaises(ValueError):
            ft_zoom(self.original, x=450, y=100, size=-400)

        with self.assertRaises(ValueError):
            ft_zoom(self.original, x=-450, y=-100, size=-400)

    def test_coordinate_out_of_range(self):
        with self.assertRaises(ValueError):
            ft_zoom(self.original, x=1000, y=100)

        with self.assertRaises(ValueError):
            ft_zoom(self.original, x=100, y=1500)

    def test_oversize(self):
        x = 450
        y = 100
        size = 4000
        z = ft_zoom(self.original, x, y, size)
        expect_y = self.original.shape[0] - y
        expect_x = self.original.shape[1] - x
        self.assertEqual(z.shape[0], expect_y)
        self.assertEqual(z.shape[1], expect_x)
        # self._show_image(z)
