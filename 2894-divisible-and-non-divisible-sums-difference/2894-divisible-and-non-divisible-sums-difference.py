class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        l=[]
        m1=[]
        for i in range(1,n+1):
            if i%m!=0:
                m1.append(i)
            else:
                l.append(i)
        return sum(m1)-sum(l)
                