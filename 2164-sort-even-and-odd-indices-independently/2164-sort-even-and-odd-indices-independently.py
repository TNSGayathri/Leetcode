class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if(len(nums)<=2):
            return nums
        l1=nums[:len(nums):2]
        l2=nums[1:len(nums):2]
        l1.sort()
        l=[]
        l2.sort(reverse=True)
        # print(l1,l2)
        for i in range(min(len(l1),len(l2))):
            l.append(l1[i])
            l.append(l2[i])
        i=i+1
        if i==len(l1):
            while i<len(l2):
                l.append(l2[i])
                i+=1
        if i==len(l2):
            while i<len(l1):
                l.append(l1[i])
                i+=1
        return l
        