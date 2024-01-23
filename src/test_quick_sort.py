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

    def test_input_file(self):
        # given
        with open('quick_sort_input.txt', 'r', encoding='UTF-8') as file:
            # Read each line, strip any whitespace, and convert to integer
            numbers = [int(line.strip()) for line in file]
        testee = QuickSort()
        # when
        testee.sort(numbers)
        result = all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
        # then
        assert_equal(result, True)
