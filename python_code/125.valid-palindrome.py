class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for i in range(len(s)):
            if s[i].isalnum():
                new_s += s[i]
        p, q = 0, len(new_s) - 1
        while p < q:
            if new_s[p] != new_s[q]:
                return False
            p += 1
            q -= 1
        return True