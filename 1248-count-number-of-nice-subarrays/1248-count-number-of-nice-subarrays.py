class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        c=0
        totalcount=0
        while j<len(nums):
            if(nums[j]%2!=0):
                c+=1
            while c> k:
                if nums[i] % 2 != 0:
                    c -= 1
                i += 1

            if c == k:
                tempi = i
                while tempi <= j and nums[tempi] % 2 == 0:
                    tempi += 1
                totalcount += tempi - i + 1
            j+=1

        return totalcount