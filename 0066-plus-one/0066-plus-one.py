class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        m=""
        l=[]
        for i in digits:
            m+=str(i)
        s=int(m)+1
        print(s)
        while s:
            l.append(s%10)
            s=s//10
        return l[::-1]
