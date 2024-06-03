class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=""
        k=0
        for i in nums:
            s+=str(i)
        for i in s:
            k+=int(i)
        return abs(k-sum(nums))
        