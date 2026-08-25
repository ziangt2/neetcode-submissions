import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)



        return -res