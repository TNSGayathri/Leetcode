class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if nums[i]==x:
                l.append(i)
                
        # print(l)     
        m=[]
        for i in queries:
            if i>len(l):
                m.append(-1)
            else:
                m.append(l[i-1])
        return m
            