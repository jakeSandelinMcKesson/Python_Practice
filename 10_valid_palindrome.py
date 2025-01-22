class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        r = ''

        for l in s:
            if l.isalnum():
                t += l.lower()
                r = l.lower() + r
        if t == r:
            return True
        else:
            return False