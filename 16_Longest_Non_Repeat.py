class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I originally had it where I was using a list. 
        #However a list when you do a search within it goes through your entire list.. 
        #This made my solution a (O)N^2 solution.. which seemed like a bad move when searching a 
        #set or dictionary could make it 
        res = {}
        chMax = 0
        l = 0

        for r in range(len(s)):
            if s[r] in res:
                l = max(res[s[r]] + 1,l) #replacing my old left marker to be just left of that character
                res[s[r]] = r
            print(l,r)
            res[s[r]] = r
            chMax = max((r - l)+1, chMax)

        return chMax
