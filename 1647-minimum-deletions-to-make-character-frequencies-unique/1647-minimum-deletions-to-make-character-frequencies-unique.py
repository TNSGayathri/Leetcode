class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        c=0
        for i in s:
            if i  not in d:
                d[i]=1
            else:
                d[i]+=1
        l=list(d.values())
        # print(l)
        k=[]
        for i in l:
            if i not in k:
                k.append(i)
            else:
                f=0
                while f!=1:
                    i-=1
                    c+=1
                    if(i<=0):
                        f=1
                    elif(i not in k):
                        k.append(i)
                        f=1
                print(k)
        return c
                    
        