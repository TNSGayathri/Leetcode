class Solution(object):
    def runningSum(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        l=[]
        for i in arr:
            s+=i
            l.append(s)
        return l
            
        