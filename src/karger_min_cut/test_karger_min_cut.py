from unittest import TestCase

from src.karger_min_cut.graph import Graph
from src.karger_min_cut.karger_min_cut import KargerMinCut
from src.karger_min_cut.utility import create_graph_from_file
from src.karger_min_cut.vertex import VertexKey, Vertex


class TestKargerMinCut(TestCase):

    def test_random_choice(self):
        # given
        graph = create_graph_from_file('smallTestCase.txt')
        testee = KargerMinCut(graph)
        # when
        u, v = testee.pick_random_edge()
        # then
        self.assertIsInstance(u, VertexKey)
        self.assertIsInstance(v, VertexKey)

    def test_merge(self):
        # given
        graph = Graph()
        vertex_1 = Vertex(VertexKey(1))
        vertex_1.add_neighbour(VertexKey(2))
        graph.add_vertex(vertex_1)

        vertex_2 = Vertex(VertexKey(2))
        vertex_2.add_neighbour(VertexKey(1))
        vertex_2.add_neighbour(VertexKey(3))
        vertex_2.add_neighbour(VertexKey(3))
        graph.add_vertex(vertex_2)

        vertex_3 = Vertex(VertexKey(3))
        vertex_3.add_neighbour(VertexKey(2))
        vertex_3.add_neighbour(VertexKey(2))
        graph.add_vertex(vertex_3)

        testee = KargerMinCut(graph)
        # when
        testee.merge(VertexKey(1), VertexKey(2))
        u = graph.get_vertex(VertexKey(1))
        v = graph.get_vertex(VertexKey(3))
        # then
        self.assertNotIn(VertexKey(2), graph.vertices)
        self.assertEqual({VertexKey(1): 1, VertexKey(3): 2}, u.neighbours)
        self.assertEqual({VertexKey(1): 2}, v.neighbours)

    def test_remove_self_loop(self):
        # given
        graph = Graph()
        vertex_1 = Vertex(VertexKey(1))
        vertex_1.add_neighbour(VertexKey(2))
        vertex_1.add_neighbour(VertexKey(1))
        graph.add_vertex(vertex_1)

        testee = KargerMinCut(graph)
        # when
        testee.remove_self_loop(VertexKey(1))
        u = graph.get_vertex(VertexKey(1))
        # then
        self.assertNotIn(VertexKey(1), u.neighbours)
        self.assertEqual({VertexKey(2): 1}, u.neighbours)

    def test_remove_self_loop_no_loop(self):
        # given
        graph = Graph()
        vertex_1 = Vertex(VertexKey(1))
        vertex_1.add_neighbour(VertexKey(2))
        graph.add_vertex(vertex_1)

        testee = KargerMinCut(graph)
        # when
        testee.remove_self_loop(VertexKey(1))
        u = graph.get_vertex(VertexKey(1))
        # then
        self.assertNotIn(VertexKey(1), u.neighbours)
        self.assertEqual({VertexKey(2): 1}, u.neighbours)

    def test_small_case(self):
        # given
        graph = create_graph_from_file('smallTestCase.txt')
        testee = KargerMinCut(graph)
        # when
        result = testee.find_min_cut()
        # then
        self.assertEqual(2, result)

    def test_input_file(self):
        # given
        graph = create_graph_from_file('kargerMinCut.txt')
        testee = KargerMinCut(graph)
        # when
        result = testee.find_min_cut()
        # then
        self.assertEqual(17, result)