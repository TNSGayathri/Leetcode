class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        s=s[::-1]
        total=0
        prv=0
        for i in s:
            v=r[i]
            if(v<prv):
                total-=v
            else:
                total+=v
                prv=v
        return total