class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=0
        j=0
        m=[]
        nums1.sort()
        nums2.sort()
        while i<len(nums1) and j<len(nums2):
            if (nums1[i]<nums2[j]):
                i+=1
            elif(nums2[j]<nums1[i]):
                j+=1
            else:
                m.append(nums1[i])
                i+=1
                j+=1
        return m
        