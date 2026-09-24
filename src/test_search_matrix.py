from unittest import TestCase

from src.search_matrix import Solution


class TestSearchMatrix(TestCase):

    def test_middle_left_side(self):
        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 10
        testee = Solution()

        result = testee.searchMatrix(matrix, target)

        assert result is True
