import unittest

from find_critical_and_pseudo_critical_edges import FindCriticalAndPseudoCriticalEdges


class TestFindCriticalAndPseudoCriticalEdges(unittest.TestCase):

    def test_small_case(self):
        n = 5
        edges = [
            [0, 1, 1],
            [1, 2, 1],
            [2, 3, 2],
            [0, 3, 2],
            [0, 4, 3],
            [3, 4, 3],
            [1, 4, 6],
        ]
        testee = FindCriticalAndPseudoCriticalEdges()
        result = testee.findCriticalAndPseudoCriticalEdges(n, edges)
        self.assertEqual(result, [[0, 1], [2, 3, 4, 5]])

    def test_big_case(self):
        n = 4
        edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
        testee = FindCriticalAndPseudoCriticalEdges()
        result = testee.findCriticalAndPseudoCriticalEdges(n, edges)
        self.assertEqual(result, [[], [0, 1, 2, 3]])


if __name__ == "__main__":
    unittest.main()
