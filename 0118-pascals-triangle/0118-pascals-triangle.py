class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[]
        for i in range(numRows):
            if(i!=0):
                l.append([1,1])
            else:
                l.append([1])
        for i in range(2,numRows):
            k=1
            for j in range(len(l[i-1])-1):
                l[i].insert(k,l[i-1][j]+l[i-1][j+1])
                k+=1
                
        return l
    
        