import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        f=0
        for i in range(int(math.sqrt(c)+1)):
            b=math.sqrt(c-(i*i))
            if(b==int(b)):
                f=1
                break
        return f