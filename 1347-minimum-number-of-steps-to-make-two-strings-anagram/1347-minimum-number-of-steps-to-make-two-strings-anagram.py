class Solution(object):
    def minSteps(self, n,m):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        def dic(n):
            d={}
            for i in n:
                if(i in d.keys()):
                    d[i]+=1
                else:
                    d[i]=1
            return d
        c=0
        l=dic(n)
        k=dic(m)
        for i in k:
            if(i in l and k[i]>l[i]):
                c+=k[i]-l[i]
            elif(i not  in l):
                c+=k[i]
        return c
