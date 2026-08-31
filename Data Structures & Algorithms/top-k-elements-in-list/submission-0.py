from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=Counter(nums)
        return [x for x,f in n.most_common(k)]

        