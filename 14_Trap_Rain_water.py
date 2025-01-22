class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = 0
        rMax = 0
        trap = 0
        r = len(height) -1
        res = []

        for l, num in enumerate(height):
            rMax = 0
            r = len(height) -1
            while l < r:
                rMax = max(rMax,height[r])
                r -= 1
            if l > 0:
                lMax = max(lMax,height[l-1])
             
            res.append(max(min(lMax,rMax)-num,0))
            trap += max(min(lMax,rMax)-num,0)
        print(res)
        return trap