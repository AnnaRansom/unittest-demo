# tests/test_calculator.py
# tests/test_calculator.py

import unittest
from src.calculator import Calculator


class TestCalculatorBasics(unittest.TestCase):
    def setUp(self):
        # Runs before each test - creates a fresh Calculator instance
        self.calc = Calculator()

    def test_add_normal(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    # def test_subtract_normal(self):
    #     # TO DO: verify subtraction
    #     pass

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(2, 0)

    def test_divide_normal(self):
        result = self.calc.divide(2, 3)
        self.assertAlmostEqual(result, 0.6666666666)
