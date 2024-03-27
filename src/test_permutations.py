from unittest import TestCase

from numpy.testing import assert_equal

from permutations import Permutations


class TestPermutations(TestCase):

    def test_small_case(self):
        # given
        input = [1, 2, 3]
        testee = Permutations()
        expected = [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
        # when
        output = testee.permute(input)
        # then
        assert_equal(output, expected)
