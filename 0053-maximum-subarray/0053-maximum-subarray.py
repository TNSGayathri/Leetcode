class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma=-99999999
        maxi=0
        for i in range(0,len(nums)):
            maxi=maxi+nums[i]
            if ma<maxi:
                ma=maxi
            if maxi<0:
                maxi=0
        return ma