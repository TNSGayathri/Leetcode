class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        t=numBottles
        while t>=numExchange:
            t-=numExchange
            numBottles+=1
            t+=1
            numExchange+=1
        return numBottles
            
        