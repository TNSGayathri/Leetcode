class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # s=numBottles
        # while(numBottles>=numExchange):
        #     empty=numBottles%numExchange
        #     numBottles=numBottles//numExchange
        #     s+=numBottles
        #     numBottles+=empty
        # # s+=numBottles
        return numBottles+(numBottles-1)//(numExchange-1);
