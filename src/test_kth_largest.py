from unittest import TestCase

from src.kth_largest import KthLargest


class TestKthLargest(TestCase):

    def test_simple_case(self):
        kthLargest: KthLargest = KthLargest(3, [1, 2, 3, 3])
        assert kthLargest.add(3) == 3
        assert kthLargest.add(5) == 3
        assert kthLargest.add(6) == 3
        assert kthLargest.add(7) == 5
        assert kthLargest.add(8) == 6

    def test_negative_numbers(self):
        kthLargest: KthLargest = KthLargest(3, [1000, -1000])
        assert kthLargest.add(0) == -1000
        assert kthLargest.add(2) == 0
        assert kthLargest.add(-3) == 0
        assert kthLargest.add(1000) == 2
