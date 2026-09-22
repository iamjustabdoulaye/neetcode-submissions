class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # Product of everything to the LEFT
        prefix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        # Product of everything to the RIGHT
        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output