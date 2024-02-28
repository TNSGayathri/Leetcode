class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[0]
        r=[0]
        m=[]
        for i in range(len(nums)-1):
            l.append(l[-1]+nums[i])
        for i in range(len(nums)-1,0,-1):
            r.append(r[-1]+nums[i])
        r=r[::-1]
        for i in range(len(nums)):
            m.append(abs(l[i]-r[i]))
        return m
        
        
        