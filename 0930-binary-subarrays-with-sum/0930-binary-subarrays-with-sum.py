from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, l: List[int], s: int) -> int:
        pre=defaultdict(int)
        c=0
        x=0
        for i in l:
            x+=i
            if x==s:
                c+=1
            if x-s in pre:
                c+=pre[x-s]
            pre[x]+=1
        return c
            