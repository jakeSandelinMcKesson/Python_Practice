class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newList =[]

        for j, num in enumerate(nums):
            goal = target - num
            if goal == num:
                first_index = nums.index(goal)
                if goal in nums[first_index + 1:]:
                    second_index = nums.index(goal, first_index + 1)
                    return [first_index, second_index]
                else:
                    continue

            if goal in nums:
                return [j, nums.index(goal)]