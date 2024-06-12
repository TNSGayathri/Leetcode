class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if(len(set(nums))<3):
            return False
        t=-999999999999
        s=[]
        for i in nums[::-1]:
            if i<t:
                return True
            while s and s[-1]<i:
                t=s.pop()
            s.append(i)
        return False