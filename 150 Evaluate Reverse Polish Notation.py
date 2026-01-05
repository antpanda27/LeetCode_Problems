class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    temp = a + b
                elif token == "-":
                    temp = a - b
                elif token == "*":
                    temp = a * b
                elif token == "/":
                    temp = int(a / b)
                stack.append(temp)
            else:
                stack.append(int(token))
        return stack[0]