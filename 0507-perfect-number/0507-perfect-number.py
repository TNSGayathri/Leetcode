class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if(num<=3):
            return False
            
        l=[]
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                if(i not in l  and num//i not in l):
                    l.append(i)
                    l.append(num//i)
        if(sum(l)+1==num):
            return True
        return False