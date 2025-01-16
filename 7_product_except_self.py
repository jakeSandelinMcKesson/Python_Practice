class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        has0 = 0
        for num in nums:
            if num == 0:
                has0 += 1
            else:
                product *= num
        
        res = []

        for num in nums:
            if has0 == 1:
                if num == 0:
                    res.append(int(product))
                else: 
                    res.append(0)
            elif has0 > 1:
                res.append(0)
            else:
                res.append(product//num)
        return res