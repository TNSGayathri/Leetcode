class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m=max(nums)
        ans=s=mw=0
        for i in range(len(nums)):
            if nums[i]==m:
                mw+=1
            while mw==k:
                if nums[s]==m:
                    mw-=1
                s+=1
            ans+=s
        return ans
        