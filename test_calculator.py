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

    def test_adding_numbers_separated_by_new_line_returns_their_sum(self):
        add = self.calc.add('1\n2,3,4\n5')
        self.assertEqual(15, add)

    def test_adding_numbers_separated_by_a_different_delimiter_returns_their_sum(self):
        add = self.calc.add('//;\n1;2')
        self.assertEqual(3, add)

    def test_adding_negative_numbers__returns_exception_message_with_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            self.calc.add('1,2,-3,4,-5')
        self.assertTrue('negatives not allowed: -3,-5' in str(context.exception))
