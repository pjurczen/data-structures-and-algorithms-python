from unittest import TestCase

from src.lru_cache import LRUCache


class TestLruCache(TestCase):

    def test_complex_case(self):
        operations = ["LRUCache", [3], "put", [1, 1], "put", [2, 2], "put", [3, 3], "get", [1], "get", [2], "get", [4],
                      "put", [4, 4], "get", [1], "get", [2], "get", [3], "get", [4], "get", [2], "put", [1, 8], "put",
                      [3, 7], "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get", [2], "get", [3], "get",
                      [4],
                      "put", [1, 9], "put", [6, 6], "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get",
                      [6]]

        expected_output = [None, None, None, None, 1, 2, -1, None, 1, 2, -1, 4, 2, None, None, 8, 2, 7, -1, -1, 2, 7,
                           -1, None, None, 9, -1, 7, -1, -1, 6]

        testee = LRUCache(*operations[1])
        actual_output = [None]
        for i in range(1, len(operations) // 2):
            op = operations[2 * i]
            arguments = operations[2 * i + 1]
            method = getattr(testee, op)
            result = method(*arguments)
            actual_output.append(result)

        self.assertEqual(expected_output, actual_output)
