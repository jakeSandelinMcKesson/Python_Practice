class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for a, num in enumerate(nums):
            if num == nums[a - 1] and a > 0:
                continue

            l = a + 1
            r = len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]
                if total == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l != r:
                        l+= 1
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                
        return res

