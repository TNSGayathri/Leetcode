class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        l=[]
        s=(n*(n+1))//2
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                l.append(i)
                d[i]+=1
                
        s1=sum(list(d.keys()))
        l.append(abs(s1-s))
        return l
        
        