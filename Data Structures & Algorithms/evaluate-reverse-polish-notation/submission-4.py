class Solution:

    def compute(self, f_n: int, s_n: int, operator: str):
        match operator:
            case "+":
                return f_n + s_n
            case "-":
                return f_n - s_n
            case "*":
                return f_n * s_n
            case "/":
                return f_n / s_n

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for c in tokens:
            if c in operators:
                s_n = stack.pop()
                f_n = stack.pop()
                result = int(self.compute(f_n, s_n, c))
                stack.append(result)
            else:
                n = int(c)
                stack.append(n)

        return stack[-1]