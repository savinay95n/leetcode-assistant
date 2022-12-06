class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_dict = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in para_dict:
                stack.append(c)
            elif stack and c == para_dict[stack[-1]]:
                stack.pop()
            else:
                return False
        if not stack:
            return True