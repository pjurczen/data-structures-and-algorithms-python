from unittest import TestCase

from src.longest_common_prefix import Solution


class TestLongestCommonPrefix(TestCase):

    def test_shared_prefix(self):
        strs = ["flower", "flow", "flight"]
        result = Solution().longestCommonPrefix(strs)
        assert result == "fl"

    def test_no_prefix(self):
        strs = ["dog", "racecar", "car"]
        result = Solution().longestCommonPrefix(strs)
        assert result == ""

    def test_shared_prefix_increasing_length(self):
        strs = ["flow", "flowing", "flower"]
        result = Solution().longestCommonPrefix(strs)
        assert result == "flow"

    def test_shared_prefix_decreasing_length(self):
        strs = ["ab", "a"]
        result = Solution().longestCommonPrefix(strs)
        assert result == "a"
