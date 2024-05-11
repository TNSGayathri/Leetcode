class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume=length*width*height
        b=0
        h=0
        if(length>=10000 or width>=10000 or height>=10000 or volume>=1000000000):
            b=1
        if(mass>=100):
            h=1
        if(b==1 and h==1):
            return "Both"
        elif(b==0 and h==0):
            return "Neither"
        elif(b==1 and h==0 ):
            return "Bulky"
        elif(b==0 and h==1):
            return "Heavy"
        