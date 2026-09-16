class Solution:

    # Naive approach:
    # - while True loop that iterates until some element doesn't hold the prefix
    # - during each iteration get character at index i from first word
    # - in each iteration iterate over all elements of strs and compare their character at idx i
    # - if we get through all elements add it to the prefix
    # - increment i at each iterations end
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i: int = 0
        prefix: str = ""
        first_str: str = strs[0]
        first_str_len = len(first_str)
        strs_len = len(strs)
        while first_str_len > i:
            curr_char: str = first_str[i]
            invalid_char: bool = False
            for j in range(1, strs_len):
                s = strs[j]
                if len(s) <= i or s[i] != curr_char:
                    invalid_char = True
                    break
            if invalid_char:
                break
            prefix += curr_char
            i += 1
        return prefix
