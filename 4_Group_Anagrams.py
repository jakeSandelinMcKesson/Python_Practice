class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sort = "".join(sorted(s))
            if sort in groups:
                groups[sort].append(s)
            else:
                groups[sort] = [s]

        return groups.values()