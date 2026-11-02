class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {0: []}
        seq = 0
        sorted_nums = sorted(set(nums))
        for i in range(len(sorted_nums)):
            if not h[seq] or sorted_nums[i] - 1 == h[seq][-1]:
                seq = seq
            else:
                seq += 1
                h.update({seq: []})
            h[seq].append(sorted_nums[i])
        winner = max(h.items(), key=lambda item: len(item[1]))
        return len(winner[1])