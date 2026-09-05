class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        max_count=0
        left=0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[left])
                left+=1
            a.add(s[i])
            max_count=max(max_count,i-left+1)
        return max_count
            

        