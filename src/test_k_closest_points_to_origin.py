from unittest import TestCase

from src.k_closest_points_to_origin import Solution


class TestKClosestPointsToOrigin(TestCase):

    def test_small_case(self):
        # given
        input = [[0, 2], [2, 2]]
        k = 1
        testee = Solution()
        # when
        result = testee.kClosest(input, k)
        # then
        assert result == [[0, 2]]

    def test_right_side_case(self):
        # given
        input = [[4, 0], [6, 0], [1, 0], [2, 0], [3, 0]]
        k = 4
        testee = Solution()
        # when
        result = testee.kClosest(input, k)
        # then
        assert [1, 0] in result
        assert [2, 0] in result
        assert [3, 0] in result
        assert [4, 0] in result

    def test_right_side_case_2(self):
        # given
        input = [[4, 0], [6, 0], [2, 0], [3, 0], [1, 0]]
        k = 4
        testee = Solution()
        # when
        result = testee.kClosest(input, k)
        # then
        assert [1, 0] in result
        assert [2, 0] in result
        assert [3, 0] in result
        assert [4, 0] in result

    def test_negative_case(self):
        # given
        input = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        testee = Solution()
        # when
        result = testee.kClosest(input, k)
        # then
        assert [3, 3] in result
        assert [-2, 4] in result
