class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        lmax=height[0]
        su=0
        j=len(height)-1
        rmax=height[j]
        while(i<j):
            if lmax<=rmax:
                su+=lmax-height[i]
                i+=1
                lmax=max(lmax,height[i])
            else:
                su+=rmax-height[j]
                j-=1;
                rmax=max(rmax,height[j])
        return su
        