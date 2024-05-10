from fractions import Fraction
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        l=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                l.append(float(arr[i])/float(arr[j]))
        l.sort()
        m=l[k-1]
        f = Fraction(m).limit_denominator()
        l1=[]
        l1.append(f.numerator)
        l1.append(f.denominator)
        return l1
        