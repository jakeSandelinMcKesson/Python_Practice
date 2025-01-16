class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)

        i = 1
        lastNum = None
        longest = 0

        for num in sortedNums:
            if lastNum == None:
                lastNum = num
                longest = i
                continue
            elif lastNum == num:
                continue
            elif num - lastNum == 1:
                i+=1
                lastNum = num
                if i > longest:
                    longest = i
            else:
                i = 1
                lastNum = num
        return longest
            