class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
                m=0
                n=len(nums)
                d={}
                i=0
                j=0
                while i <n and j<n:
                    if nums[j] not in d:
                        d[nums[j]]=1
                        j+=1
                    elif nums[j] in d and d[nums[j]]<1:
                        d[nums[j]]+=1
                        j+=1
                    else:
                        # print(j,i)
                        m=max(m,(j-i))
                        d[nums[i]]-=1
                        i+=1
                # print(" ")
                m=max(m,(j-i))
                return m

        