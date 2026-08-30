# Test calculator app here
import unittest
from calculator.calc import Calculator



class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
       
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):

        self.assertEqual(self.calc.add(-2, -7), -9)

    def test_add_floating_point_numbers(self):
        self.assertAlmostEqual(self.calc.add(1.1, 0.5), 1.6)
        self.assertAlmostEqual(self.calc.add(-1.222, 5), 3.778)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-9, -3), -6)

    def test_subtract_floating_point_numbers(self):
        self.assertAlmostEqual(self.calc.subtract(6.61, 4.2), 2.41)
        self.assertAlmostEqual(self.calc.subtract(88, 18.25), 69.75)

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-12, 4), -48)

    def test_multiply_floating_point_numbers(self):
        self.assertAlmostEqual(self.calc.multiply(22.2, 2), 44.4)
        self.assertAlmostEqual(self.calc.multiply(-33.12, -7.1), 235.152)

    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.division(10, 2), 5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.division(-99, -3), 33)

    def test_division_floating_point_numbers(self):
        self.assertAlmostEqual(self.calc.division(6.6, 2.2), 3)
        self.assertAlmostEqual(self.calc.division(125, 500), .25)

    def test_division_by_zero(self):
        with self.assertRaises(ArithmeticError):
            self.calc.division(5,0)