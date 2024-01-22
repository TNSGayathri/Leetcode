class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[]
        m=[]
        for i in range(len(nums)):
            if(i+1 not in nums):
                l.append(i+1)
            if(nums[i] in m):
                l.insert(0,nums[i])
            elif(nums[i]not in m):
                m.append(nums[i])
        return l
        
        