class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l=[]
        s=0
        for i in num:
            s=s*10+i
        c=s+k
        while c>0:
            r=c%10
            l.append(r)
            c=c//10
        return l[::-1]