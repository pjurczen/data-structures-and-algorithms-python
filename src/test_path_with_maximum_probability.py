import unittest

from path_with_maximum_probability import PathWithMaximumProbability


class TestPathWithMaximumProbability(unittest.TestCase):

    def test_small_case(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.2]
        start = 0
        end = 2
        testee = PathWithMaximumProbability()
        result = testee.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(result, 0.25000)

    def test_other_case(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.3]
        start = 0
        end = 2
        testee = PathWithMaximumProbability()
        result = testee.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(result, 0.30000)

    def test_negative_case(self):
        n = 3
        edges = [[0, 1]]
        succProb = [0.5]
        start = 0
        end = 2
        testee = PathWithMaximumProbability()
        result = testee.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(result, 0.00000)


if __name__ == "__main__":
    unittest.main()
