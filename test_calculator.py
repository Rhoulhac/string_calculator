from unittest import TestCase

from calculator import Calculator


class TestAddFunction(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_adding_empty_string_returns_zero(self):
        add = self.calc.add('')
        self.assertEqual(0, add)

    def test_adding_one_number_returns_the_same_number(self):
        add = self.calc.add('1')
        self.assertEqual(1, add)
