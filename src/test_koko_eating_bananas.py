from unittest import TestCase

from src.koko_eating_bananas import Solution


class TestKokoEatingBananas(TestCase):

    def test_middle_cas(self):
        piles = [3, 6, 7, 11]
        h = 8
        testee = Solution()

        result = testee.minEatingSpeed(piles, h)

        assert result == 4

    def test_big_number(self):
        piles = [312884470]
        h = 968709470
        testee = Solution()

        result = testee.minEatingSpeed(piles, h)

        assert result == 1
