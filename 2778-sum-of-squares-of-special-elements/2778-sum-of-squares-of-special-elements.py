class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(1,n+1):
            if n%i==0:
                c+=nums[i-1]*nums[i-1]
                # print(i,nums[i-1])
        return c
        