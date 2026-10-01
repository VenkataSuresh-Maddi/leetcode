class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)

            elif char in ')}]' and len(stack) == 0:
                return False

            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ')' and stack[-1] != '(':
                return False

            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == '}' and stack[-1] != '{':
                return False

            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == ']' and stack[-1] != '[':
                return False

        if len(stack) == 0:
            return True
        elif len(stack) > 0:
            return False