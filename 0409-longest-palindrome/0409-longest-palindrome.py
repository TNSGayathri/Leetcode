class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=list(d.values())
        e=[]
        o=[]
        for i in l:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        if(o==[]):
            return sum(e)
        o.sort()
        s=sum(e)
        for i in o:
            s+=i-1
        return s+1