from unittest import TestCase

from numpy.testing import assert_equal

from closest_pair import Point, ClosestPair


class TestClosestPair(TestCase):
    def test_find_closest_pair(self):
        # given
        p = [Point(x=2, y=3), Point(x=39, y=51), Point(x=12, y=30),
             Point(x=40, y=50), Point(x=5, y=1), Point(x=12, y=10), Point(x=3, y=4),
             Point(x=4, y=3), Point(x=1, y=3),
             Point(x=40, y=50), Point(x=40, y=51), Point(x=40, y=49)
             ]
        testee = ClosestPair()
        # when
        result = testee.find_closest_pair(p)
        # then
        assert_equal(result, (Point(x=39, y=51), Point(x=40, y=51)))
