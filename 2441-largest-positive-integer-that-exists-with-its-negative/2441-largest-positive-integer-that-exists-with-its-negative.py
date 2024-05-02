class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i=len(nums)-1
        c=1
        while c==1 and i>=0:
            if(-(nums[i])in nums):
               c=0
               return nums[i]
            i-=1
        return -1