from unittest import TestCase

from src.search_insert_position import search_insert


class TestSearchInsertPosition(TestCase):

    def test_single_value(self):
        input = [1]
        result = search_insert(input, 1)
        assert result == 0

    def test_two_values(self):
        input = [1, 3]
        result = search_insert(input, 3)
        assert result == 1

    def test_two_values_between(self):
        input = [1, 3]
        result = search_insert(input, 2)
        assert result == 1

    def test_simple_case(self):
        input = [1, 2, 3]
        result = search_insert(input, 2)
        assert result == 1

    def test_recursive_halving(self):
        input = [1, 2, 3, 4, 5]
        result = search_insert(input, 2)
        assert result == 1

    def test_missing_value(self):
        input = [1, 3, 4, 5]
        result = search_insert(input, 2)
        assert result == 1

    def test_missing_value_2(self):
        input = [3, 6, 7, 8, 10]
        result = search_insert(input, 5)
        assert result == 1

    def test_outside_max(self):
        input = [1, 3, 4]
        result = search_insert(input, 5)
        assert result == 3

    def test_outside_min(self):
        input = [1, 3, 4]
        result = search_insert(input, 0)
        assert result == 0

    def test_multiple_values_right_half(self):
        input = [2, 7, 8, 9, 10]
        result = search_insert(input, 9)
        assert result == 3
