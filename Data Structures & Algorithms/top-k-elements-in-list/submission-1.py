class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = {}
        for i in nums:
            if i in h:
                h[i] = h[i] + 1
            else:
                h.update({i : 1})
        
        l = list(h.items())
        for i in range(len(l) - 1):
            j = 0
            for j in range(i+1, len(l)):
                if l[i][1] < l[j][1]:
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp
        return [l[i][0] for i in range(k)]