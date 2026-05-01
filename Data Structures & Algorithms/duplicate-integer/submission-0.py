class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        d = {}
        for i in nums:
            if d.get(i):
                return True
            d[i] = 1
        return False