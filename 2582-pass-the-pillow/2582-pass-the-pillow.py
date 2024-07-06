class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        if(time<=n-1):
            return time+1
        m=[]
        for i in range(1,n+1):
            m.append(i)
        time-=n
        while time>n-1:
            m=m[::-1]
            time-=n-1
        m=m[::-1]
        # print(m,time)
        if(time==n-1):
            return m[time-1]
        return m[time+1]