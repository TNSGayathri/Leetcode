class Solution:
    def digitCount(self, num: str) -> bool:
        d={}
        m=max(num)
        for i in range(int(m)+1):
            d[str(i)]=0
        for i in num:
            d[i]+=1
        
        for i in range(len(num)):
            if(str(i) in d and d[str(i)]!=int(num[i])):
                return False
        return True