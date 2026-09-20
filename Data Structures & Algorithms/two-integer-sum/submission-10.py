class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outmap={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff in outmap:
                return [outmap[diff],i]
            outmap[n]=i

