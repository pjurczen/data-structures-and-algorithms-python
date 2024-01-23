from unittest import TestCase

from numpy.testing import assert_equal

from src.randomized_selection import RandomizedSelection


class TestRandomizedSelection(TestCase):
    def test_small_case(self):
        # given
        numbers = [40, 50, 30, 70, 90, 10, 20, 25]
        testee = RandomizedSelection()
        # when
        result = testee.select(numbers, 3)
        # then
        assert_equal(result, 30)
