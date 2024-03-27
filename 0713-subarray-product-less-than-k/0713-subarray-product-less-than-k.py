class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p=1
        c=0
        j=0
        for i in range(len(nums)):
            p*=nums[i]
            while j<i and p>=k:
                p=p//nums[j]
                j+=1
            if(p<k):
                c+=(i-j)+1
        return c
                
        