class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=[0]*26
        d1=[0]*26
        for i in s:
            c=ord(i)-97
            d[c]+=1
        for i in t:
            c=ord(i)-97
            d1[c]+=1
        if(d==d1):
            return True
        return False

        
        
        