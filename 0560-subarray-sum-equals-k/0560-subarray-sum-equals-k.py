class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        pre=0
        cnt=0
        for i in range(len(nums)):
            pre+=nums[i]
            r=pre-k
            if( r in d):
                cnt+=d[r]
            if pre in d:
                d[pre]+=1
            else:
                d[pre]=1
        return cnt
                