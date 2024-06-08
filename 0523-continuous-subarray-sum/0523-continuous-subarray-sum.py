class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if(k==0):
            for i in range(1,len(nums)):
                if(num[i]==0 and nums[i-1]==0):
                    return True
            return False
        d={}
        d[0]=-1
        pre=0
        for i in range(len(nums)):
            pre=pre+nums[i]
            if(pre%k in d):
                if(i-(d[pre%k])>1):
                    return True
            else:
                d[pre%k]=i
        return False