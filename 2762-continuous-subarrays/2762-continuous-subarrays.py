class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i=0
        c=0
        d={}
        for j in range(len(nums)):
            if nums[j] in d:
                d[nums[j]]+=1
            else:
                d[nums[j]]=1
            # print(d)
            while (max(d)-min(d))>2:
                k=nums[i]
                i+=1
                d[k]-=1
                if d[k]==0:
                    del d[k]
            c+=j-i+1
            # print(c)
        return c