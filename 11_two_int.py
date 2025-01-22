class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num2 = None

        for j, num in enumerate(numbers):
            num2 = target - num
            if num2 in numbers:
                return [j+1,numbers.index(num2)+1]
        
