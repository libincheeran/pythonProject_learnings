from unittest import TestCase

from gender_converter import gender_converter


class Test(TestCase):
    def test_gender_converter(self):
        actual = gender_converter("M")
        expected = "Male"
        self.assertEqual(actual,expected)
