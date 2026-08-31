from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=Counter(nums)
        a=[]
        for i,f in n.most_common(k):
            a.append(i)
        return a
        