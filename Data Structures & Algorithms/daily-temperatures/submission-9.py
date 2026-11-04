class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        temps_len = len(temperatures)
        results = []
        if len(set(temps)) == 1:
            return [0] * temps_len
        for i in range(temps_len):
            count = 0
            for j in range(i+1, temps_len, 1):
                if temps[i] >= temps[j]:
                    continue
                count = j - i
                break
            results.append(count)
        return results