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

    def test_adding_two_numbers_returns_their_sum(self):
        add = self.calc.add('1,2')
        self.assertEqual(3, add)

    def test_adding_unknown_amount_of_numbers_returns_their_sum(self):
        add = self.calc.add('1,2,3,4,5')
        self.assertEqual(15, add)
