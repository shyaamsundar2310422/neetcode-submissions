from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b=defaultdict(list)
    

        for a in strs:
            count=[0]*26
            for ch in a:
                count[ord(ch)-ord('a')]+=1

            b[tuple(count)].append(a)
        
        return list(b.values())