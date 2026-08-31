class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list=[1]*len(nums)
        for i in range(1,len(nums)):
            new_list[i]=nums[i-1]*new_list[i-1]
        k=1
        for i in range(len(nums)-2,-1,-1):
            k*=nums[i+1]
            new_list[i]=new_list[i]*k
        return new_list

        