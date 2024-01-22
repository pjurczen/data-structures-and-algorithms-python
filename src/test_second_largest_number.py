from unittest import TestCase
from numpy.testing import assert_equal

from src.second_largest_number import SecondLargestNumber


class TestSecondLargestNumber(TestCase):

    def test_small_case(self):
        # given
        numbers = [5, 7, 1, 3, 11, 5, 10, 12, 30, 2, 4]
        testee = SecondLargestNumber()
        # when
        result = testee.find_second_largest_number(numbers)
        # then
        assert_equal(result, 12)
