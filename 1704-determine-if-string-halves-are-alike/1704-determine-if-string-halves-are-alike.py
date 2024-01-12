class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k="aeiouAEIOU"
        c,c1=0,0
        a=len(s)//2
        for i in range(a):
            if(s[i] in k):
                c+=1
        for i in range(a,len(s)):
            if(s[i] in k):
                c1+=1
        if(c1==c):
            return True
        return False