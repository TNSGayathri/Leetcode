class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        power_of_5 = 5
        while n >= power_of_5:
            count += n // power_of_5
            power_of_5 *= 5
        return count
