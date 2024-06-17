class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        # l=[]
        for i in range(len(arr)):
            l=[arr[i]]
            s+=arr[i]
            for j in range(i+1,len(arr)):
                l.append(arr[j])
                if(len(l)%2!=0):
                    s+=sum(l)
        return s