class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend==-2147483648 and divisor==-1):
            return 2147483647
        if(dividend*divisor<0):
            dividend=abs(dividend)
            divisor=abs(divisor)
            c=dividend//divisor
            return c*-1
        return dividend//divisor
        