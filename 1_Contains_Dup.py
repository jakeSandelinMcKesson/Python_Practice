#Contains Duplicate
#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = defaultdict(int)

        for num in nums:
            if num in numbers:
                return True
            numbers[num] = 1
        return False