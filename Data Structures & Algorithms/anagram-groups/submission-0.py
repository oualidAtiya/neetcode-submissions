class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        l = ["".join(sorted(s)) for s in strs]
        h = {s: [] for s in set(l)}
        for i, s in enumerate(l):
            h[s] = h[s] + [strs[i]]
        final = []
        for v in h.values():
            final.append(v)
        return final