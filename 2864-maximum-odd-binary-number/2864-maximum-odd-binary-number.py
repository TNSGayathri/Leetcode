class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        k=""
        l=[]
        for i in s:
            l.append(int(i))
        l.sort()
        
        for i in range(len(l)-2,-1,-1):
            k+=str(l[i])
        return k+"1"
        