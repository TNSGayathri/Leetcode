class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        l=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
    
            else:
                d[nums[i]]+=1
        for i in d.keys():
            if(d[i]>2):
                while(d[i]!=2):
                    nums.remove(i)
                    d[i]-=1
        # print(nums)
        return len(nums)