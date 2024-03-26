class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        l=[]
        for i in nums:
            if i>0:
                l.append(i)
        if(len(l)==0):
            return 1
        l=list(set(l))
        m=len(l)
        l.sort()
        for i in range(0,m):
            if i+1!=l[i]:
                return i+1
        return l[-1]+1
        
        