class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r)//2
            if nums[m] < target:
                l = m  + 1 # I already checked m, so I should move this to the right one
            elif nums[m] > target:
                r = m - 1 # same as above
            elif nums[m] == target:
                return m
        return -1