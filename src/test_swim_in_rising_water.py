import unittest

from swim_in_rising_water import SwimInRisingWater


class TestSwimInRisingWater(unittest.TestCase):

    def test_small_case(self):
        grid = [[0, 2], [1, 3]]
        testee = SwimInRisingWater()
        result = testee.swimInWater(grid)
        self.assertEqual(result, 3)

    def test_big_case(self):
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        testee = SwimInRisingWater()
        result = testee.swimInWater(grid)
        self.assertEqual(result, 16)


if __name__ == "__main__":
    unittest.main()
