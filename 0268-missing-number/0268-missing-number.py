class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        m=max(nums)
        for i in range(0,m+1):
            x=x^i
        for i in nums:
            x=x^i
        if(len(nums)==m+1 and x==0):
            return m+1
        else:
            return x