class Permutations:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return self.recurse(nums, 0)

    def recurse(self, nums: list[int], i: int) -> list[list[int]]:
        if i == len(nums):
            return [[]]
        permutations = self.recurse(nums, i + 1)
        result = []
        for p in permutations:
            for j in range(0, len(p)+1):
                perm = p.copy()
                perm.insert(j, nums[i])
                result.append(perm)
        return result
