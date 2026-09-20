# Alternative O(1)-space solution to 169. Majority Element.
#
# Boyer-Moore (see majority_element.py) is the better answer for this problem:
# one pass instead of 32. This version exists because the underlying technique --
# counting a FIXED-SIZE set of properties instead of unbounded values -- is the
# standard solution to 137. Single Number II, where no cancellation trick applies.
#
# Idea
# ----
# O(1) space forbids a counter per distinct value (there are ~4 billion of them).
# But every int is also 32 yes/no facts: "is bit b set?". 32 is a constant, so
# one counter per bit IS affordable.
#
# For any bit position b, split the array into the majority element's copies and
# everything else. All the majority's copies are the same number, so they share
# every bit -- they contribute either all or nothing to column b:
#
#   majority's bit b is 1 -> it alone contributes > n/2 ones. Threshold cleared
#                            regardless of the other elements.
#   majority's bit b is 0 -> it contributes nothing, and everything else combined
#                            is < n/2. Threshold unreachable.
#
# So "column count > n // 2" is an exact read-out of the majority's bit b, and
# the 32 verdicts spell out the answer.
#
# Two's complement / Python
# -------------------------
# Reading bits needs no special handling: Python's (v >> b) & 1 already yields
# the two's-complement bit, matching a real int32 for every value in range.
#
# Rebuilding does. Python integers are unbounded, so a value assembled from bits
# 0..31 is always POSITIVE -- the infinite leading 1s that marked a negative
# number are gone. What we hold is a POSITION on a 2**32 wheel, not a value.
# Decoding a position is the same rule as in a 4-bit box (13 -> 13 - 16 = -3):
# top bit set means the second half of the wheel, so subtract the wheel size.
#
# Valid while every input fits in signed 32 bits. LeetCode's constraint is
# -10**9 .. 10**9; int32 reaches +-2_147_483_648, so it holds.
#
# Time:  O(32n) = O(n)  -- 32 passes, ~55x slower than Boyer-Moore in practice
# Space: O(1)           -- one counter plus the accumulating pattern

WIDTH = 32
WHEEL = 1 << WIDTH  # 2**32, the number of positions
SIGN_BIT = WIDTH - 1  # bit 31


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        threshold = len(nums) // 2
        pattern = 0

        # decide each bit independently; no column is compared to any other
        for bit in range(WIDTH):
            ones = 0
            for num in nums:
                ones += (num >> bit) & 1
            if ones > threshold:
                pattern |= 1 << bit

        # pattern is a position on the wheel -- decode it into a signed value
        if (pattern >> SIGN_BIT) & 1:
            return pattern - WHEEL
        return pattern
