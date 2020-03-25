from typing import Optional, Dict, Any
from unittest import TestCase
import unittest
from .Calculator import Calculator


class TestCalculator(TestCase):
    def test_evaluate(self):
        foo = Calculator.evaluate("2 + 2")
        TestCase.assertAlmostEqual(self, 4, foo)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2 - 2"), 0)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2 * 2"), 4)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2 / 2"), 1)

        assert Calculator.evaluate("2.1 + 2") == 4.1
        TestCase.assertAlmostEqual(self, Calculator.evaluate("1.9 - 2"), -0.1)
        assert Calculator.evaluate("2.1 * 2") == 4.2
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2.2 / 2"), 1.1)

    def test_complex(self):
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2.2 + 2 + 1"), 5.2)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2.2 + 2 * 1"), 4.2)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2.2 + 2 * 9"), 20.2)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2.2 - 2 * 9"), 2.2 - 2 * 9)

        TestCase.assertAlmostEqual(self, Calculator.evaluate("(2.2 - 2) * 9"), (2.2 - 2) * 9)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2 / 2 + 3 * 4 - 6"), 7)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2 / (2 + 3) * 4 - 6"), 2 / (2 + 3) * 4 - 6)
        TestCase.assertAlmostEqual(self, Calculator.evaluate("2 / (2 + 3) * 4 - 6"), 2 / (2 + 3) * 4 - 6)

    def test_extract_brackets_expression_1(self):
        dd: Optional[Dict[int, int]] = Calculator.extract_brackets_expression("aaaa(bb()()ccc)dd")
        expected = {4: 14, 7: 8, 9: 10}
        TestCase.assertDictEqual(self, expected, dd)

        pure = Calculator.purify_from_included_brackets(dd)
        TestCase.assertDictEqual(self, {4: 14}, pure)

    def test_extract_brackets_expression_2(self):
        dd: Optional[Dict[int, int]] = Calculator.extract_brackets_expression("aaaa(bb ccc)d(d)")
        expected = {4: 11, 13: 15}
        TestCase.assertDictEqual(self, expected, dd)

        pure = Calculator.purify_from_included_brackets(dd)
        TestCase.assertDictEqual(self, expected, pure)

if __name__ == '__main__':
    unittest.main()


