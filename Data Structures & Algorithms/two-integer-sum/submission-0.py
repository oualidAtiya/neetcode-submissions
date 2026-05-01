class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, n in enumerate(nums):
            if target - n in h:
                return [h[target - n], i]
            h[n] = i