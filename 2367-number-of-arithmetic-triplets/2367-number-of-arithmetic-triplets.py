class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    m=[nums[i],nums[j],nums[k]]
                    m.sort()
                    if(nums[j]-nums[i]==diff and nums[k]-nums[j]==diff and m not in l):
                        l.append(m)
        return len(l)
                        