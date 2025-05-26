import unittest
from Triangle import Triangle, TriangleException

class TestTriangle(unittest.TestCase):
    def test_creates_triangle_with_zero_sides_raises_exception(self):
        with self.assertRaises(TriangleException):
            Triangle(0, 0, 0)

    def test_creates_triangle_with_negative_sides_raises_exception(self):
        with self.assertRaises(TriangleException):
            Triangle(-3, -4, -5)

    def test_identifies_equilateral_triangle_correctly(self):
        triangle = Triangle(5, 5, 5)
        self.assertTrue(triangle.isIsosceles())

    def test_string_representation_handles_large_numbers(self):
        triangle = Triangle(3000, 4000, 5000)
        self.assertEqual(str(triangle), "Triangle with sides 3000, 4000, 5000")

    def test_show_method_handles_invalid_triangle(self):
        with self.assertRaises(TriangleException):
            Triangle(1, 1, 3).show()

if __name__ == '__main__':
    unittest.main()