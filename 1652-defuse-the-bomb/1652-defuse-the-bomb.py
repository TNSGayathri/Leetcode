class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l=[]
        if(k==0):
            l=[0]*len(code)
        elif(k>0):
            for i in range(len(code)):
                if(i+k<len(code)):
                    l.append(sum(code[i+1:i+k+1]))
                else:
                    l.append(sum(code[i+1:])+sum(code[:(i+k)%len(code)+1:]))
        elif(k<0):
            for i in range(len(code)):
                if(i+k>=0):
                    # print(code[i],code[i-1:i+k-1:-1])
                    l.append(sum(code[i+k:i:]))
                else:
                    # print(code[i],code[i-1:-1:-1],code[i+k::])
                    l.append(sum(code[:i:])+sum(code[i+k::]))
        return l