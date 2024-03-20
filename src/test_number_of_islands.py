import unittest
from numbers_of_islands import NumberOfIslands

class TestNumberOfIslands(unittest.TestCase):

    def test_small_case(self):
        input = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        testee = NumberOfIslands()
        result = testee.numIslands(input)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
