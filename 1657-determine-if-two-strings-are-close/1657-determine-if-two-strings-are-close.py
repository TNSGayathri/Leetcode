class Solution(object):
    def closeStrings(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        def dic(w):
            d={}
            for i in w:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            return d
        if(len(w1)!=len(w2)):
            return False
        else:
            c2=dic(w1)
            v2=dic(w2)
            c1=list(c2.keys())
            c=list(c2.values())
            c.sort()
            c1.sort()
            c1="".join(c1)
            v=list(v2.values())
            v1=list(v2.keys())
            v1.sort()
            v.sort()
            v1="".join(v1)
            if(c==v and c1==v1):
                return True
            else:
                return False