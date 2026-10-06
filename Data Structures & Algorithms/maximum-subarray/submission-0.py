class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        best = nums[0]
        for num in nums:
            current += num
            best = max(best, current)
            if current<0:
                current = 0
            

        return best