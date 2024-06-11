class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
                m=0
                n=len(nums)
                d={}
                i=0
                j=0
                while j<n:
                    if nums[j] not in d:
                        d[nums[j]]=j
                    elif nums[j] in d:
                        m=max(m,(j-i))
                        i=max(i,d[nums[j]]+1)
                        d[nums[j]]=j
                    j+=1
                if(m==0):
                    return n
                m=max(m,j-i)
                return m

        