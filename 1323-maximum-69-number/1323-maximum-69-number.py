class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        s=""
        c=0
        for i in num:
            if i=="6" and c==0:
                s+="9"
                c=1
            else:
                s+=i
        return int(s)