class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] = h[i] + 1
            else:
                h.update({i : 1})
        
        l = sorted(h.items(), key=lambda x: x[1], reverse=True) 
        return [l[i][0] for i in range(k)]