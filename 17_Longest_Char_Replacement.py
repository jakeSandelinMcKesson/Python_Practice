class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 
        maxF = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxF = max(maxF,count[s[r]])
            #print(count[s[r]])

            if (r-l+1) - maxF > k:
                count[s[l]] = count.get(s[l],0) - 1
                l += 1
            
            res = max(res,(r-l+1))

        return res