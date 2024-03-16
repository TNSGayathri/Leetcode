class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        ma=0
        d={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                c-=1
            else:
                c+=1
            if c in d:
                ma=max(ma,i-d[c])
            else:
                d[c]=i
        return ma
        