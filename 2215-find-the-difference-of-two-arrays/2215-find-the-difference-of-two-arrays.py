class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[]
        n=[]
        m=[]
        for i in nums1:
            if i not in n and i not in nums2:
                n.append(i)
        ans.append(n)
        for i in nums2:
            if i not in m and i not in nums1:
                m.append(i)
        ans.append(m)
        return ans