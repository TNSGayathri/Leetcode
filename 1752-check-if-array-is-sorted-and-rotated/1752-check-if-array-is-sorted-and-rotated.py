class Solution:
    def check(self, nums: List[int]) -> bool:
        if(nums==sorted(nums)):
            return True
        count = 0

        for i in range(len(nums)):
            
            if nums[(i-1) % len(nums)] > nums[i]:        
                count += 1

            if count > 1:
                return False
        
        return True
