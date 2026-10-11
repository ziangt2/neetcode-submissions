from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1 = {}
        hash2 = defaultdict(list)
        for i in nums:
            hash1[i] = hash1.get(i, 0) + 1
        for i, j in hash1.items():
            hash2[j].append(i)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in hash2[i]:
                res.append(num)
                if len(res) == k:
                    return res