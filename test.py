from figure import *
import unittest
import math


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(5)
        self.assertAlmostEqual(c.calculate_area(), math.pi * (5 ** 2))
        self.assertAlmostEqual(c.calculate_area(), FigureManager.calculate_area(c))

    def test_circle_radius_setter(self):
        c = Circle(5)
        c.radius = 7
        self.assertEqual(c.radius, 7)

    def test_circle_negative_radius(self):
        with self.assertRaises(Exception) as context1:
            c = Circle(5)
            c.radius = -1
        self.assertTrue('некорректное значение: радиус должен быть больше нуля' in str(context1.exception))
        with self.assertRaises(Exception) as context2:
            c = Circle(-5)
        self.assertTrue('некорректное значение: радиус должен быть больше нуля' in str(context2.exception))


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.calculate_area(), 6)
        self.assertAlmostEqual(t.calculate_area(), FigureManager.calculate_area(t))

    def test_triangle_is_right_triangle(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right_triangle())
        t1 = Triangle(1, 1, 1)
        self.assertFalse(t1.is_right_triangle())

    def test_triangle_invalid_side(self):
        with self.assertRaises(Exception) as context1:
            t = Triangle(1, 1, 3)
        self.assertTrue('некорректное значение' in str(context1.exception))
        with self.assertRaises(Exception) as context2:
            t = Triangle(2, 2, 3)
            t.side1 = 1
        self.assertTrue('некорректное значение' in str(context2.exception))


if __name__ == '__main__':
    unittest.main()
