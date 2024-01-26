import sys
from unittest import TestCase

from src.scc.strongly_connected_components import StronglyConnectedComponents
from src.scc.utils import create_graph_from_file


class TestStronglyConnectedComponents(TestCase):

    def test_small_scc(self):
        # given
        graph = create_graph_from_file('small_example.txt')
        testee = StronglyConnectedComponents()
        # when
        result = testee.find_scc(graph)
        # then
        self.assertEqual(result, [3, 3, 3])

    def test_big_scc(self):
        # given
        sys.setrecursionlimit(300000)
        graph = create_graph_from_file('scc.txt')
        testee = StronglyConnectedComponents()
        # when
        result = testee.find_scc(graph)
        print(result)
        # then
        self.assertEqual(result, [3, 3, 3, 3, 3])
