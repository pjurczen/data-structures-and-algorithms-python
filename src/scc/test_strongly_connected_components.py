import sys
from unittest import TestCase

from src.scc.strongly_connected_components import StronglyConnectedComponents


class TestStronglyConnectedComponents(TestCase):

    def test_small_scc(self):
        # given
        testee = StronglyConnectedComponents()
        # when
        result = testee.find_scc('small_example.txt')
        # then
        self.assertEqual(result, [3, 3, 3])

    def test_big_scc(self):
        # given
        sys.setrecursionlimit(300000)
        testee = StronglyConnectedComponents()
        # when
        result = testee.find_scc('scc.txt')
        print(result)
        # then
        self.assertEqual(result, [3, 3, 3, 3, 3])
