from unittest import TestCase

from src.roman_to_integer import romanToInt


class TestRomanToInteger(TestCase):

    def test_triple_ones(self):
        input: str = "III"
        result: int = romanToInt(input)
        assert result == 3

    def test_repeated_char(self):
        input: str = "XXVII"
        result: int = romanToInt(input)
        assert result == 27
