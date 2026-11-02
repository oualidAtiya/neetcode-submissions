class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            ']': '[',
            ')':'(',
            '}':'{'
        }
        stack = []
        for c in s:
            if c in h.values():
                stack.append(c)
                continue
            if stack and stack[-1] != h[c]:
                return False
            elif not stack and c in h:
                return False
            elif stack:
                stack.pop()
        if stack:    
            return False
        return True