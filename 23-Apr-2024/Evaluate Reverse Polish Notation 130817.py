# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                 stack.append(stack.pop(-2) - stack.pop(-1))
            elif token == "*":
                 stack.append(stack.pop() * stack.pop())
            elif token == "/":
                 stack.append(int(stack.pop(-2) / stack.pop(-1)))
            else:
                stack.append(int(token))
        return stack.pop()