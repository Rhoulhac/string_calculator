from unittest import TestCase

from calculator import Calculator


class TestAddFunction(TestCase):
    def test_adding_empty_string_returns_zero(self):
        calc = Calculator()
        add = calc.add('')
        self.assertEqual(0, add)
