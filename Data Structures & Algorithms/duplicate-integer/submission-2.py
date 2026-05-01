class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True