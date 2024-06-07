class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nu=str(num)
        c=0
        i=0
        j=k-1
        while i<=(len(nu)-k):
            # print(nu[i:j+1:])
            ku=int(nu[i:j+1:])
            if(ku !=0 and num%ku==0):
                c+=1
            i+=1
            j+=1
        return c
            