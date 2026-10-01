from unittest import TestCase

from src.longest_common_subsequence import Solution


class TestLongestCommonSubsequence(TestCase):

    def test_simple_case(self):
        text1 = "cat"
        text2 = "crabt"

        testee = Solution()

        assert testee.longestCommonSubsequence(text1, text2) == 3

    def test_other_case(self):
        text1 = "psnw"
        text2 = "vozsh"

        testee = Solution()

        assert testee.longestCommonSubsequence(text1, text2) == 1
