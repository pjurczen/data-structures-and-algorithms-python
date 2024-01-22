from unittest import TestCase

from numpy.testing import assert_equal

from src.index_is_value import IndexIsValue


class TestIndexIsValue(TestCase):
    def test_index_is_value(self):
        # given
        sorted_num = [-2, 0, 1, 3, 5, 7, 9]
        testee = IndexIsValue()
        # when
        result = testee.index_is_value(sorted_num, 0, len(sorted_num))
        # then
        assert_equal(result, 0)
