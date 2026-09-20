class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        times=set()
        for num in nums:
            if num in times:
                return True 
            times.add(num)
        return False