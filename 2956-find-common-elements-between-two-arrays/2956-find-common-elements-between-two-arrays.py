class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in nums1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d1={}
        for i in nums2:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        s=0
        nums1=list(set(nums1))
        for i in nums1:
            if i in d1:
                # print(i)
                s+=d1[i]
        s1=0
        nums2=list(set(nums2))
        for i in nums2:
            if i in d:
                s1+=d[i]
        return [s1,s]