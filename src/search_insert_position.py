def search_insert(nums: list[int], target: int) -> int:
    left: int = 0
    right: int = len(nums)
    while right - left > 0:
        idx: int = (left + right) // 2
        if nums[idx] >= target:
            right = idx
        else:
            left = idx + 1
    return right
