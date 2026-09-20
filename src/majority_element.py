# more than n/2 times -> [n/2 + 1, n], if we find element with n//2 + 1 count then we're done
# what if we looked how far we've looked so far and only maintained candidates that are still viable
# at any location minCount would be:
# count + open >= min
# count + len - pos >= len//2 + 1
# count >= pos - ceil(len/2) + 1
# count >= i - ceil(len/2) + 2
# min_count = i - ceil(len/2) + 2
# candidates_count = max(1, pos // min_count)
# candidates_count = max(1, (i + 1) // (i - ceil(len/2) + 2))
# meaning counting candidates is bounded, but still linear to input length -> no chance to arrive at O(1) space

# O(1) solution is Boyer–Moore algorithm

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majorityCount = 0
        majorityElement = None
        for n in nums:
            if majorityElement is None:
                majorityCount = 1
                majorityElement = n
            elif n != majorityElement:
                majorityCount -= 1
                if majorityCount == 0:
                    majorityElement = None
            else:
                majorityCount += 1
        return majorityElement
