class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        if(len(nums)<2):
            return 0
        nums.sort()
        for i in range(len(nums)-1):
            d=nums[i+1]-nums[i]
            l.append(d)
        return max(l)
        