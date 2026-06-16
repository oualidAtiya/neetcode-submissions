class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1 for _ in range(n)]
        for i in range(n):
            product = 1
            new_array = nums[:i] + nums[i+1:]
            for j in  new_array:
                product *= j
            output[i] = product
        return output