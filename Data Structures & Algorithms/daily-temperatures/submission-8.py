class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        s = set(t)
        if len(s) == 1:
            return [0]* len(t)
        stack = []
        l = []
        i = 0
        while i < len(t):
            if not stack:
                stack.append(t[i])
                i += 1
            elif t[i] > stack[0]:
                l.append(len(stack))
                i += (-len(stack) + 1)
                stack.clear()
            elif i == len(t) - 1 and stack:
                l.append(0)
                i += (-len(stack) + 1)
                stack.clear()
            else:
                stack.append(t[i])
                i += 1
        l.append(0)

        return l

