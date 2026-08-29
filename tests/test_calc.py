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