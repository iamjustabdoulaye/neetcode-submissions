import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outnum=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
                outnum[i]=prefix
                prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            outnum[i]*=suffix
            suffix*=nums[i]     
        return outnum