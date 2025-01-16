class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = sorted(s)
        t2 = sorted(t)
        
        if len(s2) != len(t2):
            return False 

        for x in range(len(s2)):
            if s2[x] != t2[x]:
                return False
        return True