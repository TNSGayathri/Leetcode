class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        l=[]
        if(nums.count(0)>=2):
            return [0]*len(nums)
        for i in range(0,len(nums)):
            if(nums[i]!=0):
                p=p*nums[i]
        if(0 in nums):
            for i in nums:
                if i!=0:
                    l.append(0)
                else:
                    l.append(p)
        else:
            for i in nums:
                l.append(p//i)
        return l
                