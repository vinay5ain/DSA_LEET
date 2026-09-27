class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                temp = []

                while stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop()  # remove '('

                for c in temp:
                    stack.append(c)

        return ''.join(stack)