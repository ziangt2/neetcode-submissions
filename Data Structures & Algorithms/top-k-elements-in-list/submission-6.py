class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        bucket = [[] for _ in range(len(nums) +1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(nums),0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res