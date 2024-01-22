from unittest import TestCase

from numpy.testing import assert_equal

from src.local_minimum import LocalMinimum


class TestLocalMinimum(TestCase):
    def test_local_minimum_exists(self):
        # given
        data = [[20, 24, 25, 11, 10],
                [19, 22, 13, 3, 9],
                [18, 17, 23, 21, 8],
                [12, 16, 15, 7, 2],
                [14, 5, 1, 6, 4]]
        testee = LocalMinimum()
        # when
        result = testee.find_local_minimum(data)
        # then
        assert_equal(result, 3)
