class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        x=0
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d.keys():
            if d[i]>=2:
                x=x^i
        return x
        