from unittest import TestCase

from numpy.testing import assert_equal

from src.largest_number import LargestNumber


class TestLargestNumber(TestCase):

    def test_small_case(self):
        # given
        numbers = [4, 5, 8, 9, 10, 11, 7, 3, 2, 1]
        testee = LargestNumber()
        # when
        result = testee.find_largest_number(numbers)
        # then
        assert_equal(result, 11)

    def test_skewed_case(self):
        # given
        numbers = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        testee = LargestNumber()
        # when
        result = testee.find_largest_number(numbers)
        # then
        assert_equal(result, 11)
