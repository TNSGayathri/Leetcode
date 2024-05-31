class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=nums.count(0)
        n=c
        while n!=0:
            nums.remove(0)
            n-=1
        while c!=0:
            nums.append(0)
            c-=1
        