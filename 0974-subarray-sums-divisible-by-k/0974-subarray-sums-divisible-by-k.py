class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        pre=0
        c=0
        for i in range(0,len(nums)):
            pre=pre+nums[i]
            r=pre%k
            # if r<0:
            #     r+=k
            if r in d:
                c+=d[r]
            if pre%k in d:
                d[pre%k]+=1
            else:
                d[pre%k]=1
        return c
        