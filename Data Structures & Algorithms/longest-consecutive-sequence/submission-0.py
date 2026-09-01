class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a=list(set(nums))
        a.sort()
        b=len(a)
        count=1
        max_count=1

        for i in range(b):
            if a[i]-a[i-1]==1:
                count+=1
                max_count=max(count,max_count)
            else:
                count=1
        
        return max_count