from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        max_count=0
        left=0

        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]]=1
            
            max_freq=max(count.values())

            if (i-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            max_count=max(max_count,i-left+1)
        return max_count
        