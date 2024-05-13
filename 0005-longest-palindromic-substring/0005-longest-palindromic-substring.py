class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)<=1):
            return s
        str1=""
        for i in range(1,len(s)):
            l=i
            h=i
            while(s[l]==s[h]):
                l-=1
                h+=1
                if(l==-1or h==len(s)):
                    break
            pal=s[l+1:h:]
            if(len(pal)>len(str1)):
                str1=pal
            l=i-1
            h=i
            while(s[l]==s[h]):
                l-=1
                h+=1
                if(l==-1 or h==len(s)):
                    break
            pal=s[l+1:h:]
            if(len(pal)>len(str1)):
                str1=pal
        return str1
            
        
        