from unittest import TestCase

from numpy.testing import assert_equal

from quick_sort import QuickSort

class TestQuickSort(TestCase):

    def test_small_case(self):
        # given
        numbers = [40, 50, 30, 70, 90, 10, 20, 25]
        testee = QuickSort()
        expected = [10, 20, 25, 30, 40, 50, 70, 90]
        # when
        testee.sort(numbers)
        # then
        assert_equal(numbers, expected)