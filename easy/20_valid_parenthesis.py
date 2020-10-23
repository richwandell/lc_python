class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            elif ch == "}":
                prev = stack.pop()
                if prev != "{":
                    return False
            elif ch == "]":
                prev = stack.pop()
                if prev != "[":
                    return False
            elif ch == ")":
                prev = stack.pop()
                if prev != "(":
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
print(s.isValid("("))
print(s.isValid("(("))