class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        test={}
        for i in nums:
            if i not in test:
                test[i]=1
            else:
                test[i]+=1
        max_freq = max(test.values())
        if max_freq == 1:
            return 1
        numb=[]

        for key, value in test.items():
            if max_freq == value:
                numb.append(key)
        for i in range(len(numb)):
            target = numb[i]
            start = 0
            end =0
            for j in range(len(nums)):
                if nums[j] == target:
                    start = j
                    break
            for j in range(len(nums)-1,-1,-1):
                if nums[j] == target:
                    end = j
                    break
            numb[i] = (end-start)+1

        return min(numb)
        