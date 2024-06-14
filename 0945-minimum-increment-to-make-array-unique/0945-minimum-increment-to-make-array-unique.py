class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                total+= increment

        return total