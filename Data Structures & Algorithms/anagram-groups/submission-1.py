from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for i in strs:
            a[tuple(sorted(i))].append(i)
        return list(a.values())