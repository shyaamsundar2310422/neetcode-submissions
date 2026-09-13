from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        n=Counter(nums)
        def custom_sort(x):
            return (n[x],-x)

        nums.sort(key=custom_sort)
        return nums