class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outnum=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            outnum[i]=prefix
            prefix*=nums[i]
        postfix =1
        for i in range(len(nums)-1,-1,-1):
            outnum[i]*=postfix
            postfix*=nums[i]
            
        return outnum