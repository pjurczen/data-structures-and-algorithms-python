import unittest

from network_delay_time import NetworkDelayTime


class TestNetworkDelayTime(unittest.TestCase):

    def test_small_case(self):
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2
        testee = NetworkDelayTime()
        result = testee.networkDelayTime(times, n, k)
        self.assertEqual(result, 2)
    
    def test_negative_case(self):
        times = [[1,2,1]]
        n = 2
        k = 2
        testee = NetworkDelayTime()
        result = testee.networkDelayTime(times, n, k)
        self.assertEqual(result, -1)
    
    def test_another_case(self):
        times = [[1,2,1], [2,1,3]]
        n = 2
        k = 2
        testee = NetworkDelayTime()
        result = testee.networkDelayTime(times, n, k)
        self.assertEqual(result, 3)
    
    def test_another_case_shorter_path(self):
        times = [[1,2,1],[2,3,2],[1,3,4]]
        n = 3
        k = 1
        testee = NetworkDelayTime()
        result = testee.networkDelayTime(times, n, k)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
