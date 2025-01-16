class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = defaultdict(int)

        for num in nums:
            if num in topK:
                #topK(num) = topK(num) + 1
                topK.update({num:topK[num]+1})
            else:
                topK[num] = 1
        ordered = sorted(topK.items(), key=lambda item: item[1], reverse=True)

        return [num[0] for num in ordered[:k]]