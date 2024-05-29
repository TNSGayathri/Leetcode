class Solution:
    def numSteps(self, s: str) -> int:
        
        count=0
        p=1
        c=0
        for i in s[::-1]:
            if i=="1":
                count+=p
            p=p*2
        # return p
        if count==1:
            return 0
        while count>1:
            if(count%2==0):
                count=count//2
            else:
                count+=1
            c+=1
        return c
            