class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        for i in range(0,len(nums)):
            x=x^i+1
            x=x^nums[i]
        return x