class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num<=9):
            return num
        while num>9:
            s=0
            while num>0:
                r=num%10
                s+=r
                num=num//10
            num=s
        return s
            
        