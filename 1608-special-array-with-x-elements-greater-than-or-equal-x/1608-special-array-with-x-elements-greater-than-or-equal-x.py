class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        l=[]
        for i in range(n):
            c=0
            for j in nums:
                if j >i:
                    c+=1
            l.append(c)
        # print(l)
        for i in range(n):
            if i+1==l[i]:
                return i+1
        return -1
            